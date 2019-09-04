cipher = "q{vpln'bH_varHuebcrqxetrHOXEj"

key = 23
#message = "flag{"
message = ""
for i in cipher :
	message += chr(ord(i)^23)

print message