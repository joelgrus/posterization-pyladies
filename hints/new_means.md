we need to do two things here:

assign each point to a cluster
==============================

this part is pretty easy, each input `p` belongs to the cluster

```python
closest_index(p, old_means)
```

compute the means of the new clusters
=====================================

there are several ways to do this.  one way is to actually create the clusters:

```python
clusters = [ []  # empty lists, one for each mean
             for _ in old_means ]
for p in ps:
    clusters[closest_index(p, old_means)].append(p)
```

then you can simply

```python
return [mean(cluster) for cluster in clusters]
```

