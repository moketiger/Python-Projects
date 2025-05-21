
atomic_weights = {
    "H": 1.008,"He": 4.0026,"Li": 6.94,"Be": 9.0122,"B": 10.81,"C": 12.011,"N": 14.007,"O": 16.00,"F": 18.998,"Ne": 20.180,
    "Na": 22.990,"Mg": 24.305,"Al": 26.982,"Si": 28.085,"P": 30.974,"S": 32.06,"Cl": 35.45,"Ar": 39.948,"K": 39.098,"Ca": 40.078,
    "Sc": 44.956,"Ti": 47.867,"V": 50.942,"Cr": 51.996,"Mn": 54.938,"Fe": 55.845,"Co": 58.933,"Ni": 58.693,"Cu": 63.546,
    "Zn": 65.38,"Ga": 69.723,"Ge": 72.630,"As": 74.922,"Se": 78.971,"Br": 79.904,"Kr": 83.798,"Rb": 85.468,"Sr": 87.62,"Y": 88.906,
    "Zr": 91.224,"Nb": 92.906,"Mo": 95.95,"Tc": 98.0,"Ru": 101.07,"Rh": 102.91,"Pd": 106.42,"Ag": 107.87,"Cd": 112.41,
    "In": 114.82,"Sn": 118.71,"Sb": 121.76,"Te": 127.60,"I": 126.90,"Xe": 131.29,"Cs": 132.91,"Ba": 137.33,"La": 138.91,"Ce": 140.12,
    "Pr": 140.91,"Nd": 144.24,"Pm": 145.0,"Sm": 150.36,"Eu": 151.96,"Gd": 157.25,"Tb": 158.93,"Dy": 162.50,"Ho": 164.93,"Er": 167.26,
    "Tm": 168.93,"Yb": 173.05,"Lu": 174.97,"Hf": 178.49,"Ta": 180.95,"W": 183.84,"Re": 186.21,"Os": 190.23, "Ir": 192.22,
    "Pt": 195.08,"Au": 196.97,"Hg": 200.59,"Tl": 204.38,"Pb": 207.2,"Bi": 208.98,"Po": 209.0,"At": 210.0,"Rn": 222.0,"Fr": 223.0,
    "Ra": 226.0,"Ac": 227.0,"Th": 232.04,"Pa": 231.04,"U": 238.03,"Np": 237.0,"Pu": 244.0,"Am": 243.0,"Cm": 247.0,"Bk": 247.0,"Cf": 251.0,
    "Es": 252.0,"Fm": 257.0, "Md": 258.0,"No": 259.0,"Lr": 266.0, "Rf": 267.0,"Db": 270.0,"Sg": 271.0,"Bh": 270.0,"Hs": 277.0,
    "Mt": 278.0, "Ds": 281.0,"Rg": 282.0,"Cn": 285.0, "Nh": 286.0,"Fl": 289.0,"Mc": 290.0,"Lv": 293.0,"Ts": 294.0,"Og": 294.0
}

expet = 0
elements = {}
new_formula = []
finel_weight = 0

count = 2
number = ""

print("A formula write this way: H2O (this is water)")
formula = input("What atomic formula weight do you want to know\nwrite it here: ")

for i in formula:
    try: i = int(i)

    except ValueError:
        i = str(i)
    new_formula.append(i)

for z in new_formula:
    number = ""
    count = 0
    index = new_formula.index(z ,expet)
    if type(z) == int: #Re21PtTe270
        if not type(new_formula[index - 1]) == int:
            if new_formula[index - 1] == new_formula[index - 1].upper():
                elements[new_formula[index - 1]] = z
            else:
                elements[str(new_formula[index - 2]) + str(new_formula[index - 1])] = z
        else:
            while type(new_formula[index - count]) == int:
                number = str(new_formula[index - count]) + number
                count += 1
            if new_formula[index - count] == new_formula[index - count].upper():
                elements[ str(new_formula[index - count])] = str(number)
            else:
                elements[str(new_formula[index - count - 1]) + str(new_formula[index - count])] = str(number)
    elif type(z) == str:
        if new_formula.index(z , expet) == len(new_formula) - 1:
            if new_formula[index ] == new_formula[index].upper():
                elements[z] = 1
            elif type(new_formula[index - 1]) == type(new_formula[index - 1]):
                if new_formula[index - 1] == new_formula[index - 1].upper():
                    elements[str(new_formula[index - 1]) + str(new_formula[index])] = 1
        elif type(new_formula[index + 1]) == str:
            if new_formula[index + 1] == new_formula[index + 1].upper():
                if new_formula[index] == new_formula[index].upper():
                    elements[z] = 1
                else:
                    elements[str(new_formula[index - 1]) + str(new_formula[index])] = 1

    expet += 1
print(elements)
e = 0
for key in elements.keys():
    if key in atomic_weights.keys():
        print(float(elements[key]) * float(atomic_weights[key]))
        finel_weight += (float(elements[key]) * float(atomic_weights[key]))
    else:
        print(key + " is not in the periodic table")
        break
    e += 1

if e == len(elements.keys()):
    print("The weight of " + str(formula) + " is:\t" + str(finel_weight))

