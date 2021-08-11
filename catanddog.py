import random


def get_animal_situation():
    
    cat1 = random.randint(1,10)
    cat2 = random.randint(1,10)
    mouse = random.randint(1,10)

    how_far_cats0 = cat1 - cat2
    how_far_mouse_and_cat1 = abs(mouse - cat1)
    how_far_mouse_and_cat2 = abs(mouse - cat2)

    print(cat1)
    print(cat2)
    print(mouse)

    if how_far_mouse_and_cat1 < how_far_mouse_and_cat2:
        print('Cat A Win!')

    elif how_far_mouse_and_cat2 < how_far_mouse_and_cat1:
        print('Cat B Win!')

    else:
        print('Mouse Win!')

get_animal_situation()