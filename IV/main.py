import random

two_groups = list()
for i in range(120):
    my_random = random.choice([1, 2, 3])
    my_random_int = random.randint(1, 9)
    two_groups.append([f"patient {i + 1}", my_random, my_random_int])

print(*two_groups, sep="\n")
print()

three_groups = list()
for i in range(120):
    my_random = random.choice([1, 2, 3])
    my_random_int = random.randint(1, 9)
    my_random_int_2 = random.randint(150, 170)
    three_groups.append([f"patient {i + 1}", my_random, my_random_int, my_random_int_2])

print(*three_groups, sep="\n")

three_groups = list()
for i in range(120):
    my_random = random.choice([1, 2, 3])
    my_random_int = random.randint(1, 9)
    my_random_int_2 = random.randint(150, 170)
    three_groups.append([f"patient {i + 1}", my_random, my_random_int, my_random_int_2])

print(*three_groups, sep="\n")
print()

equal_groups = list()
for i in range(120):
    my_random = random.choice([1, 2, 3])
    equal_groups.append([f"patient {i + 1}", my_random, my_random])

print()

two_one_groups = list()
for i in range(120):
    my_randoms   = random.choices(population=[0, 1], weights=[0.33333, 0.66666], k=120)
    my_randoms_2 = random.choices(population=[55, 67], weights=[0.33333, 0.66666], k=120)
    two_one_groups.append([f"patient {i + 1}", my_randoms[i], my_randoms_2[i]])

print(*two_one_groups, sep='\n')