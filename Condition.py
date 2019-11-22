# nNumber = input("정수를 입력하세요 : ")
# while nNumber.isalnum():
#     nNumber = int(nNumber)
#     if nNumber % 2:
#         print("짝수")
#     else:
#         print("홀수")
#     nNumber = input("정수를 입력하세요 : ")

# python에서는 3항연산자를 지원하지 않고 if문 축약형이 존재
# a = 3
# rst = 100 if a > 0 else 200
# print(rst)

nNumber = input("정수를 입력하세요 : ")
while nNumber.isalnum():
    nNumber = int(nNumber)
    print('even' if nNumber % 2 is 0 else '홀수')
    nNumber = input("정수를 입력하세요 : ")
