**A cli cron parser**
-----------------------


Example `config.txt`

```text

30 1 /bin/run_me_daily
45 * /bin/run_me_hourly
* * /bin/run_me_every_minute
* 19 /bin/run_me_sixty_times
```

Expected Output
```
1:30 tomorrow - /bin/run_me_daily
16:45 today - /bin/run_me_hourly
16:10 today - /bin/run_me_every_minute
19:00 today - /bin/run_me_sixty_times
```


To run

Using `python 2.7+, 3.0+`

```
python parser.py 16:45 < config.txt

``` 
