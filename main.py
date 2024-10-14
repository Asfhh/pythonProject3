#
#
# arr = [1, 5, 10]
# # sum = 0
# # count = 0
# # for i in arr:
# #     count += 1
# #     sum += i
# #     print(sum / count)
#
# # arr2 = [9, 10, 55, 421, 1563, 12.1]
# # def avg(arr):
# #     sum = 0
# #     count = 0
# #     for i in arr:
# #         count += 1
# #         sum += i
# #     return sum / count
# # print(avg(arr))
# # print(avg(arr2))
# #         # print(sum / count)
# #
# # arr3 = [9, 10, 55, 421, 1563, 12.1,500]
# # print(avg(arr3))
#
#
# def sayHi(): # nieko negražina
#     print("Hi")
#
# sayHi()
# sayHi()
# sayHi()
# sayHi()
# print(sayHi())
#
# def simPi():
#     return 3.14 # gražina
# print(simPi())
#
# def sayHiTo(name):  # priima, bet nieko negražina
#     print(f'Hi {name}')  # Pataisytas kintamojo pavadinimas
#
# # Kvietimas funkcijos su skirtingais vardais
# sayHiTo("Jonas")
# sayHiTo("Vilna")
# vardas = "Petriukas"
# sayHiTo(vardas)
#
# def intSum(a, b):  # priima du skaičius a ir b
#     return a + b  # grąžina jų sumą
#
# result = intSum(16, 36)  # kviečiame funkciją su 16 ir 36
# print(result)  # atspausdiname rezultatą
#

# 
# def avg(arr):
#     sum = 0
#     count = 0
#     for i in arr:
#         count += 1
#         sum += i
#     return sum / count if count != 0 else 0
# 
# arr = [8, 9, 10, 7, 8, 9]
# 
# print("Ausros gimnazijos studento pažymių vidurkis yra: " + str(avg(arr)))
# 
# 
# 


# def makecoffee(type, temperature="hot"):
#     print(f'There u go, your {type} {temperature} coffee')
#
# makecoffee("black")
# makecoffee("Latte", temperature="cold")

# 1. Sukurkite funkciją, kuri išvestų jūsų vardą ir kodėl pasirinkote
# programavimą. Iškvieskite šią funkciją tris kartus.
# 2. Sukurkite funkciją, kuri išvestų 5 eilučių eilėraštį. Iškvieskite šią funkciją 5
# kartus.
# 3. Sukurkite tris funkcijas, kur kiekviena išvestų skirtingus tekstus. Iškvieskite
# visas tris funkcijas po vieną kartą.
# 4. Sukurkite dvi funkcijas, kur vienoje būtų viena teksto eilutėje, kitoje kita.
# Sukurkite trečią funkciją, kuri iškviestų pirmas dvi funkcijas. Iškvieskite šią
# trečiąją funkciją už visų funkcijų ribų.
# 5. Sukurkite funkciją, kurios viduje sugeneruotumėte du atsitiktinius
# skaičius. Funkcijoje suskaičiuokite ir išveskite šių dviejų skaičių sumą,
# kartu išvedant ir patį atliekamą veiksmą (pvz 7 + 2 = 9). Iškvieskite šią
# funkciją keletą kartų.
# 6. Sukurkite ir iškvieskite funkciją, kurioje kintamuosiuose būtų saugoma
# informacija apie policininką (vardas, pavardė, amžius, alga, etatas,
# specializacija). Išveskite šią informaciją suformatuotai (pavyzdžiui įterpkite
# į sakinį, ar išveskite sąrašu ar pan.).
# 7. Sukurkite funkciją, kuri išvestų 10 atsitiktinių skaičių. Po visų išvestų
# skaičių turėtų padėti tuščią eilutę. Šią funkciją iškvieskite 5 kartus.
# 8. Sukurkite funkciją, kuri išvestų atsitiktinį skaičių. Už funkcijos ribų
# sukurkite ciklą, kurį būtų vykdomas 10 kartų. Iškvieskite sukurtą funkciją
# cikle. Turėtumėte pamatyti 10 atsitiktinių skaičių.

#1

# def prisistatyk():
#     vardas = "Justas"  # Jūsų vardas
#     priezastis = " Ir aš pasirinkau programavima "
#     print(f"Mano vardas yra {vardas}. {priezastis}")
# prisistatyk()

#2

# def a_eilerastis():
#     eilerastis = """
#     Tupi žvirblis kamine,
#     Su kažkokia kepure,
#     That's it folks.
#     """
#     print(eilerastis)
# for _ in range(5):
#     a_eilerastis()

#3
#
# def pir_funkcija():
#     print("Uno")
# def antr_funkcija():
#     print("dos")
# def trec_funkcija():
#     print("tres")
#
# pir_funkcija()
# antr_funkcija()
# trec_funkcija()

