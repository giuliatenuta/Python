from random import random
from random import choice
from random import randint
import os

ora1=["[]","[]","[]","[]","[]","[]"]
ora2=["[]","[]","[]","[]","[]","[]"]
ora3=["[]","[]","[]","[]","[]","[]"]
ora4=["[]","[]","[]","[]","[]","[]"]
ora5=["[]","[]","[]","[]","[]","[]"]
ore=[ora1,ora2,ora3,ora4,ora5]
tab={"giorni":"[Lunedi][Martedi][Mercoledi][Giovedi][Venerdi][Sabato]",
"1°":ora1,
"2°":ora2,
"3°":ora3,
"4°":ora4,
"5°":ora5
   }

a=["lunedi","martedi","mercoledi","giovedi","venerdi","sabato"]
b=int(input("Inserire ore settimanali: "))
if b==30:
    print()
elif b<30 and b>=27:
    c=b%6 
    c=6-c
    if c==1:
        d=choice(a)
        for i in range(len(a)):
            if d==a[i]:
                ora5[i]="[vuoto]"
    else:
        e=0
        while c!=0:
            d=choice(a)
            if e!=d:
                for y in range(len(a)):
                    if d==a[y]:
                        ora5[y]="[vuoto]"
                        e=d
                        c-=1


for i in range(11):
    os.system("clear")
    f=input('''Inserire  una materia compresa tra le seguenti, nell'ordine a voi presentatosi:
            -italiano,
            -religione,
            -educazione fisica,
            -matematica,
            -latino,
            -inglese,
            -geostoria,
            -arte,
            -informatica,
            -fisica,
            -scienze: ''')
    g=int(input("Inserisci ore settimanali della materia scritta precedentemente: "))
    if  f=="educazione fisica":
        while True:
            h=randint(0,5)
            if ora2[h]=="[]" and ora3[h]=="[]":
                ora2[h]="["+f+"]"
                ora3[h]="["+f+"]"
                break
    elif f=="religione":
        while True:
            h=randint(0,5)
            if ora5[h]=="[]":
                ora5[h]="["+f+"]"
                break
    elif f=="italiano" :
        while True:
            h=randint(0,5)
            if ora1[h]=="[]" and ora2[h]=="[]":
                ora1[h]="["+f+"]"
                ora2[h]="["+f+"]"
                break
        while True:
            j=randint(0,5)
            if j!= h:
                if ora3[j]=="[]":
                    ora3[j]="["+f+"]"
                    break
        while True:
            k=randint(0,5)
            if k!= j:
                if ora5[k]=="[]":
                    ora5[k]="["+f+"]"
                    break
    else:
        
        for y in range(g):
            m=0
            for n in range(5):
                l=ore[n]
                if m==0:
                    for p in range(6):
                        if l[p]=="[]":
                            l[p]="["+f+"]"
                            m=1
                            ore[n]=l
                            break
                else:break


                    
                

tab["1°"]=ore[0]
tab["2°"]=ore[1]
tab["3°"]=ore[2]
tab["4°"]=ore[3]
tab["5°"]=ore[4]
print(tab["giorni"])
print(tab["1°"])
print(tab["2°"])
print(tab["3°"])
print(tab["4°"])
print(tab["5°"])