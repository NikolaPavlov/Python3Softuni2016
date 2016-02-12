ERROR_MSG = 'INVALID INPUT'
ORD_A = ord('A')
cipher_step = input()
input_text = input()


try:
    cipher_step = int(cipher_step)
    text_ciphered = ''
    for ch in input_text:
        if ch.isalpha():
            char_as_num = ord(ch)
            ciphered_char_as_num = char_as_num - cipher_step
            if ciphered_char_as_num < ORD_A:
                ciphered_char_as_num += 26
            text_ciphered += chr(ciphered_char_as_num)
        else:
            text_ciphered += ch
    print(text_ciphered)
except:
    print(ERROR_MSG)
