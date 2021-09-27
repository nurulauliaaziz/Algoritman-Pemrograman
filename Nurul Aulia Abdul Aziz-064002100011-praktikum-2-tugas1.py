Created on Mon Sep 27 13:03:42 2021

@author: nurul
NAMA : Nurul Aulia Abdul Aziz
NIM : 064002100011
"""

import math



a = float(input("masukan nilai a : "))
b = float(input("masukan nilai b : "))

hasil = a + b
print("jumlah a ditambah b", hasil)

hasil = a - b
print("selisih a dan b", abs(hasil))

hasil = a * b
print("jumlah a dikali b", hasil)
      
hasil = a % b
print("jumlah pembagian a dan b",hasil)

hasil = a / b
print(" pembagian a dan b",hasil)

hasil = math.log10(a)
print("hasil log(a)",hasil)

hasil = a ** b
print("jumlah dari pangkat a dan b",hasil)
