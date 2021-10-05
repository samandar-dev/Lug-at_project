# -------------------------------Lug'at--------------------------------


# import mysql.connector
# import os
#
# my_db = mysql.connector.connect(
#       host="localhost",
#       user="Samandar",
#       passwd="samandar",
#       database="Jadval"
# )
#
# mycursor = my_db.cursor()
#
# class Logat:
#       def __init__(self):
#             pass
#
#       def yangi_soz_qoshish(self):
#             n = input("1-chi o'zbekchasini kiriting: >>>>").strip().capitalize()
#             nn = input("2-chi inglizchasini kiriting: >>>>").strip().capitalize()
#
#             while not n.isalpha() or not nn.isalpha():
#                   os.system("clear")
#                   print("Xarifdan iborat str kiriting: ")
#                   n = input("1-chi o'zbekchasini kiriting: >>>>").strip().capitalize()
#                   nn = input("2-chi inglizchasini kiriting: >>>>").strip().capitalize()
#
#             # bor_ozb = f"select uzbekcha from Lugat where uzbekcha='{n}'"
#             bor_ing = f"select inglizcha from Lugat where inglizcha='{nn}'"
#
#             # mycursor.execute(bor_ozb)
#             # bor_ozb = mycursor.fetchall()
#
#             mycursor.execute(bor_ing)
#             bor_ing = mycursor.fetchall()
#
#             if bor_ing:
#                   print("Bunday sozlar bor: ")
#                   self.pri()
#
#             mycursor.execute(f"insert into Lugat (uzbekcha, inglizcha) values ('{n}', '{nn}')")
#             my_db.commit()
#
#             print("-----Yangi so'z qoshildi-----\n")
#             self.pri()
#
#       def lugatni_ichini_korish(self):
#             logat = f"select uzbekcha, inglizcha from Lugat"
#             mycursor.execute(logat)
#             all = mycursor.fetchall()
#
#             for i in all:
#                   print(i)
#             self.pri()
#
#       def izlash(self):
#             son = ['1', '2']
#             print("""
#                   1. o'zbekcha
#                   2. inglizcha
#
#                   """)
#             n = input(">>>>>").strip()
#             while n not in son:
#                   n = input("Xato >>>>>").strip()
#
#             while n in son[0]:
#                   n = input("Sozni kiriting: >>> ").strip().capitalize()
#                   logat_ozb = f"select uzbekcha, inglizcha from Lugat where uzbekcha='{n}'"
#                   mycursor.execute(logat_ozb)
#                   all = mycursor.fetchall()
#
#                   if all:
#                         logat_ozb = f"select uzbekcha, inglizcha from Lugat where uzbekcha='{n}'"
#                         mycursor.execute(logat_ozb)
#                         all = mycursor.fetchall()
#
#                         for i in all:
#                               os.system("clear")
#                               print(f"\n\t\t--------{i}-------")
#                         self.pri()
#                   else:
#                         print("\tBunday soz yo'q: ")
#                         self.pri()
#
#             while n in son[1]:
#                   n = input("Sozni kiriting: >>> ").strip().capitalize()
#                   logat_ozb = f"select uzbekcha, inglizcha from Lugat where inglizcha='{n}'"
#                   mycursor.execute(logat_ozb)
#                   all = mycursor.fetchall()
#
#                   if all:
#                         logat_ozb = f"select uzbekcha, inglizcha from Lugat where inglizcha='{n}'"
#                         mycursor.execute(logat_ozb)
#                         all = mycursor.fetchall()
#
#                         for i in all:
#                               os.system("clear")
#                               print(f"\n\t\t---------{i}--------")
#                         self.pri()
#                   else:
#                         print("\tBunday soz yo'q: ")
#                         self.pri()
#
#       def chiqish(self):
#             print("\n---------------------Xayr------------------------")
#             exit()
#
#
#       def pri(self):
#             sonlar = ['1', '2', '3', '4']
#             while True:
#                   print("""
#
#                         1. Yangi so'z qo'shish
#                         2. Lug'at ichidagi so'zlarni ko'rish
#                         3. Izlash
#                         4. Lug'atdan chiqish
#
#                   """)
#
#                   n = input(">>>").strip()
#                   if n == sonlar[0]:
#                         self.yangi_soz_qoshish()
#                   elif n == sonlar[1]:
#                         self.lugatni_ichini_korish()
#                   elif n == sonlar[2]:
#                         self.izlash()
#                   elif n == sonlar[3]:
#                         self.chiqish()
#                   else:
#                         print("Xato kiritingiz:")
#                         os.system("clear")
#
#       def start(self):
#             son = ['1', '2']
#             print("""
#             ----------Inglizcha_O'zbekcha Lug'at----------
#
#                   1. Start
#                   2. Exit
#             """)
#
#             n = input(">>>").strip()
#             while n not in son:
#                   n = input("Xato kiritingiz:>>>>").strip()
#
#             if n == son[0]:
#                   os.system("clear")
#                   self.pri()
#             elif n == son[1]:
#                   print("\t\t-----XAYR-----")
#
#
# foyda = Logat()
# foyda.start()




