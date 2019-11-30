# # python -m py_compile xx.py ==> xx.pyc를 얻게됨
# import MyModule                     # 확장자 py, pyc, pyd
#
# rst = MyModule.plus(10, 20, 30)
# print(rst)
# rst = MyModule.multiple(10, 20, 30)
# print(rst)

# from MyModule import plus, multiple
# rst = plus(10, 20, 30, 40, 50)
# print(rst)
# rst = multiple(10, 20, 30, 40, 50)
# print(rst)

# from MyModule import *  #MyModule의 모든 함수
# rst = plus(10, 20, 30, 40, 50)
# print(rst)
# rst = multiple(10, 20, 30, 40, 50)
# print(rst)


# # 파이썬 path
# # venv는 실제 경로가 아닌 pycharm에서 제공해주는 가상경로
# import sys
# print (sys.path)
#
# # 다른 디렉토리 즉, 다른 경로에 있을 경우
# sys.path.append("c:\\")           # path 경로를 추가
# print (sys.path)

# 환경변수에 추가를 원할 시
# unix 계열
# export PYTHONPATH = $PYTHONPATH:/home/test/python/lib
# 윈도우 계열
# set PYTHONPATH = %PYTHONPATH%;C\myPython\userlib      #console이 열려있을 경우만 유지
# setx PYTHONPATH = %PYTHONPATH%;C\myPython\userlib