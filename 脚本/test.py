input = 'afZ_r9VYfScOeO_UL^RWUc'

output_list = []
for i in range(len(input)):
    output_list.append(chr(ord(input[i]) + i + 5))
print(''.join(output_list))