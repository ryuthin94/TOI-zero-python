def encode_theos(s):
    result = ""
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result += str(count) + current_char
            current_char = s[i]
            count = 1
    
    result += str(count) + current_char
    return result

input_str = input()
output = encode_theos(input_str)
print(output)