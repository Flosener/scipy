# Homework 06 - Pandas

### Deadline: Monday, 24th of May at 00:00 (2021-05-24 00:00:00 UTC+2)

This week's homework is about pandas.
Be sure to install pandas in your environment.

    conda install pandas
or

    pip install pandas

Only the ``pandas`` and ``numpy`` libraries are allowed for this homework. Like last week, you have to solve 2 out of 3 tasks in order to pass this homework - each task gives 10 points and you need at least 20 points to pass. As always, you can run ``pytest test_[FILE-TO-TEST].py`` to see if you have passed a task and ``python pass_check.py`` to see the overall status of this homework.  

There are three tasks this which, one each in the following files:

* Countries: ``countries.py``
* Pokemon: ``pokemon.py``
* Finding a Public Toilet in Australia: ``find_toilet.py``

**General Tip:** Before starting with each task take a few minutes to get familiar with the given dataset. Better to have an 
overview instead of blindly starting to mash some data together.

## 1. Countries

In the file ``countries.py`` write a function called ``aggregate_european_countries()`` which loads the ``countries.csv`` dataset into a dataframe.
From all **european** countries the function should find the country with maximum net migration **in** the EU and the one with maximum 
net migration **not in** the EU. Similarly, find the **european** countries with minimum population density in and outside of the EU.
The function should return a dataframe of the following form.

| in eu               | max net migration | max net migration country  | min pop density | min pop density country |
|---------------------|-------------------|----------------------------|-----------------|-------------------------|
| False               | some value        | some name                  | some value      | some name               |
| True                | some value        | some name                  | some value      | some name               |

One column for the maximum net migration values, followed by a column with the corresponding country name. Then two columns for the minimum population density in the same fashion.  

Note that **only the values of the dataframe and their shape** have to be correct, since index and column names might vary
depending on the methods you use.

**Hint:** The pandas methods ``groupby()`` and ``aggregate()`` are very useful for this task.

## 2. Pokemon

In the file ``pokemon.py`` write a function `most_common()` which takes an arbitrary subset of rows of the ``Pokemon_no_duplicates.csv``
dataset as dataframe as an argument. The function should compute the **most common** type combination of 
the given dataset. Then return the name of the Pokemon, which has the highest attack value amongst 
Pokemons with the most common type combination.

**Reminder:** You only care about type combinations, i.e. Pokemons that have two types.

**Hint:** Depending on your approach you might need the pandas methods ``groupby()`` 
and `count()` or ``count_values()``.

## 3. Finding a Public Toilet in Australia

You are stranded somewhere on the continent of Australia and only have your location as a pair of 
coordinates. The water you brought is almost empty and your kid really needs a change of diapers. Therefore you decide to find the next public toilet with drinkable water and a babychange or a baby careroom. Luckily you have a dataset with all the public toilets in Australia, which you can use to find the closest public toilet fulfilling the above conditions.

-----------

In the file `find_toilet.py` write a function ``find_closest_toilet(lat, lon)`` which takes as arguments a pair
of coordinates in degrees. Load the datasets ``australian_toilets.csv``, containing all public toilets in Australia with information
about the longitude and latitude, the presence of drinkable water and baby care facilities amongst other tings.
The longitude and latitude are your current location. The function should find the public toilet, closest to your location
with drinkable water and a baby change or a baby care room. It should then return a series which contains 
the *FacilityID*, *name*, *longitude*, *latitude* and *distance to your location* of that particular facility.

For the calculation of the distance between two points given in longitude and latitude use the haversine formula.
It calculates the distance between two points on a sphere (technically the earth is not a perfect spere but it is good enough for us).
![](haversine.png)

![image](https://user-images.githubusercontent.com/49363779/118363570-4d813500-b595-11eb-8923-ffe0b5618a80.png)
are the latitudes in **radians** of point one and two. ![image](https://user-images.githubusercontent.com/49363779/118356698-cde46d80-b576-11eb-95e7-2996d66346c4.png) are the longitudes in **radians** of point one and two. You can convert from degrees to radians using ``np.radians`` or the formula: 

![image](https://user-images.githubusercontent.com/49363779/118363587-6853a980-b595-11eb-82ae-7a5deec21710.png)

*r* is the radius of the sphere, which is *6371km* for the earth.

**Hint:** You can compute the formula in a vectorized fashion, by piecing it together from functions like ``np.sin()`` and ``np.sqrt()``.
