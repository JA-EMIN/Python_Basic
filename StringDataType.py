# # \ 문자열이 길경우 연결 기호로 사용
#
# s1 = 'ab' \
#      'c'
# s2 = "abc"
#
# # ''' or """에서는 문자열 내부에 escape 문자없이 문자열을 제어 가능
# s3 = '''ab
#         c'''
# s4 = """ab
# c"""
#
# print(s1)
# print(s2)
# print(s3)
# print(s4)
# print(type(s1))
# print(type(s2))
# print(type(s3))
# print(type(s4))

# # 복합(시퀀스)
# 순서있는 데이터 타입(인덱스, 슬라이싱)
# s1 = 'abc'
# print(s1[0])
# print(s1[1])
# print(s1[-1])

# # 슬라이싱
# [시작:끝:증가치] 시작<= X < 끝
# s2 = 'abcdefghi'
# print(s2[0:4:1])
# print(s2[1:4])      # 증가치가 없는 경우 default 1
# print(s2[:5:2])     # 시작이 없는 경우 default 0
# print(s2[1:])       # 끝이 없는 경우 default : end of index
# print(s2[-1:-4:-1]) # i부터 시작하여 f이전까지 -1씩 증가

# # # +, *, %
# s1 = 'abcdefghi'
# s1 = s1 + 'jkl'  # + 문자열 붙이기
# print(s1)
# s1 = s1 * 2      # * 문자열 반복
# print(s1)
# a = 10
# b = 3.14
# s = 'abc'
# s1 = 'a=%10d b=%.2f s=%s'%(a, b, s)
# print(s1)       # % c언어의 formatting

# # s = "   abcd efg    "
# # s = s.split()          # 문자열을 기준점(매개변수 없을시 화이트 스페이스)으로 쪼개서 list 로 반환
# s = s.strip()            # 문자열 좌, 우의 화이트스페이스(공백,\n,\t) 삭제
# print(s)

# # s = 'abc'
# print(s[0])
# s[0] = 'A'                 # 문자열은 immutable이므로 바꿀수 없다

# s = b'abc'                   # byte 단위로 사용, 통신 어플에서 사용
# print(s)                     # octet(byte)-send,write > 장비(시리얼), 호스트(소켓)
# print( type(s) )
#
# s1 = 'abc'
# s1 = s1.encode('utf-8')      # byte 단위로 변환, 통신 어플에서 사용
# print(s1)                    # 문자 1개는 2bytes -> 1byte로 변환 필요
# print(type(s1))
#
# # 통신 어플 - octet(byte)-send,write > 장비(시리얼), 호스트
# # str --> byte
# s1 = 'abc'
# s1 = s1.encode('utf-8')      # byte 단위로 변환, 통신 어플에서 사용
# # 통신 어플 - octet(byte)-recv,read < 장비(시리얼), 호스트
# # str <-- byte
# s1 = b'abc'
# print(s1)
# print(type(s))
# s1 = s1.decode('utf-8')      # byte 단위로 변환, 통신 어플에서 사용
# print(s1)
# print(type(s1))


