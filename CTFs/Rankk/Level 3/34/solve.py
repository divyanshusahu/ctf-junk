freq = {}
freq[' '] = 700000000
freq['e'] = 390395169
freq['t'] = 282039486
freq['a'] = 248362256
freq['o'] = 235661502
freq['i'] = 214822972
freq['n'] = 214319386
freq['s'] = 196844692
freq['h'] = 193607737
freq['r'] = 184990759
freq['d'] = 134044565
freq['l'] = 125951672
freq['u'] = 88219598
freq['c'] = 79962026
freq['m'] = 79502870
freq['f'] = 72967175
freq['w'] = 69069021
freq['g'] = 61549736
freq['y'] = 59010696
freq['p'] = 55746578
freq['b'] = 47673928
freq['v'] = 30476191
freq['k'] = 22969448
freq['x'] = 5574077
freq['j'] = 4507165
freq['q'] = 3649838
freq['z'] = 2456495

def scores(decodedString) :
    score = 0
    count = 0
    for i in decodedString :
        try :
            score += freq[i.lower()]
            count += 1
        except :
            continue
    return count

with open('t','rb') as f :
    cipher = f.read()

with open('keys.list', 'rb') as f :
    keys = f.readlines()

def xor(a,b) :
    m = ''
    for i in range(len(a)) :
        m += chr( ord(a[i]) ^ ord(b[i%len(b)]) )
    return m

max_score = 0
message = ""

for k in keys :
    key = k.rstrip()
    m = xor(cipher,key)
    s = scores(m)
    if s == len(cipher) :
        print m,key
