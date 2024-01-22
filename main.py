#Lists

shopping_list = ['apples', 'bananas', 'oranges', 'cheese']

#slicing in lists doesnt count your end range
print(shopping_list)
print(shopping_list[0])

#add items to lists
shopping_list.append('blueberries')

print(shopping_list)

#update items in lists
shopping_list[0]= 'cherries'
del shopping_list[1]

#length of lists
print(len(shopping_list))

shopping_list_2 = ['bread', 'jam', 'pb']

print(shopping_list+shopping_list_2)

list_num=(1,4,10,15)
print(max(list_num))
print(min(list_num))