#4
# Sukurkite dvi funkcijas
# kur vienoje būtų viena teksto eilutėje -   kitoje kita.
# Sukurkite trečią funkciją, kuri iškviestų pirmas dvi funkcijas.
# Iškvieskite šią trečiąją funkciją už visų funkcijų ribų.

# def pirma_f():
#     print("Pirma F")
# def antra_f():
#     print("Antra F")
# def iskviestos_f():
#     pirma_f()
#     antra_f()
# iskviestos_f()


#5
# Sukurkite funkciją, kurios viduje sugeneruotumėte du atsitiktinius
# skaičius.
#
# Funkcijoje suskaičiuokite ir išveskite šių dviejų skaičių sumą,
#
# kartu išvedant ir patį atliekamą veiksmą (pvz 7 + 2 = 9).
# Iškvieskite šią funkciją keletą kartų.


# import random
#
# def random_suma():
#     num1 = random.randint(1, 10)
#     num2 = random.randint(1, 10)
#     suma = num1 + num2
#     print(f'{num1} + {num2} = {suma}')
# random_suma()
# random_suma()


#6 Sukurkite ir iškvieskite funkciją,
# kurioje kintamuosiuose būtų saugoma informacija apie policininką
# (vardas, pavardė, amžius, alga, etatas, specializacija).
# Išveskite šią informaciją suformatuotai
# (pavyzdžiui įterpkite į sakinį, ar išveskite sąrašu ar pan.).

# def info_policinko():
#     vardas = "Saulius"
#     pavarde = "Skvernelis"
#     amžius = 55
#     alga = 800
#     etatas = "Pilnas"
#     specializacija = "patrulis"
#
#     print("-------------------------------------------")
#     print(f'|          Policininko aprašymas          |')
#     print("-------------------------------------------")
#     print(f'| Vardas:  {vardas}                        |')
#     print(f'| Pavarde: {pavarde}                     |')
#     print(f'| Amžius: {amžius}  metai                       |')
#     print(f'| Alga: {alga} europietiški                  |')
#     print(f'| Etatas: {etatas}                          |')
#     print(f'| Specializacija: {specializacija}                |')
#     print("-------------------------------------------")
# info_policinko()


#7
# Sukurkite funkciją,
# kuri išvestų 10 atsitiktinių skaičių.
# Po visų išvestų skaičių turėtų padėti tuščią eilutę.
# Šią funkciją iškvieskite 5 kartus.
#
# import random
#
# def random_number():
#     for _ in range(10):
#         print(random.randint(1, 10), end=' ')
#     print('\n')
#
# for _ in range(5):
#     random_number()

# 8\
#
# Sukurkite funkciją, kuri išvestų atsitiktinį skaičių.
# Už funkcijos ribų sukurkite ciklą, kurį būtų vykdomas 10 kartų.
# Iškvieskite sukurtą funkciją cikle.
# Turėtumėte pamatyti 10 atsitiktinių skaičių.

# import random
# def betkokie_sk():
#     return random.randint(1, 10)
# for _ in range(10):
#     print(betkokie_sk())

# # 9
# Sukurkite funkciją pasisveikinimui,
# šiai funkcijai per argumentus perduokite vardą,
# funkcijoje išveskite tekstą labas ir gautą vardą.
# Sukurkite kitą funkciją, kuri irgi per argumentus gautų vardą, tačiau
# pasakytų 'viso gero' ir patį vardą.
# Ne funkcijose susikurkite kintamąjį vardui saugoti ir įrašykite vardą.
# Iškvieskite abi funkcijas, perduodant kintamąjį joms.

# def pasveik(vardas):
#     print(f'Labas, {vardas}')
# def sudievu(vardas):
#     print(f'Iki, {vardas}')
# vardas = 'Saulius'
# pasveik(vardas)
# sudievu(vardas)

#10
# Sukurkite funkciją, kuriai perduotumėte du skaičius.
# Ši funkcija turi rasti kuris skaičius yra didesnis ir išvesti gautą atsakymą,
# o jei skaičiai lygūs - tuomet išvesti, kad skaičiai lygūs.
# Iškvieskite šią funkciją keletą kartų, duodant skirtingus skaičius.

# def du_sk(sk1, sk2):
#     if sk1 > sk2:
#         return f'{sk1} yra didesnis už {sk2}.'
#     elif sk1 < sk2:
#         return f'{sk2} yra didesnis už {sk1}.'
#     else:
#         return 'Skaičiai yra lygūs.'
# results = [
#         du_sk(5, 10),
#         du_sk(5, 20),
#         du_sk(45, 30),
#         du_sk(5, 40),
#         du_sk(5, 50),
#         du_sk(0, 0),
#         du_sk(100, 1),
#     ]
#
# for result in results:
#     print(result)

