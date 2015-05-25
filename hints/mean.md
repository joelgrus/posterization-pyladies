probably the best first step is to create a list for the results.

if we're computing the mean of `ps[0]`, `ps[1]`, ...  then the result
should have the same length as all of them.

```python
length = len(ps[0])
result = [0 for _ range(length)]
```

for each position we want to to add up all the elements at that position 

```python
for position in range(length):
    for p in ps:
        result[position] += p[position]
```

that's the *sum* of the inputs, to get the `mean` we need to divide by the
number of inputs

```python
num_inputs = len(ps)
result = [x / num_inputs for x in result]
```
