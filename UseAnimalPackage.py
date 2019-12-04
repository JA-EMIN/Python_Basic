# from Animal import *
#
# d = Dog()
# d.hi()
#
# c = Cat()
# c.hi()

# from geopy.geocoders import Nominatim
# geolocator = Nominatim(user_agent="jany")
# location = geolocator.geocode("Seoul, South Korea")
# print(location.address)
# print(location.latitude)
# print(location.raw)

fruit = ["사과", "사과", "바나나", "바나나", "딸기", "키위", "복숭아", "복숭아", "복숭아"]

dic = {}
for key in fruit:
    if key in dic:
        dic[key] = dic[key] + 1
    else:
        dic[key] = 1

for k, v in dic.items():
    print("key : {0}, value : {1}".format(k, v))