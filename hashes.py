#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Prueba de concepto de Hashes Criptográficos en Python
# 
# Importamos la librería criptográfica de Hashes
import hashlib
# 
print "Algoritmos Disponibles:"
print hashlib.algorithms  # Lista de algoritmos disponibles
#
# cadena = input('Introduce una cadena que Hashear: ')
# 
chain = raw_input("Introduce una cadena: ")
# Codificamos como UTF-8
chain_enc = chain.encode('UTF-8')
hash_object_md5 = hashlib.md5(chain_enc)
print "Cadena inicial: "+chain
print "================================================================================================================="
#print "MD5 :    "+hash_object_md5.digest()
print "MD5 (hex):    "+hash_object_md5.hexdigest()
print "================================================================================================================="
#
# Creamos el Hash con SHA1 para la misma cadena
hash_object_sha1 = hashlib.sha1(chain_enc)
#print "SHA1 :   "+hash_object_sha1.digest() 
print "SHA1 (hex):   "+hash_object_sha1.hexdigest()
print "================================================================================================================="
#
# Creamos el Hash con SHA224 para la misma cadena
hash_object_sha224 = hashlib.sha224(chain_enc)
#print "SHA224 : "+hash_object_sha224.digest()
print "SHA224 (hex): "+hash_object_sha224.hexdigest()
print "================================================================================================================="
#
# Creamos el Hash con SHA256 para la misma cadena
hash_object_sha256 = hashlib.sha256(chain_enc)
#print "SHA256 : "+hash_object_sha256.digest()
print "SHA256 (hex): "+hash_object_sha256.hexdigest()
print "================================================================================================================="
#
# Creamos el Hash con SHA384 para la misma cadena
hash_object_sha384 = hashlib.sha384(chain_enc)
#print "SHA384 : "+hash_object_sha384.digest()
print "SHA384 (hex): "+hash_object_sha384.hexdigest()
print "================================================================================================================="
#
# Creamos el Hash con SHA512 para la misma cadena
hash_object_sha512 = hashlib.sha512(chain_enc)
#print "SHA512 : "+hash_object_sha512.digest()
print "SHA512 (hex): "+hash_object_sha512.hexdigest()
print "================================================================================================================="
