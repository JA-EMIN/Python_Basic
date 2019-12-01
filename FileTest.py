# open(filename, mode, encoding) - file object return
# mode = r, w, a
def FileWrite():
    fp = open("test.txt", "w")
    # print(fp.tell())            #fp의 위치
    fp.write("abcndefnghi")
    fp.write("\nabcndefnghi")
    # fp.seek(3)                  #fp의 위치를 강제로 변경
    # print(fp.tell())
    # fp.write("hello")
    fp.close()

def FileRead():
    # fp = open("test.txt", "r")
    # # rd = fp.read()      #파일의 전체 내용을 읽어옴
    # # rd = fp.read(3)        #3글자를 읽어옴
    # while True:
    #     rd = fp.read(3)
    #     if rd is not '':
    #         print(rd)
    #     else:
    #         break
    fp = open("test.txt", "r")
    # for r in fp:           # 파일의 전체 내용을 읽을 때 사용, fp가 readline() 단위로 동작
    #     print(r)
    rd = fp.readlines()      # line 단위로 읽은 것을 리스트 객체로 만들어줌
    print(rd)
    fp.close()


FileWrite()
FileRead()

def fn1():
    return (10, 20, 30)
rst1, rst2 = fn1()
print( rst1, rst2 )