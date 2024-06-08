def caesar_decrypt(ciphertext, shift):
    decrypted = []
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                decrypted.append(chr((ord(char) - ord('a') - shift) % 26 + ord('a')))
            elif char.isupper():
                decrypted.append(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
        else:
            decrypted.append(char)
    return ''.join(decrypted)

input = "synt{5pq1004q-86n5-46q8-o720-oro5on0417r1}"

# 尝试所有可能的位移（从0到25）
for shift in range(26):
    decrypted_text = caesar_decrypt(input, shift)
    print(f"Shift {shift}: {decrypted_text}")