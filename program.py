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
    'tomatoes', 'cucumbers', 'mayonnaise', 'onion'
]
Crab_stick_salad = [
    'crab sticks', 'corn', 'rice', 'eggs',
    'salt', 'mayonnaise'
]
Boiled_eggs = [
    'eggs', 'salt'
]

def Salads(a, b, c, d, e):
    if set(a).issubset(b) is True:
        print('We can cook cod liver salad')
    else:
        print("We can't cook cod liver salad")


    if set(c).issubset(b) is True:
        print('We can cook olivie')
    else:
        print("We can't cook olivie")


    if set(d).issubset(b) is True:
        print('We can cook crab stick salad')
    else:
        print("We can't cook crab stick salad")


    if set(e).issubset(b) is True:
        print('We can cook boiled eggs')
    else:
        print("We can't cook boiled eggs")


print(Salads(Cod_liver_salad, products, Olivie, Crab_stick_salad, Boiled_eggs))