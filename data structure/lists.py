lst = ["Avroot", "Arzoo", "Kumail", "Kalleanka"]
print("The list is: ",lst)
print("The list's length is: ", len(lst))
print("The first element is: ", lst[0])
print("The last element is: ", lst[-1])


lst.append('Musse Pigg')
print("The list now is: ", lst)

lst.remove('Avroot')
print("The list now is: ", lst)

lst.sort()
print("The list sorted is: ", lst)

lst.pop(1)
print("The list now is: ", lst)

lst.reverse()
print("The list reversed is: ", lst)

print("The list multiplied is: ", lst*2)

lst = lst[:1]
print("The list sliced: ", lst)

lst.clear()
print("The list now is: ", lst)