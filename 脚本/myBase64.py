import base64

#输入
input = "ZmxhZ3tUSEVfRkxBR19PRl9USElTX1NUUklOR30="

#解码
decoded_bytes = base64.b64decode(input)
output = decoded_bytes.decode('utf-8')

print(output)