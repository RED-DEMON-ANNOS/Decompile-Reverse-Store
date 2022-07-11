#!/usr/bin/python2
# -*- coding:utf-8 -*-
#kalo mau ricod izin dulu
#izin dulu kontol asu memek
# Decode By Demon
import os, sys, re, time
import binascii, base64, marshal, zlib
from py_compile import compile as _compile
try:
	import uncompyle6
except ImportError:
	os.system('pip2 install uncompyle6')

d = '\x1b[90;1m'
m = '\x1b[91;1m'
h = '\x1b[92;1m'
k = '\x1b[93;1m'
b = '\x1b[94;1m'
j = '\x1b[95;1m'
a = '\x1b[96;1m'
p = '\x1b[97;1m'

Xenzi = "\x1b[96;1m\n _______          _________          _______  _       \n(  ____ )|\     /|\__   __/|\     /|(  ___  )( (    /|\n| (    )|( \   / )   ) (   | )   ( || (   ) ||  \  ( |\n| (____)| \ (_) /    | |   | (___) || |   | ||   \ | |\n|  _____)  \   /     | |   |  ___  || |   | || (\ \) |\n| (         ) (      | |   | (   ) || |   | || | \   |\n| )         | |      | |   | )   ( || (___) || )  \  |\n|/          \_/      )_(   |/     \|(_______)|/    )_)                                                      \n                   "+h+"Version "+p+"0.3"
Ganz = """
\x1b[96;1m╭─[\x1b[97;1m+\x1b[96;1m] \x1b[97;1mCreator \x1b[96;1m: \x1b[93;1mXenzi X Aldi X Mr.1557
\x1b[96;1m├─[\x1b[97;1m+\x1b[96;1m] \x1b[93;1mGithub  \x1b[96;1m: \x1b[92;1mhttps://github.com/Aldi098
\x1b[96;1m╰─[\x1b[97;1m+\x1b[96;1m] \x1b[92;1mScript  \x1b[96;1m: \x1b[96;1m( \x1b[92;1mCompile \x1b[96;1m) \x1b[90;1mX \x1b[96;1m( \x1b[92;1mDecompile \x1b[96;1m)

\x1b[96;1m[\x1b[91;1m!\x1b[96;1m] \x1b[97;1mNote \x1b[96;1m: \x1b[93;1mKlik CTRL Z Untuk Keluar Dari Script"""
tod = []


def save_file(outfile, value):
	open(outfile, 'w').write(value[0])
	del value[::]
	main_menu(a+'\n['+h+'√'+a+'] '+p+'File Saved '+a+outfile)

class Compile:
	def __init__(self, file):
		try:
			self.code = open(file).read()
			self.outfile = str('enc_'+file)
			self.filename = str(file)
		except Exception as exception:
			main_menu(exception)

	def marshal(self):
		tod.append('import marshal\nexec marshal.loads({code})'.format(code=repr(marshal.dumps(compile(self.code, self.filename, 'exec')))))
		save_file(self.outfile, tod)

	def pyc(self):
		_compile(self.filename)
		main_menu(a+'\n['+h+'√'+a+'] '+p+'File Saved '+a+self.filename+'c')

	def zlib(self):
		tod.append('import zlib\nexec zlib.decompress({code})'.format(code=repr(zlib.compress(self.code))))
		save_file(self.outfile, tod)

	def base16(self):
		tod.append('import base64\nexec base64.b16decode("{code}")'.format(code=base64.b16encode(self.code)))
		save_file(self.outfile, tod)

	def base32(self):
		tod.append('import base64\nexec base64.b32decode("{code}")'.format(code=base64.b32encode(self.code)))
		save_file(self.outfile, tod)

	def base64(self):
		tod.append('import base64\nexec base64.b64decode("{code}")'.format(code=base64.b64encode(self.code)))
		save_file(self.outfile, tod)

	def hex(self):
		tod.append('import binascii\nexec binascii.unhexlify("%x" % int("{code}", 0))'.format(code=hex(int(binascii.hexlify(self.code),16))))
		save_file(self.outfile, tod)

	def bin(self):
		tod.append('import binascii\nexec binascii.unhexlify("%x" % int("{code}", 0))'.format(code=bin(int(binascii.hexlify(self.code),16))))
		save_file(self.outfile, tod)


