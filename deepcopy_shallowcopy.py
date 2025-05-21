# Normal cases:

numeric_list = [100, 200, 300, 400]
numeric2 = numeric_list
print(id(numeric_list))
print(id(numeric2))
#it prints the same memory address of both the objects, in further if any changes made in numeric2 or numeric_list , it gets reflected back in both of the obj


#---------------------------SHALLOW COPY -------------------------------

import copy

number_list = [100, 200, 300, 400, 500]

shallow_copy = copy.copy(number_list)
#shallow_copy has the same data assigned to number_list as it is reffrring to it. 
# But in this case 

print(shallow_copy)
print(id(number_list))
print(id(shallow_copy))
#but here python allocates different memory address for both the obj, when we use shallow copy, any changes made in either 1 of the obj , it does not get reflecterd for the obj .

#----------------------shallow_copy in nested lists----------------------


lst1 = [[1,2,3,4,5], [5,6,7,8]]
lst2 =lst1.copy()
#or
lst2 =copy.copy(lst1)
lst2[1][2]= 0

print(lst1, id(lst1))
print(lst2, id(lst2))

# but in nested lists it does not works like that, python alloctes same memory address for both the objects and similarily changes done in either of the obj gets reflected to the other.

#--------------------------DeepCopy in lists---------------------------
import copy

lst1 = [5,4,3,2]
lst2= copy.deepcopy(lst1)

lst2[2] = 0
print(lst1, id(lst1))
print(lst2, id(lst2))


#--------------------------------Deep Copy in nested lists-------------------

import copy
lst1 = [[5,4,3,2],[8,7,6,9,]]
lst2= copy.deepcopy(lst1)

lst2[1][2] = 0
print(lst1, id(lst1))
print(lst2, id(lst2)) 

#Deep copy works same as lists and nested lists , python allocated diffreent mem space for both the obj, and niether of the obj changes will get reflected to the other.

