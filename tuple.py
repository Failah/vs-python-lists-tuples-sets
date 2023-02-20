# tuple is a collection that is ordered and unchangeable

student = ("Valerio", 32, "male")

print(student.count("Valerio"))
print(student.index((32)))

for x in student:
    print(x)

if "Valerio" in student:
    print(student[0] + " is here!")

