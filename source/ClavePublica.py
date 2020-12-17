# Luis Felipe Castaño
# El codigo completo (Con requirements) se encuentra en https://github.com/felipe-castano-95/Criptografia

import sympy as sympy
import gmpy2 as gmpy
import random

# _______________________________________________________ Primera Parte ___________________________

def key_generator():
	# Se define el rango para las semillas
	lowest_range =  1000
	highest_range = 9999

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

def char_to_num(text):
	text = text.upper()
	n = len(text)
	num = 0
	for x in range(0,n):
		num += (ord(text[x]) - 65) * pow(26, n - x - 1)
	return num

def num_to_char(num):
	text = ""
	q = num
	while(q > 0):
		q, r = divmod(q, 26)
		text = chr(r + 65) + text 
	return text


# Mis valores:

# a) Generar un par de claves RSA mediante los cálculos indicados en la página 6 del documento TextbookRSA.pdf y escribirlas en el “Directorio de Claves RSA” de Moodle (desde la pestaña “Añadir entrada”).

#p, q, n, e, d = key_generator()

print("RSA")

p = 8819
q = 1847
n = 16288693
e = 8777675
d = 5916967

print("p = ", p)
print("q = ", q)
print("n = ", n)
print("e = ", e)
print("d = ", d)




# b) Utilizar la clave en la posición previa a la propia, del Directorio de Claves RSA, para codificar un mensaje numérico (El primer alumno en introducir una clave utilizará la clave propuesta por el profesor). Escribir los resultados en el “Canal mensaje numérico cifrado”. Cuando un compañero añada un mensaje cifrado dirigido hacia nosotros se añadirá un comentario en el mensaje del canal (Desde “Ver individual” “>Comentarios (0)” ) que indique si se descifra correctamente o no.

# Enviado mensaje a David Fernández Rodríguez
print("Encriptando mensaje a David Fernández Rodríguez: ", encrypt(12355, 7, 21132299602195509187553378240027))

# Descifrando mensaje númerico de Christian Vega González.. 123456
print("Desencriptando mensaje de Christian: ", decrypt(9021323, d, n))


# c) Utilizar la clave en la posición previa a la propia, del Directorio de Claves, para cifrar un mensaje de texto, teniendo en cuenta cuál es la longitud de bloque máxima permitida por la clave utilizada. Utilizar el alfabeto internacional según la codificación A=0, B=1,…,Z=25. Cuando un compañero añada un mensaje cifrado usando la clave propia se añadirá un comentario que indique el mensaje descifrado.

# Codificando mensaje de texto
print("Codificando mensaje de texto para David Fernández Rodríguez: ", num_to_char(encrypt(char_to_num('RSA'), 7, 21132299602195509187553378240027)))


# Desencriptando el mensaje en texto de Christian Vega González
print("Desencriptando mensaje de texto de Christian Vega González: ", num_to_char(decrypt(char_to_num('BEEVIG'), d, n)))





#__________________________________________________ Segunda parte ________________________________________

# a) Sea p=7883 un número primo y g=2 un generador. Escribir un mensaje en el “Canal Diffie-Hellman” para establecer una clave con otro y calcular (y escribir) una clave conmigo.



def diffie_hellman_key_exchange(a, p, g):
	return pow(g, a, p)

def get_full_key_diffie_hellman(B, a, p):
	return pow(B, a, p)

a = 5454
p = 7883
g = 2

print("Diffie_Hellman")
print("a = ", a)
print("p = ", p)
print("g = ", g)

A = diffie_hellman_key_exchange(a, p, g)

print('Calculando la clave para compartir: ', A)

print('Calculando clave con Héctor Diez: ', get_full_key_diffie_hellman(62, a, p))

print('Calculando clave con Christian Vega González: ', get_full_key_diffie_hellman(7768, a, p))


#__________________________________________________ Tercera parte ________________________________________

def elgamal_key_generator(g, b, p):
	return pow(g, b, p)

def elgamal_encrypt(m, be, r, g, p):
	c1 = pow(g, r, p)
	q, c2 = divmod(m * pow(be, r, p), p) # Como se aplica modulos aqui?
	return c1, c2

def elgamal_decrypt(c1, c2, b, p):
	s = pow(c1, b, p)
	q, m = divmod(c2 * gmpy.invert(s, p), p)
	return m

# Generando el primo 
lowest_range =  1000
highest_range = 9999

# Se generan semillas en un rango para ingresar a la función generadora de primos
# p_seed = random.randint(lowest_range, highest_range)
# p = sympy.nextprime(p_seed)
p = 5479
print("El primo selecionado es: ", p)

	 
# Seleccionando el generador
# g = random.randint(2, p - 2)
g = 1641
print("El generador es: ", g)

# Seleccionando b
# b = random.randint(2, p - 2)
b = 3875
print("b es: ", b)

be = elgamal_key_generator(g, b, p)

print("Public key: ", be)
print("Private key: ", b)

r = 123456
m = 2250

print('Mensaje para Alberto Miranda')
print("r: ", r)
print("m: ", m)

print('Datos de Alberto Miranda')
print('be: ', 5738)
print('p: ', 4547)
print('g:', 5)

print('Encriptando mensaje para Alberto Miranda: ', elgamal_encrypt(m, 5738, r, 5, 4547))
print('Desencriptando mensaje de Pablo Ruiz Encinas: ', elgamal_decrypt(46050, 86650, b, p))