from os import system
from time import sleep
import sys

cmd = system

def barras():
	print('=' * 40)
	print('{:^30}'.format('verificador de pacote'.upper()))
	print('=' * 40)

def procura():
	barras()
	print('\n')
	entrada = input('digite o nome do pacote:  ')
	comando = cmd(f'which {entrada}')
	cmd('clear')
	print('procurando o pacote...'.upper())
	sleep(4)
	cmd('clear')
	if comando == 0:
		print(f'o pacote {entrada} ja estar instalado!!!'.upper())
	elif comando != 0:
		print(f'o pacote {entrada} não estar instalado!!!\n'.upper())
		sleep(2)
		cmd('clear')
		print(f'instalando o pacote {entrada}\n'.upper())
		sleep(2)
		cmd('clear')
		instalador = cmd(f'apt install {entrada} -y')
		if instalador != 0:
			cmd('clear')
			sleep(3)
			print('algo deu errado meu parça'.upper())
			sleep(3)
			sys.exit()
		elif instalador == 0:
			cmd('clear')
			print(f'tudo ocorreu bem e o pacote {entrada} foi instalado')
	

procura()
