

import os
import sys

os.system('apt-get upgrade && apt-get update')
os.system('apt install zaproxy')
os.system('apt-get install nmap')

a = input("Ip adresini gir  ")

print("""
1 = Basit tarama PORT ve portta çalışan uygulamarı gösterir.(Tahmini bitiş süresi 1dk)

2 = Orta derecede script taraması ve bütün portlar taraması sistem bilgisi.(Tahmini bitiş süresi 6DK) 

3 = Bütün olarak tarama web site taraması da yapılabilir.(Tahmini bitiş süresi 10DK)


""") 

giris = input("Hangi işlemi yapmak istersin:  ")


if (giris == 1):
	os.system('nmap {} -Pn -vvv'.format(a))

if (giris == 2):
	os.system('nmap {} -sC -Pn -vvv -O -sV '.format(a))


if (giris == 3):
	print(i)
	



i = input("Web sitesini taramak ister misiniz? (Y/N  ")


if  (i == "y"):
	slm = input("Web sitesini gir")

if (i == "n"):
	os.system('nmap {} -sC -Pn -vvv -O -A -sV -all  '.format(a))



owasp = os.system(' nmap {} -sC -Pn -vvv -O -A -sV -all -sS & qterminal -e owasp-zap  {}'.format(a,slm))