import re
string = 'Mi música es el Heavy Metal'
print (re.findall('Mi música',string)) # Nos busca todas las veces que se repite
print (re.search('Mi música', string)) # Nos busca solo la primera vez que aparece

