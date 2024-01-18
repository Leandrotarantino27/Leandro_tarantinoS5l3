
Code



Python 3 (ipykernel)
n
nome_scuola = "Epicode"
indice = 0
while indice < len(nome_scuola):
    print(nome_scuola[indice])
    indice += 1
E
p
i
c
o
d
e
nome_scuola = "Epicode"
for lettera in list(nome_scuola):
    if lettera < nome_scuola[0]:
        print(lettera)
nome_scuola = "Epicode"
for lettera in list(nome_scuola):
    print(lettera, end=" ")
E p i c o d e 
indice = 0
while indice <= 20:
    print(indice)
    indice += 1
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
for x in range(0,21):
    print(x)
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
indice = 0
power = 1
while indice <= 10:
    print(power)
    power*=2
    indice += 1
indice = 0
power = 1
while indice <= 10:
    print(power)
    power*=2
    indice += 1
1
2
4
8
16
32
64
128
256
512
1024
for power in lista:
    if power <=10
    print(power)
    else:
        print("fine")
power = 1
for indice in range(11):
    print(power)
    power *= 2
1
2
4
8
16
32
64
128
256
512
1024
dizionario_auto = {
    "Ada": "Punto",
    "Ben": "Multipla",
    "Charlie": "Golf",
    "Debbie": "107"
}
print(dizionario_auto)
print("L'auto di Debbie è una", dizionario_auto["Debbie"])
for auto in dizionario_auto.values():
    if auto != "Multipla":
        print(auto)
​
nuovi_proprietari = {"Ben": "Polo", "Fred": "Octavia", "Grace": "Yaris", "Hugh": "Clio"} 
dizionario_auto.update(nuovi_proprietari)
​
for proprietario, auto in dizionario_auto.items():
    print(proprietario, "guida una", auto)
{'Ada': 'Punto', 'Ben': 'Multipla', 'Charlie': 'Golf', 'Debbie': '107'}
L'auto di Debbie è una 107
Punto
Golf
107
Ada guida una Punto
Ben guida una Polo
Charlie guida una Golf
Debbie guida una 107
Fred guida una Octavia
Grace guida una Yaris
Hugh guida una Clio
numeri = [10, 15, 20, 25, 30, 35]
def min_max(lista):
    minimo = lista[0]
    massimo = lista[0]
    for numero in lista:
        if numero < minimo:
            minimo = numero
        if numero > massimo:
            massimo = numero
    return minimo, massimo
numeri = [10, 15, 20, 25, 30, 35]
minimo, massimo = min_max(numeri)
print("Il valore minimo è", minimo)
print("Il valore massimo è", massimo)
Il valore minimo è 10
Il valore massimo è 35
numeri = [10, 15, 20, 25, 30, 35] 

def tre_numeri_piu_grandi(lista):
    if len(lista)<3:
        return"mi dispiace! la lista deve contenere almento tre numeri,riprova: "
    else:
        numeri_ordinati= sorted(set(lista), reverse=True)
        return numeri_ordinati[:3]
    
numeri = [10, 15, 20, 25, 30, 35] 
risultato=tre_numeri_piu_grandi(numeri)
print("I tre numeri più grandi sono: ", risultato)
I tre numeri più grandi sono:  [35, 30, 25]
numeri = [10, 15, 20, 25, 30, 35] 
def media_nuemri(lista, K):
    numeri_validi = [numero for numero in lista if numero >= K]
    if len(numeri_validi)==0:
           return"non ci sono numeri > o uguali a K nella lista."
    else:
        media=sum(numeri_validi) / len(numeri_validi)
        return media
    
numeri = [10, 15, 20, 25, 30, 35] 
K = 50
risultato = media_numeri(numeri, K)
if type(risultato) == str:
    print(risultato)
else:
    print("La media dei numeri maggiori o uguali a", K, "è", risultato)
Non ci sono numeri maggiori o uguali a K nella lista.






o
def aster(numeri):
    for numero in numeri:
        print("*" *numero)
        
numeri = [5,2,3,4]
aster(numeri)
*****
**
***
****