my_set = {12,24,36,48}
print("Set: ", my_set)
my_set.add(5)
print("Updated Set: ",my_set)

s1 = my_set
s2 = {21,42,63,84}
print("Second Set: ", s2)

print("Set Difference: ")
print(s1.difference(s2))

print("Symmeterric Difference: ")
print(s1.symmetric_difference(s2))