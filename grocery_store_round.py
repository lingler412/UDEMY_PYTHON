# first i set my variablers as floats

penne_pasta_12pack_16oz = 16.68
pasta_sauce_24oz = 6.98
garlic_cloves_bagof20 = 16.78
italian_seasoning = 15.26
baguettes_twin_pack = 3.00
meatballs_12oz_bag = 4.39

# then i subtotal all of my groceries

subtotal = (penne_pasta_12pack_16oz+pasta_sauce_24oz+garlic_cloves_bagof20+italian_seasoning+baguettes_twin_pack+meatballs_12oz_bag)

# then i round my subtotal to the nearest 2 digit decimal

rounded_subtotal = round(subtotal, 2)

# then i print some text along with my subtotal variable
print("Your subtotal is $", rounded_subtotal)

