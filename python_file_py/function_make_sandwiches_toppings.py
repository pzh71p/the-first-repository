def make_sandwiches(size,*toppings):
    print(f"We will make a sandwich which has a size of {size} inch")
    for i in toppings:
        print(f"--With topppings of {i.title()}")

make_sandwiches(16,'cheese','shits','idionts')