from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from datetime import datetime
from Crypto.Util.strxor import strxor

def gettime(): return int((datetime.now() - datetime(1970,1,1)).total_seconds()).to_bytes(8, byteorder='big')

def ANSI_x719_PRNG(k1, k2, Vi):
	key = key1+key2
	DTime = gettime()

	#encrypt/d/e the Date/Time String
	ede1 = DES3.new(key, DES3.MODE_ECB)
	ede1out = ede1.encrypt(DTime)
	#xor it with the seed value
	ede2in = strxor(ede1out, Vi)
	#encrypt/d/e the xor'd value to find Pt
	ede2 = DES3.new(key, DES3.MODE_ECB)
	Rt = ede2.encrypt(ede2in)
	#xor Pt with the first ede
	ede3in = strxor(Rt, ede1out)
	#encrypt/d/e the xor'd value
	ede3 = DES3.new(key, DES3.MODE_ECB)
	Vt1 = ede3.encrypt(ede3in)
	#prints Vt+1 for testing purposes
	#print('Vt('+ str(i) + '): ' + str(int.from_bytes(Vt1, 'big')))
	#return the Pt and the 
	return(Rt, Vt1)


if __name__ == '__main__':
	key1 = get_random_bytes(8)
	key2 = get_random_bytes(8)
	v = get_random_bytes(8)

	print('k1: ', key1.hex())
	print('k2: ', key2.hex())
	print('Vi: ', v.hex())

	#loop it to find the first 5 values for 
	for i in range(5):
		r = ANSI_x719_PRNG(key1, key2, v)
		print('R('+ str(i+1) + '): ' + str(int.from_bytes(r[0], 'big')))
		v = r[1]