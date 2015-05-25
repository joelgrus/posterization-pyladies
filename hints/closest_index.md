the simplest way is probably to iterate over the +means+, remembering the best index.

```python
closest_distance = float('inf')  # this is infinity in Python
for i in range(len(means)):
    squared_distance_i = squared_distance(p, means[i])
    if squared_distance_i < closest_distance
        best = i
        closest_distance = squared_distance_i
```

a slight improvement is to use `enumerate`

```python
for i, mean in enumerate(means):
```

the slickest way is to use `min` and specify a `key` argument, which is
the function we want to "min by".  here we'd need to `min` over the indexes
and use a `key` function that takes an index and returns the squared distance
from `p` to the mean at the index.
