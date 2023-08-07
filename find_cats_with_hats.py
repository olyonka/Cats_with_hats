def find_cats_with_hats():
    cats = [0] * 100

    for i in range(1, 101):
        for j in range(i - 1, 100, i):
            cats[j] = 1 - cats[j]

    for i, hat in enumerate(cats):
        if hat == 1:
            print(f"Cat #{i + 1} has a hat")

find_cats_with_hats()