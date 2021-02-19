from Crypto.Cipher import AES

# s = AES.new()

def writeNew(name, content):
    f = open(name, "w")
    f.write(content)
    f.close()


def writeApp(name, content):
    f = open(name, "a")
    f.write(content)
    f.close()


def readFile(name):
    f = open(name, "r")
    con = f.read()
    f.close()
    return con
