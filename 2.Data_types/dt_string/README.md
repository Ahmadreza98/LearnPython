## Data Types: String

---
In generally, the string structure implement with single or double 
quote. For example:
```
Name = 'John' or "John"
Full_name = 'John Smith' or "John Smith"
```
The string structure is similar to a "List". We can slice a string 
into smaller character.
```
ns = "Hello, I'm John Smith, I'm 22 years old"
ns[0] -> res: H
ns[-1] -> res: d
ns[1:4] -> res: ell
ns[1:5:2] -> res: el
```
To slice, we use three values: `[start:stop:step]`.The step value is 
optional.
```
ns = '0123456789'
ns[1:6] -> res: '12345'
ns[1:6:2] -> res: '135'
ns[::-1] -> res: '9876543210'
```
To Complicate string used to 3 double quote.
```
""" Hi,
my name is John Smith,
I'm 22 years old,
I'm single. """
```
The string is immutable. There are many methods to combine string 
data with other data types.
```
Full_name = "John Smith"
print("Hello" + " " + Full_name)
```
This method name is "String Interpolation".
```
print(f"Hello {Full_name}"
print("Hello {name}, {family} is {age} year old.".format(name=name, 
family=Full_name, age=age))
```