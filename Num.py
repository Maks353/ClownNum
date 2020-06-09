import urllib.request
import json
from time import sleep

print ("ClowNum")

phone = input("number: ")

getInfo = "https://htmlweb.ru/geo/api.php?json&telcod=" + phone

try:
        infoPhone = urllib.request.urlopen( getInfo )
       

except:
        print( "\n[!] - Phone not found - [!]\n" )

infoPhone = json.load( infoPhone )

print( u"Number >>>", "+" + phone )
print( u"Country >>>", infoPhone["country"]["name"] )
print( u"Region >>>", infoPhone["region"]["name"] )
print( u"Okrug >>>", infoPhone["region"]["okrug"] )
print( u"Operator >>>", infoPhone["0"]["oper"] )
print( u"World >>>", infoPhone["country"]["location"] )