class Decompile:
	def __init__(self, file):
		try:
			self.code = open(file).read()
			self.outfile = str('dec_'+file)
			self.filename = str(file)
		except Exception as exception:
			main_menu(exception)

	def marshal(self):
		if 'marshal.loads' in self.code:
			if 'c\\x00' in self.code:
				if ')))' in self.code:
					code = re.search('marshal.loads(.+)', self.code).group()[:-2]
				elif '(marshal.loads(' in self.code:
					code = re.search(r'[(]marshal.loads(.+)', self.code).group()[1:][:-1]
				else:
					code = re.search(r'marshal.loads(.+)', self.code).group()
			else:
				main_menu(a+'\n['+m+'!'+a+'] '+p+'File not supported')
		else:
			main_menu(a+'\n['+m+'!'+a+'] '+p+'File not supported')
		open('_Xenzi_', 'w').write('#Decompile BY Xemzi Ganz\nimport marshal, sys\n__import__("uncompyle6").main.decompile(2.7, {code}, sys.stdout)'.format(outfile=self.outfile, code=str(code)))
		os.system('python2 _Xenzi_ > {hasil}'.format(hasil=self.outfile))
		os.remove('_Xenzi_')
		exit(a+'\n['+h+'√'+a+'] '+p+'File saved '+a+self.outfile)

	def pyc(self):
		os.system('uncompyle6 {filename} > {hasil}'.format(filename=self.filename, hasil=self.filename[:-4]+'_dec.py'))
		main_menu(a+'\n['+h+'√'+a+'] '+p+'File saved '+a+self.filename[:-4]+'_dec.py')

	def zlib(self):
		if 'zlib.decompress' in self.code:
			if ')))' in self.code:
				code = re.search(r'zlib.decompress(.+)', self.code).group()[:-2]
			elif '(zlib.decompress(' in self.code:
				code = re.search(r'[(]zlib.decompress(.+)', self.code).group()[1:][:-1]
			else:
				code = re.search(r'zlib.decompress(.+)', self.code).group()
		else:
			main_menu(a+'\n['+m+'!'+a+'] '+p+'File not supported')
		exec 'print >> open("{hasil}", "w"), {code}'.format(hasil=self.outfile, code=str(code))
		exit(a+'\n['+h+'√'+a+'] '+p+'File saved '+a+self.outfile)

	def base16(self):
		if 'base64.b16decode' in self.code:
			if ')))' in self.code:
				code = re.search(r'base64.b16decode(.+)', self.code).group()[:-2]
			elif '(base64.b16decode(' in self.code:
				code = re.search(r'[(]base64.b16decode(.+)', self.code).group()[1:][:-1]
			else:
				code = re.search(r'base64.b16decode(.+)', self.code).group()
		else:
			main_menu(a+'\n['+m+'!'+a+'] '+p+'File not supported')
		exec 'print >> open("{hasil}", "w"), {code}'.format(code=str(code), hasil=self.outfile)
		exit(a+'\n['+h+'√'+a+'] '+p+'File saved '+a+self.outfile)

	def base32(self):
		if 'base64.b32decode' in self.code:
			if ')))' in self.code:
				code = re.search(r'base64.b32decode(.+)', self.code).group()[:-2]
			elif '(base64.b32decode(' in self.code:
				code = re.search(r'[(]base64.b32decode(.+)', self.code).group()[1:][:-1]
			else:
				code = re.search(r'base64.b32decode(.+)', self.code).group()
		else:
			main_menu(a+'\n['+m+'!'+a+'] '+p+'File not supported')
		exec 'print >> open("{hasil}", "w"), {code}'.format(code=str(code), hasil=self.outfile)
		exit(a+'\n['+h+'√'+a+'] '+p+'File saved '+a+self.outfile)

	def base64(self):
		if 'base64.b64decode' in self.code:
			if ')))' in self.code:
				code = re.search(r'base64.b64decode(.+)', self.code).group()[:-2]
			elif '(base64.b64decode(' in self.code:
				code = re.search(r'[(]base64.b64decode(.+)', self.code).group()[1:][:-1]
			else:
				code = re.search(r'base64.b64decode(.+)', self.code).group()
		else:
			main_menu(a+'\n['+m+'!'+a+'] '+p+'File not supported')
		exec 'print >> open("{hasil}", "w"), {code}'.format(code=str(code), hasil=self.outfile)
		exit(a+'\n['+h+'√'+a+']'+p+' File saved '+a+self.outfile)

	def hex(self):
		if 'binascii.unhexlify' in self.code:
			if '))))' in self.code:
				code = re.search(r'binascii.unhexlify(.+)', self.code).group()[:-2]
			elif '(binascii.unhexlify(' in self.code:
				code = re.search(r'[(]binascii.unhexlify(.+)', self.code).group()[1:][:-1]
			else:
				code = re.search(r'binascii.unhexlify(.+)', self.code).group()
		else:
			main_menu(a+'\n['+m+'!'+a+'] '+p+'File not supported')
		exec 'print >> open("{outfile}", "w"), {code}'.format(outfile=self.outfile, code=str(code))
		exit(a+'\n['+h+'√'+a+']'+p+' File saved '+a+self.outfile)

	def bin(self):
		if 'binascii.unhexlify' in self.code:
			if '))))' in self.code:
				code = re.search(r'binascii.unhexlify(.+)', self.code).group()[:-2]
			elif '(binascii.unhexlify(' in self.code:
				code = re.search(r'[(]binascii.unhexlify(.+)', self.code).group()[1:][:-1]
			else:
				code = re.search(r'binascii.unhexlify(.+)', self.code).group()
		else:
			main_menu(a+'\n['+m+'!'+a+'] '+p+'File not supported')
		exec 'print >> open("{outfile}", "w"), {code}'.format(outfile=self.outfile, code=str(code))
		exit(a+'\n['+h+'√'+a+'] '+p+'File saved '+a+self.outfile)


