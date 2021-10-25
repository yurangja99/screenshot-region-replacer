from time import time
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class GUIManager:
  def __init__(self, title, image):
    # create tkinter GUI
    self.gui = tk.Tk()

    # get display size
    self.screen_width = self.gui.winfo_screenwidth()
    self.screen_height = self.gui.winfo_screenheight()

    # using display size, resize given image
    self.image = self.__resize_image(image)

    # set window config
    self.gui.title(title)
    self.width, self.height = self.image.size
    self.gui.geometry(f'{self.width}x{self.height}')
    self.gui.configure(background='grey')
    
    # create canvas on the GUI and render the source image
    self.image_tk = ImageTk.PhotoImage(self.image, master=self.gui)
    self.canvas = tk.Canvas(
      self.gui, 
      width=self.width, 
      height=self.height, 
      borderwidth=0, 
      highlightthickness=0
    )
    self.canvas.pack(expand=True)
    self.canvas.img = self.image_tk
    self.canvas.create_image(0, 0, image=self.image_tk, anchor=tk.NW)
    
    # set rectangle points and event handlers
    self.raw_left, self.raw_top, self.raw_right, self.raw_bottom = 0, 0, 0, 0
    self.left, self.top, self.right, self.bottom = 0, 0, 0, 0
    self.rect_id = self.canvas.create_rectangle(
      self.left, self.top, self.right, self.bottom,
      dash=(2, 2), 
      width=3, 
      fill='', 
      outline='red'
    )
    self.canvas.bind('<Button-1>', self.__handle_mouse_click)
    self.canvas.bind('<B1-Motion>', self.__handle_mouse_move)
    self.canvas.bind('<ButtonRelease-1>', self.__handle_mouse_leave)

    # set status
    self.displaying = True
    
    # start loop
    self.gui.mainloop()

  def __resize_image(self, image):
    # get image size
    width, height = image.size

    # compare with display size
    # min: 0.25 of display
    # max: 0.9 of display
    if width > 0.9 * self.screen_width or height > 0.9 * self.screen_height:
      self.ratio = min(0.9 * self.screen_width / width, 0.9 * self.screen_height / height)
    elif width >= 0.25 * self.screen_width or height >= 0.25 * self.screen_height: 
      self.ratio = 1.0
    else:
      self.ratio = min(0.25 * self.screen_width / width, 0.25 * self.screen_height / height)
    
    # resize and return image
    return image.resize((round(width * self.ratio), round(height * self.ratio)), Image.LANCZOS)

  def __handle_mouse_click(self, event):
    # set upper left point of selection rectangle
    self.left = max(0, min(self.width - 1, event.x))
    self.top = max(0, min(self.height - 1, event.y))

    self.raw_left = round(self.left / self.ratio)
    self.raw_top = round(self.top / self.ratio)

  def __handle_mouse_move(self, event):
    # set lower right point of selection rectangle
    self.right = max(0, min(self.width - 1, event.x))
    self.bottom = max(0, min(self.height - 1, event.y))

    self.raw_right = round(self.right / self.ratio)
    self.raw_bottom = round(self.bottom / self.ratio)
    
    self.canvas.coords(self.rect_id, self.left, self.top, self.right, self.bottom)

  def __handle_mouse_leave(self, event):
    # mouse leave means rectangle is selected, so close GUI
    self.gui.quit()
    self.gui.destroy()

    # close image
    self.image.close()

    # set status
    self.displaying = False

    # print box coordinates to debug
    print('resized', self.left, self.top, self.right, self.bottom)
    print('raw', self.raw_left, self.raw_top, self.raw_right, self.raw_bottom)


def main():
  # select object image
  messagebox.showinfo('이미지 선택', '바꾸고 싶은 이미지를 선택해주세요.')
  object_image_name = filedialog.askopenfilename(
    initialdir='./', 
    title='바꾸고 싶은 이미지 선택', 
    filetypes=[('이미지 파일', ('*.png', '*.jpg', '*.jpeg'))]
  )
  
  # select source image
  messagebox.showinfo('이미지 선택', '원하는 부분이 있는 이미지를 선택해주세요.')
  source_image_name = filedialog.askopenfilename(
    initialdir='./', 
    title='원하는 부분이 있는 이미지 선택', 
    filetypes=[('이미지 파일', ('*.png', '*.jpg', '*.jpeg'))]
  )
  
  if object_image_name == '' or source_image_name == '':
    # print error message and quit
    messagebox.showerror('이미지 선택 실패', '이미지를 선택하지 않아 프로그램을 종료합니다.')
  else:
    # open images and check size
    object_image = Image.open(object_image_name)
    source_image = Image.open(source_image_name)
    
    # check two image size is equal
    if object_image.size != source_image.size:
      # print error message and quit
      messagebox.showerror(
        '이미지 크기 불일치', 
        f'이미지의 크기가 다릅니다.\n' \
          + f'바꾸고 싶은 이미지: {object_image.size}\n' \
          + f'원하는 부분이 있는 이미지: {source_image.size})'
      )
    else:
      # create tkinter GUI
      gui = GUIManager(
        title='대체할 부분을 선택해주세요.', 
        image=object_image
      )

      # check GUI is well ended
      if gui.displaying:
        # print error message and quit
        messagebox.showerror('오류 발생', '이미지 창이 제대로 종료되지 않았습니다.')
      else:
        # crop selected region
        region = source_image.crop(box=(
          min(gui.raw_left, gui.raw_right), 
          min(gui.raw_top, gui.raw_bottom), 
          max(gui.raw_left, gui.raw_right), 
          max(gui.raw_top, gui.raw_bottom)
        ))

        # create new image from object image and paste the region
        result_image = object_image.copy()
        result_image.paste(region, box=(
          min(gui.raw_left, gui.raw_right), 
          min(gui.raw_top, gui.raw_bottom)
        ))

        # save the new image
        result_image_name = f'이미지{round(time()) % 7919}.png'
        result_image.save(result_image_name)
        result_image.close()
        messagebox.showinfo('저장 완료', f'\"{result_image_name}\"에 완성된 이미지가 저장되었습니다!')

    # close images
    object_image.close()
    source_image.close()
    print('완료되었습니다!')


if __name__ == '__main__':
  main()