#11.Sukurkite funkciją, kuri per argumentus gautų automobilių duomenis
# (markė, modelis, gamybos metai, darbinis tūris).
# Ši funkcija turėtų šiuos duomenis išvesti kaip nors gražiai formatuotai.
# Iškvieskite šią funkciją du kartus, perduodant skirtingus duomenis jai.

# def auto_info(marke, modelis, metai, turis):
#     print(f'--- Automobilio duomenys ---')
#     print(f'Marke: {marke}')
#     print(f'Modelis: {modelis}')
#     print(f'Metai: {metai}')
#     print(f'Tūris: {turis}')
# auto_info('BMW', 'e46', 2003, 3)
# auto_info(' Toyota', 'Prius', 2003, 2)

#12. Sukurkite funkciją sumai skaičiuoti,
# ši funkcija per argumentus turėtų gauti du skaičius,
# bei išvesti patį veiksmą kartu su atsakymu (pvz 7 + 5 =12).
# Sukurkite tokias pačias funkcijas skirtumui, sandaugai ir dalmeniui rasti.
# Sukurkite dar vieną funkciją, kuri sugeneruotų du atsitiktinius skaičius,
# bei iškviestų kitas 4 funkcijas, perduodant joms sugeneruotus skaičius.
# Šią bendrąją funkciją iškvieskite keletą kartų.

# import random
#
#
# def sk_suma(a, b):
#     result = a + b
#     print(f'{a} + {b} = {result}')
#
#
# def sk_skirtumas(a, b):
#     result = a - b
#     print(f'{a} - {b} = {result}')
#
#
# def sk_sandauga(a, b):
#     result = a * b
#     print(f'{a} * {b} = {result}')
#
#
# def sk_dalmuo(a, b):
#     if b != 0:
#         result = a / b
#         print(f'{a} / {b} = {result}')  #
#     else:
#         print('Dalyba iš 0 negalima')
#
#
# def atlikimas():
#     sk1 = random.randint(1, 100)
#     sk2 = random.randint(1, 100)
#     print(f'\nSugeneruoti skaičiai: {sk1} ir {sk2}\n')
#
#     sk_suma(sk1, sk2)
#     sk_skirtumas(sk1, sk2)
#     sk_sandauga(sk1, sk2)
#     sk_dalmuo(sk1, sk2)
#
# atlikimas()
# atlikimas()
# atlikimas()

#13. Susikurkite funkciją, kuri per argumentus priimtų žodžių masyvą.
# Funkcijoje išveskite visus žodžius iš masyvo atskirose
# (eilutėse nurodant) žodžio ilgį (simbolių kiekį).
# Už funkcijos ribų susikurkite žodžių masyvą ir užpildykite jį duomenimis.
# Iškvieskite sukurtą funkciją perduodant turimą masyvą.

# def zodziu_masyvas(zodziai):
#     for zodziai in zodziai:
#         ilgis = len(zodziai)a
#         print(f'Žodis {zodziai}, ilgis:  {ilgis}')
# zodziu_sarasas =  ["keptuve", "koja", "kriauklė", "bulve", "slyva"]
#
# zodziu_masyvas(zodziai=zodziu_sarasas)

#14. Susikurkite funkciją,
# kuri per argumentus priimtų skaičių masyvą.
# Funkcija turėtų atspausdinti visus skaičius,
# šalia jų išvedant to skaičiaus kvadratą ir jį padalintą iš dviejų.
# Už funkcijos ribų susikurkite du skaičių masyvus ir užpildykite jį duomenimis.
# Iškvieskite funkciją du kartus, kiekvieną kartą perduodant skirtingą turimą masyvą.

# def skaic(masyvas):
#     for skaiciai in masyvas:
#         kvadratas = skaiciai ** 2
#         dalyba = skaiciai / 2
#         print(f'Skaičius: {skaiciai}, Kvadratas: {kvadratas}, Dalyba iš dviejų: {dalyba}')
#
# masyvas1 = [1, 2, 3, 4, 5, 6]
# masyvas2 = [11, 2, 8, 4, 5, 7]
#
# skaic(masyvas1)
# print()
# skaic(masyvas2)

#15.Susikurkite funkciją, kuri per argumentus priimtų pažymių masyvą,
# bei studento vardą su pavarde.
# Funkcija turėtų išvesti studento vardą ir pavardę, jo pažymius.
# Taip pat, suskaičiuoti vidurkį, bei jį išvesti.
# Už funkcijos ribų susikurkite reikiamus kintamuosius ir masyvus, arba
# objektus studentų pažymiams saugoti ir užpildykite juos duomenimis.
# Iškvieskite šią funkciją perduodant visus reikalingus duomenis.

