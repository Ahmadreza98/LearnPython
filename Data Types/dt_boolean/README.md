## Data Type: Boolean

---
Boolean is a logical data type. It represents a result that is 
either `True` or `False`.
```
1 > 2 -> res: True: T
2 < 5 -> res: False: F
age = 15
age.isdigit() -> res: T
age = 15.4
age.isdigit() -> res: F
```
Booleans are often used in conditional statements to control the 
flow of a program.
1. OR
```
age = 15
name = "John"
if (age => 15) or (name == 'Ali') -> res: T
```
2. AND
```
age = 15
name = "John"
if (age => 15) and (name == 'Ali') -> res: F
```
3. NOT
```
age = 15
name = "John"
if NOT (age => 15) -> res: F
```
4. IN
```
my_list = [1,2,3, 'John',3.14,'Ali']
if 'John' in my_list -> res: T
```
