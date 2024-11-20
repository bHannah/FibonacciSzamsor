menny = int(input("Hány számot számítsunk ki?: "))

lista = []
elso_elem = 0
masodik_elem =1
print("A fibonacci sorozat első két eleme: ", elso_elem, " ", masodik_elem)
for i in range(menny):
  szamitott = elso_elem+masodik_elem
  print(szamitott)
  elso_elem = masodik_elem
  masodik_elem = szamitott
print("Megállapítható hogy a számsorozat következő tagja mindig az előző két szám összege!")