# def masyvas(vardas, pavarde, pazymiai):
#     print(f'Studento vardas: {vardas} {pavarde} ')
#     print(f'Pažymiai:  {pazymiai}')
#     vidurkis = sum(pazymiai) / len(pazymiai) if pazymiai else 0
#     print(f'Vidurkis: {vidurkis}')
# vardas1 = 'Justas'
# pavarde1 = 'Jonaitis'
# pazymiai1 = [10, 10, 8, 4, 10]
#
# vardas2 = 'Jonas'
# pavarde2 = 'Justaitis'
# pazymiai2 = [3, 10, 10, 9, 10]
#
# masyvas(vardas1, pavarde1, pazymiai1)
# masyvas(vardas2, pavarde2, pazymiai2)


#16.Susikurkite funkciją,
# kuri per argumentus priimtų skaičių masyvą.
# Funkcija turėtų rasti didžiausią skaičių iš masyvo
# bei išvesti gautą atsakymus.
# Taip pat, susikurkite funkciją,
# kuri per argumentus priimtų masyvą ir į jį sugeneruotų pasirinktą kiekį atsitiktinių skaičių. Susikurkite tris tuščius
# masyvus.
# Iškvieskite atsitiktinių skaičių generavimo funkciją tris kartus,
# kiekvieną kartą perduodant funkcijai vis kitą masyvą.
# Kai duomenys bus užpildyti, masyvuose esančią informaciją
# išsiveskite norimu būdu (per console.log arba per dar atskirą funkciją).
# Tuomet kvieskite didžiausio skaičiaus paieškos funkciją tris kartus, kiekvieną kartą perduodant
# skirtingą masyvą į ją.

# import random
#
# def rasti_didziausi(masyvas):
#     didziausias = max(masyvas)
#     print(f'Didžiausias skaičius: {didziausias}')
#
# def random_skaiciai(masyvas, kiekis):
#     for _ in range(kiekis):
#         rand_skaicius = random.randint(1, 100)
#         masyvas.append(rand_skaicius)
#
# masyvas1 = []
# masyvas2 = []
# masyvas3 = []
#
# random_skaiciai(masyvas1, 10)
# random_skaiciai(masyvas2, 10)
# random_skaiciai(masyvas3, 10)
#
# print('Masyvas 1:', masyvas1)
# print('Masyvas 2:', masyvas2)
# print('Masyvas 3:', masyvas3)
#
# rasti_didziausi(masyvas1)
# rasti_didziausi(masyvas2)
# rasti_didziausi(masyvas3)

# 17..Susikurkite funkciją,
# kuri grąžintų bet kokį jūsų norimą sakinį.
# Iškvieskite šią funkciją ir išspausdinkite gautus rezultatus.

# def norim_sakin():
#     return "Geras sakinys"
# sakinys = norim_sakin()
# print(sakinys)

#18. Susikurkite funkciją,
# kuri grąžintų atsitiktinai sugeneruotą skaičių.
# Iškvieskite šią funkciją kelis kartus ir
# gautus atsakymus išveskite kokiu norite būdu.

# import random
#
# def skaiciai():
#     return random.randint(1, 25)
#
# skaicius1 = skaiciai()
# skaicius2 = skaiciai()
# skaicius3 = skaiciai()
#
# print(f'Atsitiktinis skaičius: {skaicius1}')
# print(f'Atsitiktinis skaičius: {skaicius2}')
# print(f'Atsitiktinis skaičius: {skaicius3}')


# 19.Susikurkite funkciją, kuri per argumentus priimtų studento vardą ir
# vidurkį.
# Ši funkcija turėtų sugeneruoti iš to sakinį (pvz Studentas Tomas
# turi vidurkį 8.7) ir tai grąžinti kaip atsakymą.
# Iškvieskite šią funkciją bent porą kartų,
# perduodant vis skirtingus duomenis. Gautus atsakymus išveskite.

# def studento_info(vardas, vidurkis):
#     return f'Studentas {vardas} turi vidurkį {vidurkis}'
#
# tekstas1 = studento_info('Justas', '10')
# tekstas2 = studento_info('Rugilė', '9.5')
#
# print(tekstas1)
# print(tekstas2)

# 20.Susikurkite funkciją, kuri per argumentus gautų skaičių.
# Ji turėtų surasti duoto skaičiaus mažiausią daliklį
# (skaičių iš kurio dalinasi be liekanos).
# Už funkcijos ribų sukite ciklą nuo 10 iki 30
# ir kiekvienoje ciklo iteracijoje iškvieskite šią funkciją, perduodant ciklo kintamąjį.

# def maziausias_daliklis(skaicius):
#     for i in range(2, skaicius + 1):
#         if skaicius % i == 0:
#             return i
# for skaicius in range(10, 31):
#     daliklis = maziausias_daliklis(skaicius)
#     print(f'Skaičius {skaicius} mažiausias daliklis yra {daliklis}')

