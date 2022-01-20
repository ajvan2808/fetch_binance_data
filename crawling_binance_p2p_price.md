## Project 1: Fetch USDT/VND price on Binance P2P ##

### Description:
1. Research api from Google, stackoverflow, reddit where we can get p2p price data.
2. Store data in database (MySQL, postgres)
3. Run this script hourly (cronjob)
4. Display USDT/VND chart

> What is Postman?
> Postman is an API client that makes it easy for developers to create, share, test and document APIs. 
> This is done by allowing users to create and save simple and complex HTTP/s requests, as well as read their responses. 
> The result - more efficient and less tedious work.

#### 1. API Testing with Postman
- Go to p2p.binance.com and inspect sources (reload if not show)
- Go to Network -> search 
- Open Postman and copy, paste URL and payload then send POST request. 

#### 2. Python Logging Module <https://docs.python.org/3/library/logging.html>
- A good convention to use when naming loggers is to use a module-level logger, in each module which uses logging, named as follows:
```python
logger = logging.getLogger(__name__)
```

- Logging Levels

| Level    | Numeric value |
|----------|:-------------:|
| CRITICAL |      50       |
| ERROR    |      40       |
| WARNING  |      30       |
| INFO     |      20       |
| DEBUG    |      10       |
| NOTSET   |       0       |





