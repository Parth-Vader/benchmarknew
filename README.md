# New Benchmark

This is the new spider for the benchmark. I will be testing on this spider further.

Using the following settings:

	CLOSESPIDER_TIMEOUT = 20
	RETRY_ENABLED = False
	COOKIES_ENABLED = False
	LOGSTATS_INTERVAL = 3
	LOG_LEVEL = 'INFO'

The total number of requests for the site is `1191`. Since the spider was able to perform all the requests within `30 seconds`, I fixed the time to be `20 seconds`. I am calculating the average speed by taking the total number of items scraped and multiplying it by `60/20=3`.