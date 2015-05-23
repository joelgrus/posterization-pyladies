from __future__ import division
from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np
import random

def rescale_pixel(rgb_pixel):
    """given a rgb pixel (red, green, blue), where each color
    is a number between 0 and 255, return the rescaled pixel
    with values between 0.0 and 1.0"""

    red, green, blue = rgb_pixel
    return [red / 255.0, green / 255.0, blue / 255.0]

def get_pixels(filename):
    """load the pixels from the given file.  if it's a jpg file,
    rescale their rgb coordinates to lie between 0 and 1"""
    
    pixels = imread(filename)
    
    if filename.endswith(".jpg"):
        pixels = [[rescale_pixel(pixel) for pixel in row]
                  for row in pixels]
                  
    return pixels

def show_pixels(pixels):
    """display the pixels"""
    plt.imshow(pixels)
    plt.show()

def save_pixels(pixels, output_filename):
    """save the pixels"""
    plt.imsave(arr=np.array(pixels), fname=output_filename)
    

def squared_distance(p, q):
    """given points p and q (represented as Python lists)
    return the sum of the squares of the differences
    of corresponding elements: p[0] and q[0], p[1] and q[1],
    and so on"""
    
    return sum((p_i - q_i) ** 2 for p_i, q_i in zip(p, q))
    
def closest_index(p, means):
    """given a point p and a list of 'means' (also points),
    return the index of the mean that is closest to p
    (i.e. has the smallest squared_distance)"""

    return min(range(len(means)),
               key=lambda i: squared_distance(p, means[i]))
               
def mean(ps):
    """given a list of points, return the single point
    whose first element is 
    the average of all the first elements,
    whose second element is 
    the average of all the second elements,
    and so on"""

    n = len(ps)
    k = len(ps[0])
    return [sum(p[i] for p in ps) / n
            for i in range(k)]

def new_means(ps, old_means):
    """given a list of points and some cluster means,
    assign each point to its closest cluster,
    and then compute the means of the new clusters"""

    num_means = len(old_means)
    indexes = [closest_index(p, old_means) for p in ps]
    
    return [mean([p for p, i in zip(ps, indexes) if i == j])
            for j in range(num_means)]
            
def k_means(ps, k, num_iterations=10):
    """given a list of points, choose k means to start with,
    then compute new_means num_iteration times,
    returning the final means"""

    means = random.sample(ps, k)
    
    for i in range(num_iterations):
        print i, means
        means = new_means(ps, means)
        
    return means
    
def posterize(pixels, num_colors):
    """given a list of lists of pixels, 
    use k_means to find num_colors 'mean' colors
    and return a list of lists of recolored pixels"""

    flattened = [pixel for row in pixels for pixel in row]
    mean_colors = k_means(flattened, num_colors)
    
    return [[mean_colors[closest_index(pixel, mean_colors)] for pixel in row]
            for row in pixels]
            
