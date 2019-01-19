s = "abbbabaaabbabaaaabbaababaabaaaaaabbaaaababbabbbaabbbaabbabbbabbbabbaabababbbaabaaabaaaaaabbabaababbbaabbaabaaaaaabbaaaababbaabaaabbbabababbabbababbaaabaabbbaabaabbaaaababbbabaaabbaabab"
cipher = s.replace("a","0").replace("b","1")

def bintoascii(s) :
    m = ""
    while s :
        cur = s[:8]
        m += chr(int(cur,2))
        s = s[8:]
    return m

print bintoascii(cipher)