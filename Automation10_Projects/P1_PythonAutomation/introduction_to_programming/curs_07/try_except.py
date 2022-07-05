# exceptie = o eroare in Python, ceva ce nu poate sa faca codul si opreste executia
# se trateaza prin try except

try: #in try punem codul despre care presupunem ca ar putea genera o execptie
    number = 0
    number2 = 10/number
except Exception as e: #in except tratam orice exceptie (salvam mesajul ei in variabila e)
    print(f'Error: {e}')
#
# print('ajung aici')

# try: # in try punem codul 'periculos'
#     lista = [1, 2, 3]
#     lista[6]
# except IndexError as e: #tratam IndexError exception
#     print(e)
#
# print('am ajuns aici') # fiindca am prins exceptia, codul merge mai departe

# fortezi o exceptie
# raise IndexError('Limita elevilor din clasa este 30')