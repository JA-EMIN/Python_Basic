# pair = {}
# while True:
#     strName = input('이름: ')
#     nAge = int(input('나이: '))
#     pair[strName] = nAge
#     result = input('계속입력하시겠습니까(y/n)?')
#     if result == 'n':
#         break
#
# print('-'*30)
# print('이름          나이')
# print('-'*30)
# for name, age in pair.items():
#     print('%-10s\t%5d' %(name, age))
#

data = []
while True:

     name = input("이름:")

     age =  input("나이:")

     yn = input("계속입력하시겠습니까(y/n)?")

     data.append({'name':name, 'age':age})

     if yn=='n':

        break
print("="*30)

print("이름 나이")

print("="*30)

for d in data:

     print("%(name)s     %(age)s"%d)