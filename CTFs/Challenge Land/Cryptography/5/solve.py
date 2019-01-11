with open("cipher.txt", "rb") as f :
    cipher = f.read()
cipher = cipher.replace("\\x","").replace("\n","").decode("hex")
with open("out", "wb") as f :
    f.write(cipher)