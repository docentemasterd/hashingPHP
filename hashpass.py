#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import uuid
import hashlib
 
def hash_password(password):
    # uuid se usa para generar numeros aleatorios
    salt = uuid.uuid4().hex
    # Salteamos la pass
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt  
    
def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
 
init_pass = raw_input('Introduzca contraseña: ')
new_pass = init_pass.encode('UTF-8') # Cambiando utf-8 por hex obtenemos otro hash más seguro
hashed_password = hash_password(new_pass)
print('La cadena a almacenar en la DB es: ' + hashed_password)
sec_pass = raw_input('Introduzca de nuevo la contraseña: ')
old_pass = sec_pass.encode('UTF-8')
if check_password(hashed_password, old_pass):
    print('Contraseña correcta!!')
else:
    print('Las contraseñas no coinciden.')