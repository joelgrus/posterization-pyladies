from __future__ import division
from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np
import random

def rescale_pixel(rgb_pixel):
    """given a rgb pixel (red, green, blue), where each color
    is a number between 0 and 255, return the rescaled pixel
    with values between 0.0 and 1.0"""

    pass

def get_pixels(filename):
    """load the pixels from the given file.  if it's a jpg file,
    rescale their rgb coordinates to lie between 0 and 1"""
    
    pass

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
    
    pass

def closest_index(p, means):
    """given a point p and a list of 'means' (also points),
    return the index of the mean that is closest to p
    (i.e. has the smallest squared_distance)"""

    pass

def mean(ps):
    """given a list of points, return the single point
    whose first element is 
    the average of all the first elements,
    whose second element is 
    the average of all the second elements,
    and so on"""

    pass

def new_means(ps, old_means):
    """given a list of points and some cluster means,
    assign each point to its closest cluster,
    and then compute the means of the new clusters"""

    pass

def k_means(ps, k, num_iterations=10):
    """given a list of points, choose k means to start with,
    then compute new_means num_iteration times,
    returning the final means"""

    pass

def recolor(pixel, mean_colors):
    """return the element of mean_colors that's closest to pixel"""
    pass

def posterize(pixels, num_colors):
    """given a list of lists of pixels, 
    use k_means to find num_colors 'mean' colors
    and return a list of lists of recolored pixels"""

    pass

###############
#             #
# TESTS BELOW #
#             #
###############

import unittest

class TestRescalePixel(unittest.TestCase):
    """test that rescaling works correctly"""

    def test_000(self):
        pixel = [0, 0, 0]
        self.assertEqual(pixel, rescale_pixel(pixel))

    def test_255s(self):
        fraction = 255 / 256
        self.assertEqual([fraction, fraction, fraction],
                         rescale_pixel((255, 255, 255)))
                         
    def test_various(self):
        self.assertEqual([0.25, 0.5, 0.75],
                         rescale_pixel([64, 128, 192]))
                         
class TestGetPixels(unittest.TestCase):
    """tests that all values end up between 0 and 1"""
    
    def test_png(self):
        pixels = get_pixels("crayons.png")
        intensities = [intensity 
                       for row in pixels
                       for pixel in row
                       for intensity in pixel]
        
        max_intensity = max(intensities)
        min_intensity = min(intensities)
        
        self.assertLessEqual(max_intensity, 1)
        self.assertGreater(max_intensity, 0.9)
        
        self.assertGreaterEqual(min_intensity, 0)
        self.assertLess(min_intensity, 0.1)
        
    def test_jpg(self):
        pixels = get_pixels("bee.jpg")
        intensities = [intensity 
                       for row in pixels
                       for pixel in row
                       for intensity in pixel]
        
        max_intensity = max(intensities)
        min_intensity = min(intensities)
        
        self.assertLessEqual(max_intensity, 1)
        self.assertGreater(max_intensity, 0.9)
        
        self.assertGreaterEqual(min_intensity, 0)
        self.assertLess(min_intensity, 0.1)
        
class TestSquaredDistance(unittest.TestCase):

    def test_same_point_zero_distance(self):
        p = [1, 2, 3, 4, 5]
        self.assertEqual(squared_distance(p, p), 0)
        
    def test_distances(self):
        self.assertEqual(squared_distance([1, 2, 3], [1, 1, 1]), 
                         0 ** 2 + 1 ** 2 + 2 ** 2)
        self.assertEqual(squared_distance([10, 0, 10], [0, 10, 0]),
                         10 ** 2 + 10 ** 2 + 10 ** 2)
                         
class TestClosestIndex(unittest.TestCase):
    
    def test_exact_match(self):
        means = [[1,1,1], [2, 2, 2], [3, 3, 3]]
        self.assertEqual(closest_index([1,1,1], means), 0)
        self.assertEqual(closest_index([2,2,2], means), 1)
        self.assertEqual(closest_index([3,3,3], means), 2)
        
    def test_non_exact_match(self):
        means = [ [random.random() for _ in range(10)]
                  for _ in range(10)]
                  
        for _ in range(100):
            p = [random.random() for _ in range(10)]
            closest = float('inf')
            for i, mean in enumerate(means):
                d = squared_distance(p, mean)
                if d < closest:
                    result = i
                    closest = d
            self.assertEqual(closest_index(p, means), result)
            
class TestMean(unittest.TestCase):
    
    def test_concrete(self):
        ps = [[1,1,1], [1, 2, 3], [1, 4, 9]]
        result = [1, 7 / 3, 13 / 3]
        
        for x, y in zip(mean(ps), result):
            self.assertAlmostEqual(x, y)

    def test_random(self):
        ps = [[random.random() for _ in range(10)] for _ in range(100)]
        result = [0 for _ in range(10)]
        for p in ps:
            for k in range(10):
                result[k] += p[k] / 100
                
        for x, y in zip(mean(ps), result):
            self.assertAlmostEqual(x, y)
            
class TestNewMeans(unittest.TestCase):
    
    def test_new_means(self):
        
        old_means = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        
        points = [[1, 1, 2],       # closest to 0
                  [0, 0, 0],       # closest to 0
                  [0, 0, 1],       # closest to 0
                  [2, 2, 2],       # closest to 1
                  [1.5, 2.5, 2],   # closest to 1
                  [2.1, 2.2, 2.3], # closest to 1
                  [3, 3, 4],       # closest to 2
                  [10, 10, 10],    # closest to 2
                 ]
                 
        self.assertEqual(new_means(points, old_means),
                         [mean(points[:3]),
                          mean(points[3:6]),
                          mean(points[6:])])
                      
class TestRecolor(unittest.TestCase):
    
    def test_recolors(self):
        color_means = [[0,0,0], [0.5, 0.5, 0.5], [1,1,1]]
        self.assertEqual(recolor([0,0,0], color_means), [0,0,0])
        self.assertEqual(recolor([.1,.1,.1], color_means), [0,0,0])
        self.assertEqual(recolor([.9, 1, .9], color_means), [1,1,1])
        self.assertEqual(recolor([.4,.6,.4], color_means), [0.5,0.5,0.5])