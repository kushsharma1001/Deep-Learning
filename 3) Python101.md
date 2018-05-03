# PYTHON 101
[Deep-Learning/Python101.md at master · kushsharma1001/Deep-Learning · GitHub](https://github.com/kushsharma1001/Deep-Learning/blob/master/Python101.md)

--- 

## Data types in python

### 1) Numbers
``` 
eip = 10
print(eip)
print(eip + 1)
print(eip - 1)
print(eip * 2)
print(eip / 2)
print(eip ** 2) #exponentiation
```
### 2) boolean
```
eip_in = True
eip_out = False
print(type(eip_in))
print(eip_out)
print(eip_in)
print(eip_in and eip_out)
```
### 3) string
```
mlblr = 'hello'
print(mlblr)
mlblr = "Hi"
print(mlblr)
print(mlblr + " Kush Sharma!")
```
### 4) Lists
```
eip_list = [1,2,3,4,5]
print(eip_list)
eip_list2 = [1, "One", 2, "Two"]
print(eip_list2)

print(eip_list[0]) #Prints 1st element of "eip_list" list
print(eip_list2[-1]) #Prints last element of "eip_list2" list

print(eip_list[:2]) #Prints elements of eip_list from 0 index to 1 index, 2 is exclusive
print(eip_list[2:])  #Prints 2nd element to last element from eip_list
```
### 5) Dictionary
```
eip_dict = {'cat': 'cute', 'dog': 'furry'}  # Create a new dictionary with some data in form of Key Value pairs
print(eip_dict['cat'])
print('cat' in eip_dict)  # Check if a dictionary has a given key; prints "True"
eip_dict['fish'] = 'wet' # Adds data into Dictionary
print(eip_dict)
```
