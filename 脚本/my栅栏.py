def rail_fence_decrypt(ciphertext, rails):
    # Remove the braces in the ciphertext
    ciphertext = ciphertext.replace('{', '').replace('}', '')

    # Initialize the matrix for the rail fence pattern
    rail = [['\n' for _ in range(len(ciphertext))]
                  for _ in range(rails)]
    
    # To find the places where the characters should be placed in the rail matrix
    dir_down = None
    row, col = 0, 0
    
    for i in range(len(ciphertext)):
        if row == 0:
            dir_down = True
        if row == rails - 1:
            dir_down = False
        # place the marker
        rail[row][col] = '*'
        col += 1
        
        if dir_down:
            row += 1
        else:
            row -= 1
    
    # Now we will place the ciphertext characters in the marked positions
    index = 0
    for i in range(rails):
        for j in range(len(ciphertext)):
            if rail[i][j] == '*' and index < len(ciphertext):
                rail[i][j] = ciphertext[index]
                index += 1
    
    # Read the matrix in a zigzag manner to construct the plaintext
    result = []
    row, col = 0, 0
    for i in range(len(ciphertext)):
        if row == 0:
            dir_down = True
        if row == rails - 1:
            dir_down = False
        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1
        
        if dir_down:
            row += 1
        else:
            row -= 1
    return "".join(result)

# 密文
ciphertext = "felhaagv{ewtehtehfilnakgw}"

# 栅栏数
rails = 2

# 解密
plaintext = rail_fence_decrypt(ciphertext, rails)
print(plaintext)
