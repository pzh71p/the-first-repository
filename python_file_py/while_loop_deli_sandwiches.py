sandwich = ['ham_and_cheese_sandwich','chip_butty','montreal_bacon_sandwich']
finished_sandwich =[ ]

for i in sandwich:
	print(f"I made you {i.title()} sandwich")
	finished_sandwich.append(i)
print(f"We have finished all sandwich!")
print(f"Here are your sandwiches!")
for b in finished_sandwich:
	print("\t" + b.title())