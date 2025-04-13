## Order Conditions and Loop

---
#### 1. Conditions statement
Usually, this kind of logic is implemented using an `if` statement. 
The condition is written after `if`. If the condition is `True`, 
the main block of code runs; otherwise, the program continues or runs
an alternative block.
```
a = 20
b = 40

if (a/b > 1):
    print(Higher)
else:
    print(Lower)
```
#### 2. Loops
To access elements in lists and similar data types, we use loops.
##### 2.1 For
###### 2.1.1 List data
```
my_list = [1,2,3,4,5,6,7,8,9]
for x in my_list:
    print(x)
```
###### 2.1.2 Tuple data
```
people = (('Ali', 23), ('John', 45), ('Sara', 28))
for person in people:
    name, age = person
    print(f'{name} is {age} year old.')
```
###### 2.1.3 dict data
```
info = {
    'Ali': (23, 170),
    'John': (24, 177),
    'Jack': (40, 184),
    'Sara': (33, 166),
}
   
for key in info:
    print(f"{key} is {info[key][0]} year old and him height is 
    {info[key][1]}.")
    
for person, data in info.items():
    print(person, data)
```
##### 2.2 While
A `while` loop keeps running as long as the condition is `True`. 
The code inside the block will continue to execute until 
the condition becomes `False`.
```
a = 0
while a<=5:
    print (f'a is {a}')
    a += 1

print(f'finishing with {a}')
```
Sometimes, we don't want a loop to finish normally. In such cases,
we can use `break` to exit the loop early, `continue` to skip the current
iteration, or use `pass` as a placeholder for future code.
```
for _ in range(10):
    pass

for i in range(10):
    if i == 5:
        break;
        print(i)

for n in range(20):
    if i % 3 == 0:
        continue
    print(i)
```
##### 2.3 List comprehension
Sometimes, we can use loops to create a list.
```
one_list = [0,2,4,6,8,10]
two_list = []

for x in one_list:
    two_list.append(x ** 2)
print(two_list)
```
Advance code
```
one_list = [0,2,4,6,8,10]
two_list = [x ** 2 for x in one_list]

three_list = ['even' if x%2==0 else 'odd' for x in one_list]
```
##### 2.3 self study
###### 2.3.1 range(start, stop, step)
###### 2.3.2 enumerate()
###### 2.3.3 zip()