def main_menu(text=None):
	if text is not None:
		print text
		time.sleep(2.0)
	else:pass

	os.system('clear')
	print(Xenzi)
	print (Ganz)
	print (a+'\n╭─['+k+'1'+a+'] '+p+'Compile '+a+'( '+h+'Python '+a+')\n'+a+'├─['+k+'2'+a+'] '+p+'Decompile '+a+'( '+h+'Python '+a+')\n'+a+'╰─['+k+'3'+a+'] '+m+'Exit\n')

	try:
		choose = raw_input(a+'['+k+'•'+a+'] '+p+'Choose'+a+': '+h)
	except (EOFError, KeyboardInterrupt):pass

	if choose in ('1', '2', '3'):
		choose = int(choose)
		if choose == 1:
			compile_menu()
		elif choose == 2:
			decompile_menu()
		elif choose == 3:
			sys.exit('\n'+a+'['+k+'!'+a+'] '+p+'Exit')
	else:
		main_menu(a+'\n['+m+'!'+a+'] '+p+'Wrong Input')
	return


def compile_menu():
	os.system('clear')
	print(Xenzi)
	print (Ganz)
	print (a+'\n╭─['+k+'1'+a+'] '+p+'{0} '+k+'marshal '+a+'( '+h+'Python '+a+')\n'+a+'├─['+k+'2'+a+'] '+p+'{0} '+k+'pyc '+a+'( '+h+'Python '+a+')\n'+a+'├─['+k+'3'+a+'] '+p+'{0} '+k+'zlib '+a+'( '+h+'Python '+h+')\n'+a+'├─['+k+'4'+a+'] '+p+'{0} '+k+'base16 '+a+'( '+h+'Python '+a+')\n'+a+'├─['+k+'5'+a+'] '+p+'{0} '+k+'base32 '+a+'( '+h+'Python '+a+')\n'+a+'├─['+k+'6'+a+'] '+p+'{0} '+k+'base64 '+a+'( '+h+'Python '+a+')\n'+a+'├─['+k+'7'+a+'] '+p+'{0} '+k+'hex '+a+'( '+h+'Python '+a+')\n'+a+'├─['+k+'8'+a+'] '+p+'{0} '+k+'binascii '+a+'( '+h+'Python '+a+')\n'+a+'╰─['+k+'B'+a+'] '+p+'Back '+a+'( \x1b[90;1mmenu '+a+')\n').format('Compile')

	try:
		choose = raw_input(a+'['+k+'•'+a+'] Choose'+a+': '+h)
	except (EOFError, KeyboardInterrupt):pass

	if choose in ('1', '2', '3', '4', '5', '6', '7', '8'):
		try:
			file = raw_input(a+'\n['+p+'•'+a+'] '+p+'Input File'+a+': '+h)
		except Exception as exception:
			main_menu(exception)
		choose = int(choose)
		if choose == 1:
			Compile(file).marshal()
		elif choose == 2:
			Compile(file).pyc()
		elif choose == 3:
			Compile(file).zlib()
		elif choose == 4:
			Compile(file).base16()
		elif choose == 5:
			Compile(file).base32()
		elif choose == 6:
			Compile(file).base64()
		elif choose == 7:
			Compile(file).hex()
		elif choose == 8:
			Compile(file).bin()
	elif choose in ['b', 'B']:
		main_menu()
	else:
		main_menu(a+'\n['+m+'!'+a+'] '+p+'Wrong Input')
	return


