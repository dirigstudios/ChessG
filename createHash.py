#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A simple script to generate keys for config.crypto cipher
# This module is not an active part of the T&DG UI_BOT, but is an useful resource
#
# T&DG UI_BOT copyright (r) Víctor Arzoz. All rights reserved :D

from Crypto.Random import get_random_bytes
import base64
selectnum = False
selectkey = False
selectbase = False
finish = False
while finish is False:
	num = 0
	key = b''
	while selectnum is False:
		num = input('Select the length of the key ')
		if num.isnumeric():
			num = int(num)
			print(num)
			n = input('Is the length correct? [y/n] ')
			if 'y' in n:
				selectnum = True
			elif 'n' in n:
				print('Retrying...')
			else:
				print("I don't understand you")
		else:
			print(f'The value {num} is not a number')
	while selectkey is False:
		key = get_random_bytes(num)
		print(f'The key is "{key}"')
		l = input('Do you like this key? [y/n] ')
		if 'y' in l:
			selectkey = True
		elif 'n' in l:
			print('Getting new key...')
		else:
			print("I don't understand you")
	while selectbase is False:
		base = input('Do you want to base64 the key? [y,n] ')
		if 'y' in base:
			selectbase = True
			key = base64.b64encode(key)
			print(f'Decoded key is {base64.b64decode(key, validate=True)}')
			print(f'Key is {key}')
		elif 'n' in base:
			selectbase = True
		else:
			print("I don't understand you")
	f = input('Do you want to generate another key? [y/n] ')
	if 'y' in f:
		selectnum = False
		selectkey = False
		selectbase = False
	elif 'n' in f:
		finish = True
	else:
		print("I don't understand you")