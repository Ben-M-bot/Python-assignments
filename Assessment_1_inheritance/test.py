from Murphy_Ben import *

if __name__ == "__main__":
    o1 = Orc("ha", 74, False)
    ogre = Orc("Olorug", 3.1, True)
    j = Orc("juhd", 2.9, True)
    k = Orc("Kaid", 3, False)
    o1.fight(k)
    ogre.fight(j)
    j.fight(o1)
    print(ogre.name)
    print(k.strength)
    print(k.weapon)
    tr = Orc("grung", 4.9, 3)
    print(tr.strength)


a2=Archer("archer2", 2.3, "Pepe")
k1= Knight("Aragorn", 5, "Gondor",[])
orc1=Orc("Ogrorg", 5, True)
a2.fight(orc1)
print(orc1.strength)
print(a2.strength)
print(round(2.3 - 0.5, 1))