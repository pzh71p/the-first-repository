sandwich = ['chip_butty','ham_and_cheese_sandwich','chip_butty','montreal_bacon_sandwich','chip_butty',]

print(f"We heve sold out 'Chip_butty'!")
while True:
	if "chip_butty" in sandwich:
		sandwich.remove("chip_butty")
	else:
		break
print("We still have :")
for i in sandwich:
	print("\t" + i.title())