def decompile_menu():
	os.system('clear')
	print(Xenzi)
	print (Ganz)
	print (a+'\n╭─['+k+'1'+a+'] '+p+'{0} '+k+'marshal '+a+'( '+h+'Python '+a+')\n'+a+'├─['+k+'2'+a+'] '+p+'{0} '+k+'pyc '+a+'( '+h+'Python '+a+')\n'+a+'├─['+k+'3'+a+'] '+p+'{0} '+k+'zlib '+a+'( '+h+'Python '+a+')\n'+a+'├─['+k+'4'+a+'] '+p+'{0} '+k+'base16 '+a+'( '+h+'Python '+a+')\n'+a+'├─['+k+'5'+a+'] '+p+'{0} '+k+'base32 '+a+'( '+h+'Python '+a+')\n├─['+k+'6'+a+'] '+p+'{0} '+k+'base64 '+a+'( '+h+'Python '+a+')\n'+a+'├─['+k+'7'+a+'] '+p+'{0} '+k+'hex '+a+'( '+h+'Python '+a+')\n'+a+'├─['+k+'8'+a+'] '+p+'{0} '+k+'binascii '+a+'( '+h+'Python '+a+')\n'+a+'╰─['+k+'B'+a+'] '+p+'Back '+a+'( \x1b[90;1mmenu '+a+')\n').format('Decompile')

	try:
		choose = raw_input(a+'['+k+'•'+a+'] '+p+'Choose'+a+': '+h)
	except (EOFError, KeyboardInterrupt):pass

	if choose in ('1', '2', '3', '4', '5', '6', '7', '8'):
		try:
			file = raw_input(a+'\n['+k+'•'+a+'] '+p+'Input File'+a+': '+h)
		except Exception as exception:
			main_menu(exception)
		choose = int(choose)
		if choose == 1:
			Decompile(file).marshal()
		elif choose == 2:
			Decompile(file).pyc()
		elif choose == 3:
			Decompile(file).zlib()
		elif choose == 4:
			Decompile(file).base16()
		elif choose == 5:
			Decompile(file).base32()
		elif choose == 6:
			Decompile(file).base64()
		elif choose == 7:
			Decompile(file).hex()
		elif choose == 8:
			Decompile(file).bin()
	elif choose in ['b', 'B']:
		main_menu()
	else:
		main_menu(a+'\n['+m+'!'+a+'] '+p+'Wrong Input')
	return


if __name__ == '__main__':
	main_menu()

# dec denggab gaya yah asu ngentod wkwkwkkwkwkwkwkwkwkwkkwkwkw

