# Screenshot Region Replacer


## Abstract
![cover](examples/cover.jpg)
- 크기가 같은 이미지 2개가 있을 때, 한 이미지의 일부를 다른 이미지로 복사할 수 있는 프로젝트입니다. 
- 지우고 싶은 부분이 있을 때, 대체하고 싶은 부분이 있을 때 활용할 수 있습니다. 


## Examples
예시에 사용된 이미지들은 [pixabay](https://pixabay.com/)의 무료 이미지들을 활용하였습니다. 

### Example 1
- Object Image
    ![object1](examples/object1.jpg)
- Source Image
    ![source1](examples/source1.jpg)
- Result
    ![result1](examples/result1.jpg)

### Example 2
- Object Image
    ![object2](examples/object2.jpg)
- Source Image
    ![source2](examples/source2.jpg)
- Result
    ![result2](examples/result2.jpg)

### Example 3
- Object Image
    ![object3](examples/object3.jpg)
- Source Image
    ![source3](examples/source3.jpg)
- Result
    ![result3](examples/result3.jpg)


## Tech stacks
- Python 3.7.6
- Pipenv
- Packages: time, pillow, tkinter, pyinstaller


## How to use
파이썬 코드와 Windows를 위한 exe 파일을 함께 업로드하였습니다. 
각각에 대한 사용 방법은 아래와 같습니다. 

### Using python code
1. 파이썬 버전이 3.7.6과 비슷한지 확인합니다. 
버전이 완전히 같지는 않더라도 [사용하는 패키지](#tech-stacks)에 문제가 없다면 괜찮을 것 같습니다. 
2. pipenv나 conda를 사용한다면 가상 환경을 실행하고 다음 명령어로 필요한 패키지들을 설치합니다. 
    
    ```pip install -r requirements.txt```
3. 다음 명령어로 프로그램을 실행합니다. 
  
    ```python main.py```

### Using exe file (for Windows)
1. ```main.exe``` 실행 파일을 더블 클릭하여 바로 실행할 수 있습니다. 

### Generating exe file for modified python code
1. 파이썬 코드를 원하는 대로 수정합니다. 
2. 아래 명령어를 사용하여 수정된 파이썬 코드를 exe 실행 파일로 변환합니다. 
    
    ```pyinstaller main.py```

    이때, 아래와 같이 유용한 몇 가지 옵션들을 사용할 수 있습니다. 
    - ```-w```: exe 실행 파일을 실행하였을 때 cmd 창이 나타나지 않습니다. 
    - ```-F```: exe 실행 파일 하나만 생성합니다. 
3. 실행이 완료되면 ```build``` 폴더와 ```dist``` 폴더가 생성되는데, ```dist``` 폴더 안에 실행 파일이 생성됩니다. 
4. ```main.exe``` 실행 파일을 더블 클릭하여 새 실행 파일을 실행할 수 있습니다. 


## Future plans
- [ ] 지금은 object image에서만 rectangle을 선택할 수 있으므로 source image의 어떤 부분이 복사될지 가늠하기가 힘듭니다. 
따라서 둘 중 하나를 보거나 둘 모두를 보고 rectangle을 선택할 수 있도록 개선할 계획입니다. 
- [ ] 지금은 복사할 수 있는 도형이 rectangle 뿐인데, polygon에 대해서도 복사할 수 있도록 개발할 계획입니다. 
- [ ] rectangle을 선택할 때 이미지의 끝을 포함해야 하는 경우 마우스를 조절하여 rectangle을 선택하기가 힘든데, 이를 개선할 계획입니다. 


## Contributers
- NamSaeng