# 21.Susikurkite funkciją,
# kuri per argumentus gautų skaičių.
# Ji turėtų patikrinti ar šis skaičius yra pirminis
# (grąžina True jei pirminis, ir False jei ne  pirminis).
# Už funkcijos ribų sukite ciklą nuo 2 iki 15, kiekvienoje ciklo
# iteracijoje išveskite tikrinamą skaičių ir šalia jo iškviestos funkcijos
# atsakymą (pvz 10 false, 11 true, ...).

# def pirminis(skaicius):
#     if skaicius < 2:
#         return False
#     for i in range(2, int(skaicius ** 0.5) + 1):
#         if skaicius % i == 0:
#             return False
#     return True
#
# for skaicius in range(2, 16):
#     rezultatas = pirminis(skaicius)
#     print(f'{skaicius}: {rezultatas}')

# 22.Susikurkite bent 3 matematines funkcijas,
# priimančias reikiamus argumentus
# (pvz suma iš dviejų skaičių, suma iš trijų skaičių, skirtumas,
# sandauga, dalyba)
# ir grąžinančias atitinkamus atsakymus.
# Taip pat, susikurkite funkciją,
# kurioje būtų sugeneruojamas reikiamas kiekis atsitiktinių skaičių
# ir išvedami visų skaičiavimų atsakymai su veiksmais
# (iškviečiant atitinkamas kitas funkcijas ir perduodant reikiamus
# kintamuosius) (pagal 23 pavyzdį). Iškvieskite šią pagrindinę funkciją bent
# kartą.

# import random
# def suma_du(a, b):
#     return a + b
#
# def suma_trys(a, b, c):
#     return a + b + c
#
# def skirtumas(a, b):
#     return a - b
#
# def sandauga(a, b):
#     return a * b
#
# def dalyba(a, b):
#     if b != 0:
#         return a / b
#     else:
#         return 'Negalima dalinti iš 0 :)'

# def skaiciavimas():
#     skaic1 = random.randint(1, 20)
#     skaic2 = random.randint(1, 20)
#     skaic3 = random.randint(1, 20)
#
#     print(f'Skaičiai: {skaic1}, {skaic2}, {skaic3}')
#     print(f"Suma (du): {skaic1} + {skaic2} = {suma_du(skaic1, skaic2)}")
#     print(f"Suma (trys): {skaic1} + {skaic2} + {skaic3} = {suma_trys(skaic1, skaic2, skaic3)}")
#     print(f"Skirtumas: {skaic1} - {skaic2} = {skirtumas(skaic1, skaic2)}")
#     print(f"Sandauga: {skaic1} * {skaic2} = {sandauga(skaic1, skaic2)}")
#     print(f"Dalyba: {skaic1} / {skaic2} = {dalyba(skaic1, skaic2)}")
# skaiciavimas()

#23.Susikurkite funkciją kuri priimtų skaičių masyvą per argumentus.
#Ši funkcija turėtų rasti duotųjų skaičių sumą ir grąžinti gautą atsakymą.
# Už funkcijos ribų susikurkite du skaičių masyvus ir užpildykite juos
# duomenimis.
# Iškvieskite turimą funkciją du kartus, jai abu kartus
# perduodant skirtingą masyvą.
# Gautus atsakymus išveskite. Taip pat, raskite kuri suma gavosi didesnė ir išveskite atsakymą.

# def suma_masyvo(masyvas):
#     return sum(masyvas)
# masyvas1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 96]
# masyvas2 = [5, 12, 52, 15, 31, 21, 5]
#
# suma1 = suma_masyvo(masyvas1)
# suma2 = suma_masyvo(masyvas2)
# print(f' 1. Suma: {suma1}')
# print(f' 2. Suma: {suma2}')
#
# if suma1 > suma2:
#     print(f' Pirmoji masyvo suma {suma1} yra didesnė už masyvo 2 sumą {suma2}')
# elif suma2 > suma1:
#     print(f' Antroji masyvo suma  {suma2} yra didesnė už masyvo 1 sumą {suma1}')
# else:
#     print(f'Šios sumos yra vienodos: {suma1}')


# 24.Susikurkite funkciją kuri per argumentus priimtų žodžių masyvą.
# Ji turėtų rasti ir grąžinti ilgiausią žodį masyve.
# Už funkcijos ribų susikurkite žodžių masyvą.
# Iškvieskite funkciją perduodant jai žodžių masyvą.
# Gautą atsakymą išveskite, taip pat, nurodykite šio žodžio ilgį.

# def pirm_masyvas(tekstas):
# #     tekstukas = ""
# #     for zodis in tekstas:
# #         if len(zodis) > len(tekstukas):
# #             tekstukas = zodis
# #     return tekstukas
# #
# # antras_masyvas = ["naktis", "rytojus", "aušra", "mėnulis", "batas"]
# # tekstukas = pirm_masyvas(antras_masyvas)
# #
# # print(f'Ilgiausias žodis: {tekstukas}')
# # print(f'Simbolių skaičius: {len(tekstukas)}')

