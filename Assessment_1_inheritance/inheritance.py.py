class Fighter:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

    def __str__(self):
        fighter_des = "%s %0.1f" % (self._name, self._strength)
        return fighter_des

    def __getName(self):
        return self._name

    def __setName(self, new):
        if isinstance(new, str):
            self._name = new
        else:
            print("type ERROR")

    def __getStrength(self):
        return self._strength

    def __setStrength(self, s):
        if isinstance(s, int):
            s = float(s)
        if not isinstance(s, float):
            print("type ERROR")
        else:
            if s > 5:
                self._strength = 5
            elif s < 0:
                self._strength = 0
            else:
                self._strength = round(s, 1)

    name = property(__getName, __setName)
    strength = property(__getStrength, __setStrength)

    def __gt__(self, other):
        if isinstance(other, Orc) and isinstance(self, Orc):
            if self._weapon != other._weapon:
                if self._weapon:
                    return True
                return False
            else:
                if self._strength > other._strength:
                    return True
                return False

        elif (isinstance(self, Archer) or isinstance(self, Knight)) and isinstance(other, Orc):
            if other._weapon:
                if self._strength > other._strength:
                    return True
                return False
            return True

        elif isinstance(self, Orc) and (isinstance(other, Archer) or isinstance(other, Knight)):
            if self._weapon:
                if self._strength > other._strength:
                    return True
                return False
            return False

    def fight(self, other):
        if (isinstance(self, Archer) or isinstance(self, Knight)) and (isinstance(other, Archer) or isinstance(other, Knight)):
            print("fight ERROR")
            return
        if self > other:
            self.strength += 1
            other.strength -= 0.5
            print(self)
            return
        elif other > self:
            other.strength += 1
            self.strength -= 0.5
            print(other)
            return
        else:
            other.strength -= 0.5
            self.strength -= 0.5



class Orc(Fighter):
    def __init__(self, name, strength, weapon):
        Fighter.__init__(self, name, strength)
        self.weapon = weapon

    def __str__(self):
        orc_des = super().__str__() + " %s" % self._weapon
        return orc_des

    def __getWeapon(self):
        return self._weapon

    def __setWeapon(self, w):
        if not isinstance(w, bool):
            print("type ERROR")
        else:
            self._weapon = w

    # Properties
    weapon = property(__getWeapon, __setWeapon)


class Archer(Fighter):
    def __init__(self, name, strength, kingdom):
        Fighter.__init__(self, name, strength)
        self.kingdom = kingdom

    def __str__(self):
        archer_des = super().__str__() + " " + self._kingdom
        return archer_des

    def __getKingdom(self):
        return self._kingdom

    def __setKingdom(self, kingdom):
        if isinstance(kingdom, str):
            self._kingdom = kingdom
        else:
            print("type ERROR")

    kingdom = property(__getKingdom, __setKingdom)


class Knight(Archer):
    def __init__(self, name, strength, kingdom, archer_list):
        Archer.__init__(self, name, strength, kingdom)
        self.archer_list = archer_list

    def __str__(self):
        print(super().__str__() + " [", end="")
        for c in range(len(self._archer_list)):
            if c == len(self._archer_list) - 1:
                print(self._archer_list[c], end="")
            else:
                print(self._archer_list[c], end=", ")
        print("]")
        return ""

    def __getArcher_list(self):
        return self._archer_list

    def __setArcher_list(self, lst):
        if isinstance(lst, list):
            tempk = self.kingdom
            print(tempk)
            c = 0
            list1 = []
            while c < len(lst):
                if isinstance(lst[c], Archer):
                    if tempk == lst[c]._kingdom:
                        if lst[c] not in list1:
                            list1.append(lst[c])
                            c += 1
                            continue
                    c += 1
                else:
                    print("archers list ERROR")
                    c += 1
            self._archer_list = list1
        else:
            print("type ERROR")

    def addArcher(self, archer):
        if isinstance(archer, Archer):
            if self.kingdom == archer.kingdom:
                self.archer_list.append(archer)
        else:
            print("archers list ERROR")

    def removeArcher(self, archer):
        try:
            self.archer_list.remove(archer)
        except ValueError:
            print("%s, was not in the list" % archer)

    archer_list = property(__getArcher_list, __setArcher_list)

if __name__ == "__main__":
    o1 = Orc("Ghaol", 3.4, True)
    o2 = Orc("Glen", 60, False)
    o3 = Orc("Garry", 2, True)
    o4 = Orc("Eternal", 5, True)
    o5 = Orc("Cheat", "d", 3)
    print(o1)
    print(o3)
    o1.fight(o3)
    print("works" if o3 > o2 else "no")
    print(o3)
    o1.fight(o3)
    o1.fight(o4)
    print(o1)
    print(o4)
    o2.fight(o3)
    print(o1.name)
    print(o3.weapon)
    print(o4.strength)

    a = Archer("g", 3.4, "Glass")
    a2 = Archer("fr", 2, "Mordor")
    a3 = Archer("nub", 56, "Glass")
    a4 = Archer("hub", -23, "Glass")
    kn = Knight("n", 5, "Glass", [a, a3, a3, a3, a4])
    kn1 = Knight("tra", 2.4, "Mordor", [a, a2, a4])
    a.fight(kn)
    print(kn)
    print(kn1)
    kn.fight(o3)
    kn1.fight(o1)
    kn1.addArcher(a4)
    a5 = Archer("fran", 2, "Mordor")
    kn1.addArcher(a5)
    print(kn1)
    print(kn)
    kn1.removeArcher(a4)