def decode_bifid(s) :
    table = [
        ['a', 'f', 'k', 'p', 'u'],
        ['b', 'g', 'l', 'q', 'v'],
        ['c', 'h', 'm', 'r', 'w'],
        ['d', 'i', 'n', 's', 'x'],
        ['e', 'j', 'o', 't', 'y']
    ]

    message = ''
    i = 0
    while(i<len(s)) :
        if ord(s[i]) not in range(48,58) :
            message += s[i]
            i += 1
            continue
        message += table[int(s[i])-1][int(s[i+1])-1]
        i += 2
    return message

cipher = "543251 4243545134435154? 3551 113451 435354 42435451345144545141 4243 4254"
print decode_bifid(cipher)