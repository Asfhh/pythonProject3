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

