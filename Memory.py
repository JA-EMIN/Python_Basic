# g = 10                      # static(lobal)
#
# def fn():
#     # g = 100                 # stack
#     global g
#     g = 100
#     print('fn g=', g)
# fn()                        # fn() 종료 후 stack 영역의 g는 삭제
# print('g=', g)

# def fn():
#     myList = [10,20,30]       # list 객체는 heap 영역에 할당되지만, 객체를 참조하는 변수인 myList는 stack영역에 할당
# fn()
# print(myList)                 # myList변수는 함수 종료 후 삭제, heap 영역에 있는 list 객체는 참조 count가 0이 되므로 소멸

# def fn():
#     myList = [10,20,30]
#     print(id(myList))
#     return myList               #함수 종료전 return 변수의 값을 cpu 레지스터 영역에 임시저장 후 global영역의 rst로 전달
# rst = fn()                      #list객체는 참조 count가 0이 안됐으므로 살아있다.
# print(id(rst))

# print(dir(__builtins__))        #builtin 변수 및 함수, builtin 변수의 우선순위가 가장 낮음
#
# str = "abc"
# def fn():
#     str = 'cde'
#     print(str)
# fn()
# print(str)
#
# a = 10
# a = str(a)
# print(a)                        #str변수를 선언 후 builtin 함수로 쓸 수 없다

# #일급 함수
# def fn():                         #일급 함수의 기능 : 함수의 할당
#     print('hello')
#
# # fn1 = fn
# # fn()
# # fn1()
#
# def my(a):                        #함수를 인자로 전달 가능
#     a()
# my(fn)
#
# def my1():                        #함수의 리턴
#     return fn
# rst = my1()
# rst()
#
# #switch ~ case문의 대신하여 일급함수와 dictionary를 사용하여 대체 가능
# def afn():
#     print('afn')
#
# def bfn():
#     print('bfn')
#
# d = {0:afn, 1:bfn}
# menu = int(input("메뉴를선택:"))
# d[menu]()