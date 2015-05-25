flattening the pixels
=====================

the input pixels are in a grid:

```python
pixels[0]       # first row
pixels[0][0]    # first pixel
```

if we want to feed them to `k_means` we need them in a single list.  as always,
the simple way is with a `for` loop

```python
pixel_list = []
for row in pixels:
    pixel_list.extend(row)
```

while the slicker way is with a list comprehension:

```python
pixel_list = [pixel for row in pixels for pixel in row]
```

getting the colors
==================

is as simple as running `k_means` on the pixel list

recoloring one pixel
====================

if `mean_colors` is the output of the clustering, then we want to assign every
pixel the closest one of those, which is just

```python
mean_colors[closest_index(pixel, mean_colors)]
```

recoloring the pixels
=====================

again, we can use a couple of `for` loops or nested list comprehensions:

```python
recolored = []
for row in pixels:
    recolored_row = [ mean_colors[closest_index(pixel, mean_colors)]
                      for pixel in row ]
    recolored.append(row)
```

or

```python
recolored = [[mean_colors[closest_index(pixel, mean_colors)] for pixel in row ]
             for row in pixels ]