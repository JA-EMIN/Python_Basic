# def hello():
# #     print('hello')
# #     print('fn')
# #
# # def plus(a, b):
# #     return  a+b
# #
# # # python은 return 값 여러개 가능 : tuple로 반환
# # def fn1(a, b):
# #     return 10, 20, 30, 40
# #
# # # 명시적 인자 호출
# # n = 10
# # m = 20
# # print(n, m, sep='*')        #print 함수에 sep 인자 존재 디폴트 ' '
# # print('hello', end = '')    #print 함수에 end 인자 존재 디폴트 '\n'
# # print('hi')
# #
# # #default 인자 호출
# # def fn3(a=10, b=20, c=30):
# #     print(a, b, c)
# # fn3()
# # fn3(100)
# # fn3(100,200)
# # fn3(100,200,300)

# #가변인자
# def fn4(*args):          #인자의 갯수가 정해져있지 않고, type이 tuple로 정해진다
#     print(args)
#     for n in args:
#         print(n, end=' ')
#
# fn4(10, 20, 'bb')

# def fn5(*args):
#     # data = [n*n*3.14 for n in args]
#     # print(data)
#     for n in args:
#         print(n, "의 원의면적:", n**2*3.14, sep='')
#
# fn5(3,4,5)

# #정의되지 않은 인자
# def fn6(**args):          #가변인자처럼 인자의 갯수는 정해져 있지 않으나, 변수명=값 형식으로 전달해야한다.
#     print(args)           #명시적 인자 호출과 유사하지만 인자가 정해져있지 않다
#                           #dictionary로 변환된다
# fn6(name='홍길동', age=10)
# fn6(aa=100, bb=200, cc=300)

def factor():
    n = int(input("정수입력: "))
    # factor = [x for x in range(1, n+1) if n % x == 0]
    f = []
    for x in range(1, n+1):
        if n%x == 0:
            f.append(x)
    return f


print(factor())