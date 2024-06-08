#这种编码常用于邮件中传输非 ASCII 字符

import quopri

# Quoted-Printable 编码的字符串
input = "=E9=82=A3=E4=BD=A0=E4=B9=9F=E5=BE=88=E6=A3=92=E5=93=A6"

# 解码
decoded_bytes = quopri.decodestring(input)
output = decoded_bytes.decode('utf-8')

print(output)