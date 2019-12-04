#Package로 만들기 위해서 폴더내에__init.py__ 파일이 필요
#__init.py__ 파일의 역할은 패키지 폴더내에 어떠한 파일이 있다는 것을 알려준다

from .cat import Cat # . <-"이 폴더에 있는" cat.py 이라는 파일에서 Cat이라는 클래스를 갖고와줘
from .dog import Dog