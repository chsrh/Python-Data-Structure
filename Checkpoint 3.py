#Answer 01 :
my_list = [2, 3, 6]
result = 1
for num in my_list:
    result *= num
print(result)

#Answer 02 :
my_list2 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
my_list2.sort(key=lambda x: x[-1])
print(my_list2)


#Answer 03 :
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

d3 = {}
for key in d1.keys():
    if key in d2.keys():
        d3[key] = d1[key] + d2[key]
    else:
        d3[key] = d1[key]

for key in d2.keys():
    if key not in d3.keys():
        d3[key] = d2[key]

print(d3)

#Answer 04 :
n = 8
result = {}
for i in range(1, n+1):
    result[i] = i*i
print(result)


#Answer 05 :
my_list5= [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

for i in range(len(my_list5)):
    for j in range(i+1, len(my_list5)):
        if float(my_list5[i][1]) < float(my_list5[j][1]):
            result = my_list5[i]
            my_list5[i] = my_list5[j]
            my_list5[j] = result

print(my_list5)

#Answer 06 :
my_set6 = set([0, 1, 2, 3, 4, 5, 6, 7])
print(my_set6)

    #Iterate items
for item in my_set6:
    print(item)

    #Add item
my_set6.add(8)
print(my_set6)

    #Remove item
my_set6.remove(0)
print(my_set6)