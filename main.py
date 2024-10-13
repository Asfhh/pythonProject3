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

