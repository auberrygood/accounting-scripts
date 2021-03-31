"""Print out all the melons in our inventory."""


# from melons import melon_names, melon_seedlessness, melon_prices
from melons import melons

# def print_melon(melon_name):
#     """Print each melon with corresponding attribute information."""

#     # have_or_have_not = 'have'
#     # if seedless:
#     #     have_or_have_not = 'do not have'
#     melon_info[]

#     # print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')


#     print (f'{melon}'s  )


# for melon in melon_info:
#     print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])

for melon in melons:
    print (melon)
    print (f"   price: ${melons[melon]['price']:.2f}")
    print (f"   seedless: {melons[melon]['seedless']}")
    print (f"   flesh color: {melons[melon]['flesh_color']}")
    print (f"   rind color: {melons[melon]['rind_color']}")
    print (f"   weight: {melons[melon]['weight']}")
    # print ()