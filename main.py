from Crypto.Cipher import AES
from Crypto.Hash import SHA3_256
from Crypto.Util.Padding import pad, unpad
BLOCK_SIZE = 16


def writeFileNew(name: str):
    f = open(name, "w")
    f.close()


def writeFileAdd(fileName: str, service: str, login: str, password: str):
    f = open(fileName, "a")
    f.write(service + ";" + login + ";" + password + "\n")
    f.close()


def readFileAll(name: str):
    f = open(name, "r")
    con = map(lambda a: a.split(";"), f.read().splitlines())
    f.close()
    return con


def findService(name: str, fileName: str):
    c = readFileAll(fileName)
    for line in c:
        if line[0] == name:
            return line
    return "No such line"


sha = SHA3_256.new()
sha.update(b"test")
key = sha.hexdigest()[:BLOCK_SIZE].encode('utf_8')

cipher = AES.new(key, AES.MODE_ECB)
msg = cipher.encrypt(pad(b'test', BLOCK_SIZE))
print(msg.hex())

decipher = AES.new(key, AES.MODE_ECB)
msg_dec = decipher.decrypt(msg)
print(unpad(msg_dec, BLOCK_SIZE))

# writeFileNew("test.txt")
# writeFileAdd("test.txt", "test1", "test2", "test3")
# writeFileAdd("test.txt", "test", "test2", "test3")
# writeFileAdd("test.txt", "test1", "test2", "test3")
# print(findService("test", "test.txt"))
