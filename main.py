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


def makecoffee(type, temperature="hot"):
    print(f'There u go, your {type} {temperature} coffee')

makecoffee("black")
makecoffee("Latte", temperature="cold")
