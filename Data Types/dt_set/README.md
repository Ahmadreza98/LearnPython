## Data Type: Set

---
A set is a data type. It is a container that can hold numbers and 
strings. Keep in mind that all values in a set must be 
unique—duplicates are not allowed.
```
my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add("Ali")
my_set.add("Hadi")
```
Also, the `union()` and `intersection()` methods are used to combine 
or compare two sets. The union method adds elements from both sets, 
while the intersection method returns only the common elements.
```
my_set = set(['Ali', 'John', 'Susan'])
your_set = set(['Ali', 'Jack', 'Sara'])
my_name.intersection(your_set) -> res: 'Ali'
my_name.union(your_set) -> res: {'Ali', 'John', 'Susan','Jack', 'Sara'}
```