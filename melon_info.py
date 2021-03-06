"""Print out all the melons in our inventory."""

'''ORIGINAL PROGRAM'''
# from melons import melon_names, melon_seedlessness, melon_prices

# def print_melon(melon_name):
#     """Print each melon with corresponding attribute information."""

#     # have_or_have_not = 'have'
#     # if seedless:
#     #     have_or_have_not = 'do not have'
#     melon_info[]

#     # print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')


# for melon in melon_info:
#     print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])


'''MY UPDATED PROGRAM'''
# from melons import melons

# def print_melons(melons):
#     for melon in melons:
#         print (melon.upper())
#         print (f"   price: ${melons[melon]['price']:.2f}")
#         print (f"   seedless: {melons[melon]['seedless']}")
#         print (f"   flesh color: {melons[melon]['flesh_color']}")
#         print (f"   rind color: {melons[melon]['rind_color']}")
#         print (f"   weight: {melons[melon]['weight']}")
#         print ()

# print_melons(melons)

'''SOLUTION GIVEN'''
from melons import melons

def print_all_melons(melons):
    """Print each melon with corresponding attribute information."""

    for melon_name, attributes in melons.items():
        print(melon_name.upper())

        for attribute, value in attributes.items():
            print(f'{attribute}: {value}')

        print('===================================')


print_all_melons(melons)