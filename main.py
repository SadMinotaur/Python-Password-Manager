from Crypto.Cipher import AES


def writeFileNew(name):
    f = open(name, "w")
    f.close()


def writeFileAdd(fileName, service, login, password):
    f = open(fileName, "a")
    f.write(service + ";" + login + ";" + password + "\n")
    f.close()


def readFileAll(name):
    f = open(name, "r")
    con = map(lambda a: a.split(";"), f.read().splitlines())
    f.close()
    return con


def findService(name, fileName):
    c = readFileAll(fileName)
    for line in c:
        if line[0] == name:
            return line
    return "No such line"


writeFileNew("test.txt")
writeFileAdd("test.txt", "test1", "test2", "test3")
writeFileAdd("test.txt", "test", "test2", "test3")
writeFileAdd("test.txt", "test1", "test2", "test3")
print(findService("test", "test.txt"))
# s = AES.new()
