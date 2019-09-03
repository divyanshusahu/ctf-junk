from bs4 import BeautifulSoup
import requests
import string

m = string.lowercase + string.uppercase + string.digits + " -_.,;:?!"
cipher = "59656A6B6F9F656A67746767"
url = "https://www.trytodecrypt.com/decrypt.php?id=13#headline"
cookies = {"PHPSESSID" : "1712427a8d1a8a693e152abfdf297fa0"}

message = ""
current_cipher = ""

