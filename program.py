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
    'crab sticks', 'corn', 'rise', 'eggs',
    'salt', 'mayonnaise'
]
Boiled_eggs = [
    'eggs', 'salt'
]


if set(Cod_liver_salad).issubset(products) is True:
    print('We can cook cod liver salad')
else:
    print('We can not cook cod liver salad')