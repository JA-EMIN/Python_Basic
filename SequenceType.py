# 순서있는 데이터 타입(인덱스, 슬라이싱)
# list, tuple, string, byte

# 변경가능(mutable) 데이터 타입
# list, dict, set

# 순서없는 데이터 타입(인덱스 & 슬라이싱 X)
# set, dict

# 변경불가능(immutable) 데이터 타입
# tuple, string, byte

# # list type (순서가 있고, 변경이 가능)
# [] or list()
# append, count, extend, index, insert
# remove, pop, del
# list에 +, * 연산자 사용 가능
# 패킹은 불가능하나 언패킹은 가능

# remove() 함수는 첫번째 나오는 객체만 삭제
# pop() 가장 마지막 객체 삭제, index를 지칭하면 해당 객체 삭제
# del() 함수로도 list내 객체 삭제 가능
# index() 해당 객체가 몇번째에 있는지
# count() 해당 객체가 몇번 나오는지
# len(list) list 전체 길이

# myList = [10, 3.14, True, "abc"]
# print(myList)
# print(type(myList))
# print(myList[3])
# print(myList[-1])
# print(myList[0:3:1])
# print(myList[1:3:2])

# myList = [10, 20, 30, 40]
# myList[0] = 100  #mutable
# myList.append(50)
# myList.insert(1, 100)
# myList.extend([1, 2, 3]) # myList += [1, 2, 3]
# myList = myList * 3      # list 3회 반복
# # myList.remove(30)
# # myList.pop()
# # del(myList[3])
# n = myList.index(30)
#
# # n = len(myList)
# print(n)
# print(myList)

# # Quiz1
# s = 'abcd efgh ijklm'
# print(s.split())
# print(s[5:9])
# print(s[0::2])
# print(s[-1:-6:-1])
#
# s = 'abc def ghi'
# s_list = s.split()
#
# print(s_list[len(s_list)-1])

# # Tuple Type(순서가 있고, 변경 불가능)
# () or tuple
# index, slicing 가능
# 패킹, 언패킹이 가능

# myT = (10, 20, 30, 40)
# print(myT)
# print(type(myT))
# print(myT[2])
# print(myT[0::2])
# a = 10
# b = 20
# c = 30
# a, b, c = 10, 20, 30    #, 연산자를 사용하여 한번에 선언 가능
# print(a,b,c)
# a,b,c = (100, 200, 300)   #언패킹 : ()를 붙여도 튜플의 요소 갯수만큼 참조변수가 있다면 ()를 삭제하는 효과
# print(a,b,c)

# a = 100, 200, 300           #패킹 : ()를 안붙여도 자동으로 튜플로 생성
# print(a)


# # dict Type(순서가 없고, 변경 가능)
# {key:value} or dict()
# Key 중복은 불가능, 중복시 overwrite
# index, slicing 불가능
# myD = {10:"aa", 20:"bb", 30:"cc"}
# print(myD)
# print(type(myD))
# print(myD[20])              #Key값을 통해서 접근
# print(myD.get(20))
# myD[10]="AA"
# print(myD)
# myD[40] = "dd"
# print(myD)                  #key가 있으면 수정, 없으면 추가
# print(myD.pop(20))          #pop()에 해당되는 value 리턴 후 pop()
# del[myD[20]]
# print(myD)
# print(myD.keys())
# print(myD.values())
# print(myD.items())          #list의 구성요소로 tuple을 만들어줌
# s = list(myD.items())
# print(s[0])

# # dict Type(순서가 없고, 변경 가능)
# 중복없는 데이터를 저장
# index, slicing 불가능
# {} or set()
# add, remove
# 집합 연산이 가능

mySet1 = {10, 20, 30, 100, 20, 30}
mySet2 = {20, 30, 40, 50}
mySet1.add(1000)

print(mySet1 & mySet2)                  #교집합
print(mySet1.intersection(mySet2))      #교집합
print(mySet1 | mySet2)                  #합집합
print(mySet1 - mySet2)                  #차집합
print(mySet1 ^ mySet2)                  #대상 차집합(합집합 - 교집합)