#25. Susikurkite funkciją kuri per argumentus priimtų pažymių masyvą.
# Ji turėtų patikrinti ar visi pažymiai teigiami:
# jei visi teigiami turėtų grąžintų True kaip atsakymą,
# o jei yra bent vienas neigiamas - False.
# Susikurkite du pažymių masyvus.
# Iškvieskite šią funkciją du kartus, abu kartus
# perduodant skirtingus masyvus.
# Gautus atsakymus paverskite į tekstą
# (jeigu gavote True - išveskite tekstą 'visi studento pažymiai teigiami', jei
# False - 'studentas turi bent vieną neigiamą pažymį'). Šiam iškonvertavimui
# iš True/False į tekstą galite pamėginti pasikurti atskirą funkciją, jai
# perduoti kitos funkcijos atsakymą.

# def teigiami_pazym(pazymiai):
#     neigiami_pazymiai = sum(1 for paz in pazymiai if paz <= 3)
#     return neigiami_pazymiai == 0
#
# def tekstas(rezultatas):
#     if rezultatas:
#         return 'Visi studento pažymiai teigiami'
#     else:
#         return 'Studentas turi bent vieną neigiamą pažymį'
#
# pazymiai1 = [8, 10, 2, 5]
# pazymiai2 = [5, 5, 10, 5, 7]
#
# rezultatas1 = teigiami_pazym(pazymiai1)
# rezultatas2 = teigiami_pazym(pazymiai2)
#
# print(tekstas(rezultatas1))
# print(tekstas(rezultatas2))

#26.Pabandykite parašyti bent dvi pasirinktas funkcijas,
# kuriose būtų naudojami default parametrai.
# Iškvieskite šias funkcijas įvairiais būdais (perduodant visus argumentus, bei neperduodant tų kuriuos galima
# praleisti (turinčius default reikšmes)).

#                                   Funkcijos

#1 Sukurkite Funkciją kuri priima du int tipo kintamuosius. Juos susumuoja ir atspausdina
# def suma(a: int, b: int):
#     rez = a + b
#     print(f'Suma: {rez}')
#
# suma(2, 10)
# suma(4, 7)

#2. Sukurkite Funkciją kuri vadinasi PISq. Funkcija gražina float tipo reikšmę. Reikšmė yra : 9.8596; Gautą reikšmę atspausdinkite.

# def PISq() -> float:
#     return 9.8596
#
# result = PISq()
# print(f'Reiškmė: {result}')

#3. Sukurkite Funkciją kuri priima du int tipo kintamuosius.
# Funkcija gražina skaičių sandaugą.;
# Gautą reikšmę atspausdinkite.

# def sandauga(a: int, b: int) -> int:
#     return a * b
# rezultatas = sandauga(2, 10)
# print(f' Gautas rezultatas: {rezultatas}')

#4. Sukurkite Funkciją kuri priima masyvą,
# prasuka ciklą ir atspausdina kiekvieną narį vienoje eilutėje.

# def funkcija(masyvas):
#     for ciklas in masyvas:
#         print(ciklas)
# inf_masyv = 'Kiskis, upė, ir vaikai'
# funkcija(inf_masyv)

# 5. Sukurkite Funkciją kuri priima du int tipo kintamuosius,
# min ir max reikšmėms nustatyti ir
# sugeneruoja random int skaičių ir jį gražintų.

# import random
# def masyvas(min_r: int, max_r: int) -> int:
#     return random.randint(min_r, max_r)
# min_r = 1
# max_r = 10
# random_sk = masyvas(min_r, max_r)
# print(f'Min: {min_r}, Max: {max_r}, Atsitiktinis skaičius: {random_sk}')

# 6. Sukurkite Funkciją kuri sugeneruotų random int skaičių masyvą
# ir jį gražintų.
# Funkcija priima tris int tipo kintamuosius,
# min, max ir length reikšmėms nustatyti.

# import random
# def masyvas(min_r: int, max_r: int, length_r: int):
#     return [random.randint(min_r, max_r) for _ in range(length_r)]
# min_R = 5
# max_R = 24
# length_R = 5
# random_skaiciai = masyvas(min_R, max_R, length_R)
# print(f'Atsitiktiniai skaičiai: {random_skaiciai}')

