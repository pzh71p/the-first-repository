keep_going = True
while keep_going:
    code_letter = input("请打出你要加密の东西(英文和数字)")
    if code_letter == "":
        break
    outputcode = ""
    for letter in code_letter:
        if not letter.isupper():
            zimu = ord(letter) + 16
            letter = chr(zimu)
        else:
            zimu -= 16
            letter = chr(zimu)
        outputcode += letter
    print("输出の密码为：", outputcode)

