first, get the colors
=====================

a simple way is just to index into each pixel:

```python
red = pixels[0]
```

and so on  

a slightly slicker way is to use list unpacking:

```python
red, green, blue = pixels
```

next, rescale the colors
========================
I got into a big twitter argument about whether to divide by 255 or 256.
In the end, I decided 256 made more sense, although not everyone agreed with me.

