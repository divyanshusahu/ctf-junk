import string

message_chars = string.letters + string.digits + "-_.,;:?! "
solves = "cfkcifclacnldagddbdfmdihdlcdnneaieddefoeijeleenpfakfdffgafilflgfobgamgdhggcgingligodhaohdjhgehiphlkhofibaidliggijbilmiohjbcjdnjgijjdjlojojkbekdpkgkkjf"
solves += "kmakolakmanhbacbcnbfibidbkobnjcaeccplbgleblgmljhlmclonmbimedmgo"
cipher = "eaidagdagenpmgodlceijmgoefodlceijcnllonmgodlcfilfgamgodnnflgfgafilmgofildihdagmgoefodlccnlcnledddagmgoedddagfobdagedd"

key = {}
index = 0
s = solves
while s:
    key[s[:3]] = message_chars[index]
    index += 1
    s = s[3:]

c = cipher
m = ""
while c:
    m += key[c[:3]]
    c = c[3:]
print m
