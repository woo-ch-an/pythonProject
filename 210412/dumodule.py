class duclass():
    var = None
    def dufunc1(self):
        f = open("dulist.txt",'r',encoding='UTF8')
        while 1:
            line = f.readline()
            line = line.rstrip()
            if not line: break
            print(line)
        f.close()