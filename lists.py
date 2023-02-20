food = ["Pizza", "Sushi", "Pasta", "Elemento da togliere", "Bistecca", "Hamburger"]

food.append("Elemento aggiunto")
food.remove("Elemento da togliere")
# food.pop()  # removes last element
food.insert(0, "Elemento indice 0 inserito")
food.sort()  # sorts alphabetically
# food.clear()  # removes all the elements

for x in food:
    print(x)


# 2D list is a list of lists (multidimensional list)

drinks = ["caffè", "coca cola", "acqua"]
dinner = ["pizza", "hamburger", "sushi", "patatine"]
dessert = ["torta", "tiramisù"]

foods = [drinks, dinner, dessert]

print(foods)
print()

print(foods[1])
print(foods[2][1])  # tiramisù

