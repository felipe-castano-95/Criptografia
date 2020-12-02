import sympy as sympy
import gmpy2 as gmpy
import random

def key_generator():
	# Se define el rango para las semillas
	lowest_range = 100000000000000000000000000000
	highest_range = 999999999999999999999999999999

	# Se generan semillas en un rango para ingresar a la función generadora de primos
	p_seed = random.randint(lowest_range, highest_range)
	p = sympy.nextprime(p_seed)

	q_seed = random.randint(lowest_range, highest_range)
	q = sympy.nextprime(q_seed)

	# Se valida que p y q no sean iguales
	while q == p :
		q_seed = random.randint(lowest_range, highest_range)
		q = sympy.nextprime(q_seed)

	# Se calcula n y phi
	n = p * q
	phi = (p - 1) * (q - 1)

	# Se genera aleatoriamente un e y se valida que sea coprimo con phi
	e = random.randint(lowest_range, phi)

	while sympy.igcd(e, phi) != 1:
		e = random.randint(lowest_range, phi)

	# Ahora se calcula d
	d = gmpy.invert(e, phi)

	return p, q, n, e, d

#p, q, n, e, d = key_generator()

p = 505141317670549849678181245351
q = 856825486537916261698279456997
n = 432817955283472992068419799106695754337233927813245510670947
e = 401136558219224704872856438015974446133345144052516428680923
d = 230164189249061986294420853671606755852622883248776787932187

print("p = ", p)
print("q = ", q)
print("n = ", n)
print("e = ", e)
print("d = ", d)

c = pow(888888, e, n)
print(c)
m = pow(c, d, n)
print(m)
