# Homework 5 - Advanced NumPy

## Deadline

The deadline for this homework is on **Monday, 17th of May (2021-05-17 00:00:00 UTC+2)**.

## New Homework System

In response to the feedback we got through the *Homework System Survey* on StudIP, it is now only necessary to **solve 2/3 of the subtasks** in a homework order to **pass** a homework. However, we still highly encourage you to try to solve all tasks whenever possible. Solving a problem on your own is the only way you can really know if you have understood a concept.

This change comes with a partly new set of commands that you can use:

* Run `pytest test_[FILE-TO-TEST].py` to see if you have passed a subtask (e.g. `pytest test_omitting_outliers.py`)
* Run `pytest` to see whether you have passed all subtasks - **this still works, but is not what determines the checkmark any more**
* Run `python pass_check.py` to check how many points you currently have (one subtask will usually give 10 points) - **this is what determines the checkmark now**

**The checkmark next to your commit on GitHub is still the deciding factor in whether you pass a homework or not.**

If you encounter any problems with the new homework system, first check the forum. If it seems to be an unknown issue, please write to [Martin](mailto:mpoemsl@uos.de) so that it can be fixed or make a public post in the forum if it is a question whose answer might be of interest to others. 

## This Homework

This homework is about working with more advanced NumPy concepts. You will solve three tasks, one each in the following files:

* Omitting Outliers: `omitting_outliers.py`
* Rigorous Ranking: `rigorous_ranking.py`
* Printing Primes: `printing_primes.py` 

Template function headers are given in the files. You may use the full functionality of NumPy, but **no other libraries**.

As always, you pass by pushing your solution to GitHub and having the green checkmark appear next to your commit. You can also ask our Telegram bot: `@uos_scipy_bot`. Running `python pass_check.py` on your own machine should also give the same result, but it's not what counts in the end!

### 1 Omitting Outliers

A common necessity in scientific programming is the removal of outliers, i.e. data points that were likely created by mistake. Write a function `remove_outliers` that takes in an n-dimensional (numeric) array `data` as a positional parameter, as well as keyword parameters `m` (default: `3`) and `replace` (default: `True`).

Your function should detect every value as an outlier that is further than `m * sigma` away from the mean of `data`, where `sigma` is the standard deviation of `data`.

 - If `replace` is `True`, the function should return an array of the same shape as `data`, where every outlier is replaced with the mean of the original input array.

 - If `replace` is `False`, the function should return a 1D array containing all values of the input array except for the outliers.

**Note:** For the purposes of this task, assume that mean and standard deviation may be calculated once in advance, even though at that point the outliers are still present in the dataset. There exist better methods for detecting outliers, but those are trickier to implement and beyond the scope of this task.

**Functions that may be helpful:** `np.mean`, `np.std`, `np.abs`, `np.ndarray.copy`

### 2 Rigorous Ranking

Write a function `compute_rank` that takes a numeric array `array` of any shape as input and computes the **rank** of each value.

The **rank** is an integer between 0 and `array.size - 1`. It signifies the position of each element in a *sorted* version of the array. For example: `[20, 30, -10]` should map to `[1, 2, 0]`.

In the test examples, there will be no arrays that include ties. However, a good stance to take would be to give the element that comes first in the original array the lower rank.

**Hint:** The solution to this assignment can potentially be very short, but that doesn't mean it's straightforward. This task will be easier if you have a good intuition for indexing with integer arrays. Additionally, it may be a good idea to think about 1D arrays first and then adapt your solution for more dimensions.

**Functions that may be helpful:** `np.argsort`, `np.arange`, `np.flatten`

### 3 Printing Primes

For this task, you are given two helper functions that are already implemented:

 - `is_prime(n)` will return True if `n` is a prime number, `False` otherwise
 - `pretty_print_bool_array(array)` will print a boolean array to the console such that `True` is printed as "x" and `False` is printed as "."

**Step 1:** Create a new function `is_prime_numpy`, that works just like `is_prime` but will accept an entire NumPy array as input and return the result element-wise.

**Step 2:** Write a function `print_primes(rows, cols)`. Internally, it should create a boolean array of shape `(rows, cols)`. This array should be `True` exactly where the index is a prime number.

How is this supposed to work with a 2D array, you ask? We have a row and a column index after all. What I mean is that you should imagine the values of the array being enumerated from top-left to bottom-right for this task, as in the example below:

| **0**  | **1**  | **2**  | **3**  | **4**  |
|:--:|:--:|:--:|:--:|:--:|
| **5**  | **6**  | **7**  | **8**  | **9**  |
| **10** | **11** | **12** | **13** | **14** |
| **15** | **16** | **17** | **18** | **19** |

It is up to you to find a suitable way to convert from `(row, col)` to this number.

`print_primes` should then print this boolean array using the given pretty-print function. There should be no return value.

**Functions that may be helpful:** `np.vectorize` and `np.indices` (only discussed in the Jupyter notebook)
