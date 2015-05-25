choosing the initial means
==========================

one way is to just pick the first `k` elements:

```python
means = ps[:k]
```

another option is to choose `k` random elements:

```python
means = random.sample(ps, k)
```

iterating
=========

use a `for` loop, it might be helpful to print something out at each iteration
so you can watch the progress.  at each step you simply need to call

```python
means = new_means(ps, means)
```

