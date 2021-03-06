from Crypto.Cipher import AES
from Crypto.Hash import SHA3_256
from Crypto.Util.Padding import pad, unpad
import base64

BLOCK_SIZE = 16
FILENAME = "test.txt"


def getKey(key: str):
    sha = SHA3_256.new()
    sha.update(key)
    return sha.hexdigest()[:BLOCK_SIZE].encode('utf_8')


def encrypt(key: str, text: bytes):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pad(text, BLOCK_SIZE))


def decrypt(key: str, msg: bytes):
    decipher = AES.new(key, AES.MODE_ECB)
    msg_dec = decipher.decrypt(msg)
    return unpad(msg_dec, BLOCK_SIZE)


def writeFileNew(name: str):
    f = open(name, "w")
    f.close()


def writeFileAdd(service: str, login: str, password: str, key: str):
    f = open(FILENAME, "ab")
    f.write(encrypt(key, bytes(service + ";" +
                               login + ";" + password + "s", encoding='utf8')))
    f.close()


def readFileAll(name: str, key: str):
    fileName = open(name, "rb")
    allLines = map(lambda a: a.split(";"),
                   decrypt(key, fileName.read()).decode("utf-8").split("s"))
    fileName.close()
    return allLines


def findService(name: str, key: str):
    lines = readFileAll(FILENAME, key)
    for line in lines:
        if line[0] == name:
            return line
    return "No such line"


key = "test"
exit = True
while exit:
    val = input()
    if val == "exit":
        print("Exit")
        exit = False
    if val == "new":
        print("New file")
        writeFileNew(FILENAME)
    if val == "key":
        print("New key")
        key = getKey(input().encode("utf-8"))
    if val == "eN":
        if key == "":
            break
        print("Encrypt new service")
        writeFileAdd(input(), input(), input(), key)
    if val == "find":
        print("Find service")
        res = findService(input(), key)
        print(res)
        if res == "No such line":
            continue


# key = getKey(b"test")
# enc = encrypt(key, b"test")
# dec = decrypt(key, enc)

# decipher = AES.new(key, AES.MODE_ECB)
# msg_dec = decipher.decrypt(msg)
# print(unpad(msg_dec, BLOCK_SIZE))

# writeFileNew("test.txt")
# writeFileAdd("test.txt", "test1", "test2", "test3")
# writeFileAdd("test.txt", "test", "test2", "test3")
# writeFileAdd("test.txt", "test1", "test2", "test3")
# print(findService("test", "test.txt"))
