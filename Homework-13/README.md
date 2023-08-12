## Deadline

The deadline for this homework is on **Monday, 12th of July (2021-07-12 00:00:00 UTC+2)**.

## Web Scraping

In this assignment, you will scrape information from [books.toscrape.com](https://books.toscrape.com), which is a mock website specifically designed for web scraping. The end goal is to have a list of all books listed on the front page. Each book should be represented as a dictionary like the following example:

```Python
{
    "title": "A Light in the Attic",    # str
    "price": 51.77,                     # float
    "stock": 22                         # int
}
```

The title and price are directly available from the front page, the stock however is not.

There are three tasks in this assignment:

* **Scouting** in `quiz.py`
* **Scraping Title and Price** in `scraper.py`
* **Scraping Stock** in `scraper.py`


As always, you only need to solve 2 out of 3 tasks to pass this assignment. You may use any libraries you deem useful that have been covered in this course and that are listed in `requirements.txt`. If any process is taking longer than 10 seconds to execute, you are likely sending too many requests and you should stop it with `Ctrl + C`.  

Don't forget to activate your environment before working on this assignment. You should be able to install all required libraries with `pip install -r requirements.txt`. If that does not work, a good first troubleshooting step is always to update `pip`, `wheel`, and `setuptools` with `pip install --upgrade pip wheel setuptools`. For this homework, the documentations of [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [MechanicalSoup](https://mechanicalsoup.readthedocs.io/en/stable/) might be useful.

### 1 Scouting

The most important step with web scraping is locating the information you are looking for, as well as finding a convenient way to get there. For that, the developer tools of modern browsers are incredibly helpful. Use them to answer the following questions. The answers should be filled into the global variables in `quiz.py`.

1. `PRODUCT_CARD_CLASS_NAME`: On the front page, superficially, each book is contained in what's called a *product card*. Under the hood, each product card is represented by an `<article>` tag. What is the **class name** of that tag?

2. `TITLE_ATTRIBUTE_NAME`: Inside such an `<article>` on the front page, what is the name of an **attribute** that contains the title of the book we are looking for? There are two correct answers.

3. `PRICE_CLASS_NAME`: What is the class of the tag that directly contains the price information?

4. `STOCK_TAG_NAME`: On the individual product pages, what is the name of the tag that contains the number of items stocked? Do *not* include angle brackets in the answer string. (EDIT: When writing this question I didn't see that the stock information occurs twice - this question is refering to the second occurence.)

5. `ROW_NUMBER`: On the individual product pages, the number of items in stock is contained within a row of a table (`<tr>`) - which? Start counting at 0.


### 2 Scraping title and price

Not it's time to write the web scraper. In this task, you will collect the two bits of information that are available directly from the front page: title and price.

Write a function `scrape_books()` that returns a `list` of all books listed on **THE FIRST PAGE** of [books.toscrape.com](https://books.toscrape.com). Each book should be represented as a `dict` as described above, except that the stock information does not need to be present for this task. You may completely omit the `"stock"` key for now or fill it with a placeholder like `None`.

Besides `bs4` functions, you will also need to utilize some string manipulation functions (e.g. `str.split`).


### 3 Scraping stock

Finally, extend the functionality of `scrape_books()` such that the stock information is now present.

For that, you will need to open each individual product page of the books listed on the front page. This task is marginally more convenient if you use Mechanicalsoup's `StatefulBrowser`, but also entirely possible using BS4 and requests. Specifically, the method [`StatefuleBrowser.download_link`](https://mechanicalsoup.readthedocs.io/en/stable/mechanicalsoup.html#mechanicalsoup.StatefulBrowser.download_link) may be helpful, as it avoids having to re-load the original page every time.

> Good luck with your final homework!

