# first i set my variablers as floats
penne_pasta_12pack_16oz = 16.68
pasta_sauce_24oz = 6.98
garlic_cloves_bagof20 = 16.78
italian_seasoning = 15.26
baguettes_twin_pack = 3.00
meatballs_12oz_bag = 4.39

# next i re-assign my variable and multiply by 100 to make them ints
penne_pasta_12pack_16oz *= 100
pasta_sauce_24oz *= 100
garlic_cloves_bagof20 *= 100
italian_seasoning *= 100
baguettes_twin_pack *= 100
meatballs_12oz_bag *= 100

# then i subtotal the ints
subtotal = (penne_pasta_12pack_16oz+pasta_sauce_24oz+garlic_cloves_bagof20+italian_seasoning+baguettes_twin_pack+meatballs_12oz_bag)

# then i reassign and divide by 100 to make ti a float again
subtotal /= 100

# then i print some text along with my subtotal variable
print("Your subtotal is $", subtotal)