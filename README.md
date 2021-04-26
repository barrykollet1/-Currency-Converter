# Description
At this stage, you need to specify what currency you want to exchange. Imagine that you came to the bank with some money in your pocket. You want to choose the best currency to exchange your money for. First, read the currency to exchange, then read the currency you might exchange your money for and the amount of money you want to exchange. Notice that the input number can have a fractional part!

*There is a different amount of currencies in different tests. Checking if input is empty might be really useful.*

Parse the data from [FloatRates](http://www.floatrates.com/json-feeds.html). You can store it in any collection you want. It's called caching – a simple way to speed up the program. If we need to exchange the same currencies that we have already changed, we won't need to connect to the Internet, we only need to refer to the data in our cache.

*The very first currency is the one you want to exchange.*

Check the cache — the required currency might be already in there, print the result afterward. Output the amount of money that the bank employee should give you.

# Objectives
You're in the bank. Think about how much and what kind of currency you have.

1. Take the currency code, the amount of money the user has, and the currency code that the user wants to receive as the user input.
2. Retrieve the data from FloatRates as in the previous exercises.
3. Save the exchange rates for USD and EUR.
4. Read the currency to exchange for and the amount of money.
5. Take a look at the cache. Maybe you already have what you need?
6. If you have the currency in your cache, calculate the amount.
7. If not, get it from the site, and calculate the amount.
8. Save all the information to your cache.
9. Print the results.
10. Repeat steps 4-9 until there is no currency left to process.
# Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

*Be aware that the dictionary elements are unordered.*

**Example 1:**

```
> ILS
> USD
> 45
Checking the cache...
Oh! It is in the cache!
You received 13.84 USD.
> RSD
> 57
Checking the cache...
Sorry, but it is not in the cache!
You received 1684.41 RSD.
> EUR
> 33
Checking the cache...
Oh! It is in the cache!
You received 8.38 EUR.
```

**Example 2:**
```
> USD
> EUR
> 20
Checking the cache...
Oh! It is in the cache!
You received 16.52 EUR.
> NOK
> 45
Checking the cache...
Sorry, but it is not in the cache!
You received 382.1 NOK.
> SEK
> 75
Checking the cache...
Sorry, but it is not in the cache!
You received 624.66 SEK.
> NOK
> 55
Checking the cache...
Oh! It is in the cache!
You received 467.02 NOK.
> ISK
> 91
Checking the cache...
Sorry, but it is not in the cache!
You received 11708.38 ISK.
```
