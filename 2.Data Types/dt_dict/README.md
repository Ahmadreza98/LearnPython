## Data Type: Dict

---
A dictionary is a data type. It is generally structured with keys and 
values. This means every value has a corresponding key. To access a 
value, you need to use its key.
```
my_dict = {"apple": 20, "benana": 10, "orenage": 5}
my_dict["apple"] -> res: 20
```
One useful feature of dictionaries is that you can use a list as a 
value.
```
my_dict = {"apple": [15,20_000,500_000], "benana": 10, "orenage": 5}
my_dict["apple"] -> res: [15,20_000,500_000]
my_dict["apple"][0] -> res: 15
```