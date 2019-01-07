from itertools import permutations
from Crypto.Hash import MD4

hashed = '199566213bdb180d75358de558e0705e'
password_string = 'abcdefghijklmnopqrstuvwxyz0123456789'

for l in range(1,6) :
    print 'Trying Length %s' % str(l)
    cur = permutations(password_string, l)
    for s in cur :
        cur = ''
        for i in s :
            cur += i
        h = MD4.new()
        h.update(cur)
        cur_hash = h.hexdigest()
        if cur_hash == hashed :
            print cur
            break