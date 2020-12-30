# Luis Felipe Castaño
# El codigo completo (Con requirements) se encuentra en https://github.com/felipe-castano-95/Criptografia

import sympy as sympy
import gmpy2 as gmpy
import random

# _______________________________________________________ Primera Parte ___________________________

def key_generator():
	# Se define el rango para las semillas
	lowest_range =  10000
	highest_range = 99999

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

def encrypt(clear_num, e, n):
	return pow(clear_num, e, n)

def decrypt(encrypt_num, d, n):
	return pow(encrypt_num, d, n)

def sign_message(m, d, n):
	return pow(m, d, n)

def verify_sign(sign, message, e, n):
	aux = pow(sign, e, n)
	if(aux == message):
		return True
	else:
		return False


# Mis valores:

# a) Generar un par de claves RSA  y escribir la clave pública en el “Directorio de Claves Firma RSA” de Moodle.


print('')
print('______________________Primera parte')
print('')

print("Claves RSA")

#p, q, n, e, d = key_generator()
p =  90437
q =  77659
n =  7023246983
e =  79985
d =  4530120761

print("p = ", p)
print("q = ", q)
print("n = ", n)
print("e = ", e)
print("d = ", d)

m = 36363636

# Cifrado el mensaje 

e_martin_casado = 11
n_martin_casado = 781469496115823

print('Cifrando mensaje para Martin Casado Rodriguez: ', encrypt(m, e_martin_casado, n_martin_casado))

s_message = m % 1000003

print('Mensaje resumen: ', s_message)

print('Firmando mensaje resumen para Martin Casado Rodriguez: ', sign_message(s_message, d, n))


decrypt_message = decrypt(3439114531, d, n)
print('Descifrando mensaje de Abraham Sánchez Roldán: ', decrypt_message)

e_abrahan = 2345639
n_abrahan = 144467934683372227
s_sign_abrahan = 6346910895680002
s_message_abrahan = decrypt_message % 1000003

print('Verificando firma de Abraham Sánchez Roldán: ', verify_sign(s_sign_abrahan, s_message_abrahan, e_abrahan, n_abrahan))


#__________________________________________________ Segunda parte ________________________________________

def elgamal_key_generator(g, a, p):
	return pow(g, a, p)

def elgamal_encrypt(m, a, r, g, p):
	s1 = pow(g, r, p)
	q, s2 = divmod((m - (a * s1)) * gmpy.invert(r, p-1), p-1)
	return s1, s2

def elgamal_verify_signature(s1, s2, alfa, p, m, g):
	aux_1 = pow(alfa, s1, p)
	aux_2 = pow(s1, s2, p)
	q, t = divmod(aux_1 * aux_2, p)
	if(t == pow(g, m, p)):
		return True
	else:
		return False

# Generando el primo 
lowest_range =  100000
highest_range = 999999

# Se generan semillas en un rango para ingresar a la función generadora de primos
# p_seed = random.randint(lowest_range, highest_range)
# p = sympy.nextprime(p_seed)
p = 693619

print('')
print('______________________Segunda parte')
print('')

print("El primo selecionado es: ", p)

	 
# Seleccionando el generador
# g = random.randint(2, p - 2)
g = 67541
print("El generador es: ", g)

# Seleccionando b
# a = random.randint(2, p - 2)
a = 27701
print("a es: ", a)

alfa = elgamal_key_generator(g, a, p)

print("Public key: ", alfa)
print("Private key: ", a)

m = 12345
# r = random.randint(lowest_range, p-2)
# while sympy.igcd(r, p-1) != 1:
#	r = random.randint(lowest_range, p-2)
r = 571261

print('Mensaje para firmar')
print("r: ", r)
print("m: ", m)

print('Firmando mensaje: ', elgamal_encrypt(m, a, r, g, p))

print('Verificando el mensaje de Pablo Gómez de la Parra García: ', elgamal_verify_signature(1745, 1884, 2147483648, 2473, 12345, 2))

print('Verificando el mensaje de Pablo Ruiz Encinas: ', elgamal_verify_signature(45617, 31409, 4257, 73961, 456, 3))

# El mensaje de Pablo Gómez de la Parra García no se puede verifican porque el mensaje es mas grande que el p seleccionado..
