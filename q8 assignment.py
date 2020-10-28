pokemons = '''arceus piplup wooloo tyranitar audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon cresselia croagunk darmanitan deino emboar emolga exeggcute gabite greninja girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask'''

# Split through spacing 
list_pokemons = pokemons.split(" ")

# Split all pokemons names into a dictionaru
pokemon_dict = {}
for names in list_pokemons:
    if names[0] not in pokemon_dict:
        pokemon_dict[names[0]] = [names]
    else:
        pokemon_dict[names[0]].append(names)


def list_creation(order):
    global longest_order
  

    # Check the longest 
    if len(order) > longest_count:
        longest_count = len(order)
        longest_order = order

    # This is use to find the next value / Recursion
    if chain[-1][-1] in pokemon_dict:
        for name in pokemon_dict[order[-1][-1]]:
            if name not in order:
                oder.append(name)
                list_creation(order)


# Iterate all the names of the pokemons
for order in list_pokemons:
    list_creation([order])

print(longest_order)