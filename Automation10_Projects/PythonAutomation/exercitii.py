pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000}
accesibil = 15000
for key, value in pret_masini.items():
    if value <= accesibil:
        print(f'Masina pe care ti-o permiti este {key}')