# 7.Sukurkite Funkciją kuri panaudotų 6toje užduotyje sugeneruotą masyvą
# (priimtų kaip kintamąjį), susumuotų ir gražintų reikšmę.
# import random
# def masyvas(min_r: int, max_r: int, length_r: int):
#     return [random.randint(min_r, max_r) for _ in range(length_r)]
# def suma(skaicai):
#     return sum(skaicai)
# min_r = 5
# max_r = 24
# length_r = 2
#
# random_skaiciai = masyvas(min_r, max_r, length_r)
# print(f'Atsitiktiniai skaičiai: {random_skaiciai}')
#
# r_suma = suma(random_skaiciai)
# print(f'Atsitiktinių skaičių suma:  {r_suma}')

#8.Sukurkite Funkciją kuri priimtų 6toje užduotyje sugeneruotą masyvą
# ir gražintų jos skaičių vidurkį (double).

# import random
#
# def masyvas(min_r: int, max_r: int, length_r: int):
#     return [random.randint(min_r, max_r) for _ in range(length_r)]
#
# def suma(skaicai):
#     return sum(skaicai)
#
# def vidurkis(skaiciai):
#     if len(skaiciai) == 0:
#         return 0
#     return suma(skaiciai) / len(skaiciai)
#
# min_r = 5
# max_r = 24
# length_r = 2
#
# random_skaiciai = masyvas(min_r, max_r, length_r)
# print(f'Atsitiktiniai skaičiai: {random_skaiciai}')
# r_suma = suma(random_skaiciai)
# print(f'Atsitiktinių skaičių suma: {r_suma}')
# r_vidurkis = vidurkis(random_skaiciai)
# print(f'Vidurkis: {r_vidurkis}')

# 9. Sukurkite Funkciją kuri priimtų du int skaičius
# ir atspausdintų stačiakampį užpildytą žvaigždutėmis.
# Pirmas int - išoriniam ciklui, antras vidiniam.

# def staciakamp(aukstis: int, plotis: int):
#     for _ in range(aukstis):
#         print('*' * plotis)
# aukstis = 2
# plotis = 10
# staciakamp(aukstis, plotis)

#10. Sukurkite Funkciją kuri priimtų sakinį kaip kintamąjį
# ir atspausdintų kiek jame yra raidžių(simbolių) ir tarpų.
# Sakinys - “Šiandien labai graži diena”. (kodas turi veikti padavus bet kokį sakinį)

# def sakin(sakinys: str):
#     raides = len(sakinys.replace(" ", ""))
#     tarpai = sakinys.count(" ")
#     print(f'Radžių skaičius: {raides}')
#     print(f'Tarpu kiekis: {tarpai}')
# sakinys = "Šiandien labai graži diena"
# sakin(sakinys)

#11. Sukurkite Funkciją
# kuri priimtų sakinį, jį užkoduotų ir grąžintų.
# Kodavimas - sakinį apsukame iš kitos pusės.
# Pvz “Naglis” turi gautis “silgaN”.
# def uzk_sakinys(sakinys):
#     return sakinys[::-1]
# uzk = uzk_sakinys('Vaflis')
# print(uzk)
#                       sunkesni
# 1. Parašykite funkciją, kurios argumentas būtų tekstas,
# kuris būtų atspausdinamas konsolėje pridedant “---” pradžioje ir gale.
# PVZ (---labas---)

# def tekstas(tekstas: str):
#     print(f'---{tekstas}---')
# tekstas('Labas')

# 2. Sugeneruokite atsitiktinį stringą iš raidžių ir skaičių (10 simbolių)
# Atspausdinkite simbolius stulpeliu.
# Jei tai skaičius apgaubkite “ [ 7 ]”.
# Jei skaičiai eina keli iš eilės, apgaubkite juos kartu. [75].
#
# import random
# import string
#
#
# def sugen_stringai(ilgis: int):
#     raides = string.ascii_letters
#     skaiciai = string.digits
#     simboliai = raides + skaiciai
#     return ''.join(random.choice(simboliai) for _ in range(ilgis))
#
#
# def spausdint_simbolius(simbol):
#     i = 0
#     skaiciai = ''
#     while i < len(simbol):
#         if simbol[i].isdigit():
#             skaiciai += simbol[i]
#         else:
#             if skaiciai:
#                 print(f'[{skaiciai}]')
#                 skaiciai = ''
#             print(f'[{simbol[i]}]')
#         i += 1
#
#     if skaiciai:
#         print(f'[{skaiciai}]')
#
#
# random_string = sugen_stringai(10)
# print('Sugeneruotas stringas:', random_string)
# spausdint_simbolius(random_string)

# 3.Parašykite funkciją,
# kuri skaičiuotų, ir gražintų iš kiek sveikų skaičių
# jos argumentas dalijasi be liekanos (išskyrus vienetą ir patį save).

# def  dalyba(n):
#     dalintojai = 0
#     for i in range(2, n):
#         if n % i == 0:
#             dalintojai += 1
#     return dalintojai
# print(dalyba(16))

