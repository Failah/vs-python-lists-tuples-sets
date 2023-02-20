# set is a collection that is unordered and unindexed; it doesn't allow any duplicated value

ingredients = {"uova", "biscotti", "mascarpone", "caffè", "cioccolato", "rimuovimi"}
extra_set = {"el1", "el2", "el3"}

ingredients.add("Ingrediente extra")
ingredients.remove("rimuovimi")
# ingredients.clear()  # rimuove tutto dal set

for x in ingredients:
    print(x)  # vengono stampati in disordine

print()

ingredients.update(extra_set)  # adds all the element to the starting set (all extras go into ingredients)

for x in ingredients:
    print(x)