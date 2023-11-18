products = [
    'eggs', 'salt', 'water', 'salted cucumbers',
    'sausage', 'potato', 'carrot', 'green peas',
    'corn', 'crab sticks', 'rice', 'tomatoes',
    'sunflower oil', 'mayonnaise', 'onion', 'cod liver',
    'cucumbers'
]
Cod_liver_salad = [
    'rice', 'cod liver', 'onion'
]
Olivie = [
    'sausage', 'potato', 'carrot', 'green peas',
    'mayonnaise', 'salt', 'salted cucumbers', 'eggs'
]
Vegetable_salad = [
    'tomatoes', 'cucumbers', 'mayonnaise', 'onion',
]
Crab_stick_salad = [
    'crab sticks', 'corn', 'rice', 'eggs',
    'salt', 'mayonnaise'
]
Boiled_eggs = [
    'eggs', 'salt'
]

def Salads(a, b, c, d, e, f):
    if set(a).issubset(b) is True:
        print('We can cook cod liver salad')
    else:
        a_items = []
        for element in a:
            if element not in b:
                a_items.append(element)
        print('We can not cook cod liver salad. We do not have enough ' + ', '.join(a_items))


    if set(c).issubset(b) is True:
        print('We can cook olivie')
    else:
        c_items = []
        for element in c:
            if element not in b:
                c_items.append(element)
        print("We can't cook olivie. We do not have enough " + ', '.join(c_items))


    if set(d).issubset(b) is True:
        print('We can cook crab stick salad')
    else:
        d_items = []
        for element in d:
            if element not in b:
                d_items.append(element)
        print("We can't cook crab stick salad. We do not have enough " + ', '.join(d_items))


    if set(e).issubset(b) is True:
        print('We can cook boiled eggs')
    else:
        e_items = []
        for element in e:
            if element not in b:
                e_items.append(element)
        print("We can't cook boiled eggs. We do not have enough " + ', '.join(e_items))


    if set(f).issubset(b) is True:
        print('We can cook vegetable salad')
    else:
        f_items = []
        for element in f:
            if element not in b:
                f_items.append(element)
        print("We can't cook vegetable salad. We do not have enough " + ', '.join(f_items))


print(Salads(Cod_liver_salad, products, Olivie, Crab_stick_salad, Boiled_eggs, Vegetable_salad))