# 4. Sugeneruokite masyvą iš 100 elementų,
# kurio reikšmės atsitiktiniai skaičiai nuo 33 iki 77.
# Išrūšiuokite masyvą pagal daliklių be liekanos kiekį mažėjimo tvarka,
# # panaudodami trečio uždavinio funkciją.
# import random
# def dalyba(n):
#     dalintojai = 0
#     for i in range(2, n):
#         if n % i == 0:
#             dalintojai += 1
#     return dalintojai
# masyvas = [random.randint(33, 77) for _ in range(100)]
# masyvas.sort(reverse=True)
# print(masyvas)

# 5.Sugeneruokite masyvą iš 100 elementų,
# kurio reikšmės atsitiktiniai skaičiai nuo 333 iki 777.
# Naudodami 3 uždavinio funkciją iš masyvo suskaičiuokite
# kiek yra pirminių skaičių.
# import random
# masyvas = [random.randint(333, 777) for _ in range(100)]
# def pirminis(skaicius):
#     if skaicius < 2:
#         return False
#     for i in range(2, int(skaicius**0.5) +1):
#         return False
#     return True
# kiekis = sum(1 for skaicius in masyvas if pirminis(skaicius))
# print(f'Pirminiai skaičiai masyve: {kiekis}')

#8. Sugeneruokite masyvą iš trijų elementų,
# kurie yra atsitiktiniai skaičiai nuo 1 iki 33.
# Jeigu tarp trijų paskutinių elementų yra nors vienas ne pirminis skaičius,
# prie masyvo pridėkite dar vieną elementą- atsitiktinį skaičių nuo 1 iki 33.
# Vėl patikrinkite pradinę sąlygą ir jeigu reikia pridėkite dar vieną elementą.
# Kartokite, kol sąlyga nereikalaus pridėti elemento.

# import random
#
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# atsitiktiniai = [random.randint(1, 33) for _ in range(3)]
# while True:
#     paskutiniai_sk = atsitiktiniai[-3:]
#     if any(not is_prime(num) for num in paskutiniai_sk):
#         atsitiktiniai.append(random.randint(1,33))
#     else:
#         break
# print(atsitiktiniai)

# Sugeneruokite masyvą iš 10 elementų,
# kurie yra masyvai iš 10 elementų,
# kurie yra atsitiktiniai skaičiai nuo 1 iki 100.
# Jeigu tokio didelio masyvo (ne atskirai mažesnių)
# pirminių skaičių vidurkis mažesnis už 70,
# suraskite masyve mažiausią skaičių (nebūtinai pirminį) ir prie jo pridėkite 3.
# Vėl paskaičiuokite masyvo pirminių skaičių vidurkį
# ir jeigu mažesnis nei 70 viską kartokite.
# import random
# def yra_pirminis(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# masyvas = [[random.randint(1, 100) for _ in range(10)] for _ in range(10)]
# def pirminiai_vidurkis(masyvas):
#     pirminiai = [num for row in masyvas for num in row if yra_pirminis(num)]  # Pridėta 'if'
#     return sum(pirminiai) / len(pirminiai) if pirminiai else 0
# while True:
#     vidurkis = pirminiai_vidurkis(masyvas)
#     if vidurkis >= 70:
#         break
#     maziausias = min(num for row in masyvas for num in row)
#     for i in range(len(masyvas)):
#         for j in range(len(masyvas[i])):
#             if masyvas[i][j] == maziausias:
#                 masyvas[i][j] += 3
#                 break
# print("Galutinis masyvas:")
# for row in masyvas:
#     print(row)
# print("Pirminių skaičių vidurkis:", vidurkis)


import random

def generateRndStr(length):
    symbols = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890!#*.,"
    text = ""
    for i in range(length):
        text += symbols[random.randint(0, len(symbols) - 1)]
    return text

def issaugoti_pass(slaptazodis):
    with open('slaptazodis.txt', 'a') as file:
        file.write(slaptazodis + '\n')

def read_passwords():
    try:
        with open('slaptazodis.txt', 'r') as file:
            passwords = file.readlines()
            print("Išsaugoti slaptažodžiai:")
            for password in passwords:
                print(password.strip())
    except FileNotFoundError:
        print("Failas 'slaptazodis.txt' dar neegzistuoja.")

def main():
    while True:
        random_string = generateRndStr(12)
        print(f'Siūlomas slaptažodis: {random_string}')

        atsakymas = input('Ar slaptažodis Jums patinka? (taip/ne): ').strip().lower()
        if atsakymas == 'taip':
            issaugoti_pass(random_string)
            print('Slaptažodis išsaugotas!')
            break
        elif atsakymas == 'ne':
            print('Generuojamas naujas slaptažodis...')
        else:
            print('Prašome įvesti "taip" arba "ne".')

if __name__ == '__main__':
    main()
    read_passwords()
