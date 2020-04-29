#my password maker v1.0 premium
#import moduls
import random
from time import sleep
import datetime, os
from colorama import *


init(autoreset=True)


#simvols
chars = input('какие символы будут использоватся? :')



#grafi interfeis
print (Fore.BLUE + 'вас приветствует my password for brut maker v1.0 сокрощенно pfb v1.0 premium')
sleep (2)
print (Fore.MAGENTA + 'приятного использования! ;)')
sleep (1)
print (Fore.GREEN + 'рекомендовано начинать от 10000 или более.')

password_namber = int(input('сколько паролей будет?: '))

light = int(input('сколько символов в пороле?: '))

#over
for x in range( password_namber ):
	password = ''

	for i in range( light ):
		password += random.choice( chars )

	print(Back.YELLOW + 'вот пороль: ' + password )

	file = open( 'brut.txt', 'a')
	file.write( '\n' + password )
	file.close()
sleep (1)
print (Back.CYAN + 'спасибо за использование ❤')
print (Fore.MAGENTA + 'программу создал boti :)')
print (Fore.MAGENTA + 'спасибо за использование')
input()