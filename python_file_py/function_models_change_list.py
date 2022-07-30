unprinted_models = ['antimatter driven engine','ecological cycle system','curvature driven spacecraft']
printed_models = [ ]

def print_models(unprinted_models,printed_models):
	while unprinted_models:
		current_models = unprinted_models.pop()
		print(f"\nPrinting models: {current_models.title()}")
		printed_models.append(current_models)


def show_models(printed_models):
	print("\nThese models are printed: ")
	for printed_model in printed_models:
		print("\n" + printed_model.title())


print_models(unprinted_models[:],printed_models)
show_models(printed_models)
print(unprinted_models)