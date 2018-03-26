#!/usr/bin/env python3.5
#-*- coding: utf-8 -*-

import cryptocompare as crypto


Crypto = crypto.get_coin_list(format=True)

def ListeCrypto():
	for n in Crypto :
		print (n)

def Demande():
	
	Monnaie = input('Entrez le nom de la monnaie dont vous voulez connaitre le prix ou "Liste" pour avoir la liste de toute les Crypto-Monnaies: ')
	if Monnaie in Crypto :
		print (crypto.get_price([Monnaie],['EUR','GBP']))
	elif Monnaie == 'Liste': 
		ListeCrypto()
	else :
		print("La crypto-monnaie que vous demande n'est pas dans notre base de données ")


ListeCrypto()
while 1 :
	Demande()
