import sys
import random

#
# # print(sys.argv)     #첫번째 인자는 해당 파일명
# # my = sys.argv
# #
# # for arv in my:
# #     print(arv)
#
# myList = [10, 20, 30]
# myList1 = myList
# print(sys.getrefcount(myList)-1)
# sys.stdout.write('aa\n')
# sys.stdout.write('bb\n')


# for n in range(5):
#     print(random.randint(1,5))          #1<= n <=5   #중복이 허용됨

myList = [n for n in range(1, 46)]
# print(myList)
# print(random.choice(myList))                         #DATA를 임의로 한개 선택
for n in range(5):
    tList = random.sample(myList, 6)                   #DATA를 임의로 n개 선택
    print(tList)

# random.shuffle(myList)                    #중복없는 DATA를 얻을 때 이용 가능
# print(myList)
