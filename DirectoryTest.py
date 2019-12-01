import os
import re
import glob

# os.listdir : 현재 파일 및 디렉터리 목록
# os.getcwd() : 현재 경로 디렉터리
# os.path.isdir() : 디렉터리 존재유무
# if os.path.isdir("MyMath"):
#     print("Exist")
# os.path.isfile() : 디렉터리 존재유무
# if os.path.isfile("FileTest.py"):
#     print("Exist")
# os.mkdir() : 디렉터리 만들기
# os.system() : 커맨드 실행
# os.popen() : 커맨드 실행에 대한 파일객체
# glob : 파일 필터링 모듈

# print(os.listdir(os.getcwd()))
# print(os.path.isdir("Game"))
# print(os.path.isfile("test.txt"))
# cwdPath = os.getcwd()
# if not os.path.isdir("Menu"):
#     os.mkdir(os.path.join(os.getcwd(), "Menu"))
# else:
#     os.rmdir(os.path.join(os.getcwd(), "Menu"))
# print(os.path.join(os.getcwd(), "My"))

# os.system('notepad')

# fp = os.popen('dir')
# reg = re.compile('[a-zA-Z]+.py')
# for p in fp:
#     m = reg.search(p)
#     if m:
#         print(m.group())

print(glob.glob('*.py'))