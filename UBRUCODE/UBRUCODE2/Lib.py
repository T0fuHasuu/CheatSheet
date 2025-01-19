def FindDiffInt():
    value1 = list(map(int, input().replace(',', '').split()[1:]))
    value2 = list(map(int, input().replace(',', '').split()[1:]))

    diff = list(set(value1) ^ set(value2))

    if diff:
        return f"{len(diff)} {', '.join(map(str, sorted(diff)))}"
    else:
        return "No Differences"
def Isogram():
    while True:
        dup = {}
        word = input().lower()
        if word == "stop":
            break
        
        for char in word:
            if char.isalpha():
                dup[char] = dup.get(char, 0) + 1
                
        if all(count == 2 for count in dup.values()):
            print("pair isogram")
        else:
            print("Not pair isogram")
def Palindrome():
    pd_count = 0
    x, y = map(int, input().split(", "))
    start, end = min(x, y), max(x, y)
    for i in range(start, end + 1):
        if str(i) == str(i)[::-1]:
            pd_count += 1
    return pd_count
def ViginereCypher():
    message = input().lower() 
    key = input().lower()
    key_repeated = ''.join([key[i % len(key)] for i, char in enumerate(message) if char != ' '])

    result = []
    key_index = 0

    for char in message:
        if char == ' ': 
            result.append(' ')
        else:
            m_index = ord(char) - ord('a')  
            k_index = ord(key_repeated[key_index]) - ord('a')
            encrypted_char = chr(((m_index + k_index) % 26) + ord('a'))
            result.append(encrypted_char)
            key_index += 1  
    return ''.join(result)
def ExcelConvert():
    while True:
        cell = input().strip()
        if cell == "r0c0":
            break
        row, col = map(int, cell[1:].split('c'))
        col_name = ""
        while col > 0:
            col -= 1
            col_name = chr(col % 26 + ord('A')) + col_name
            col //= 26
        print(f"{col_name}{row}")
            