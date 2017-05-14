# New Benchmark

This is the new spider for the benchmark. I will be testing on this spider further.

Using the following settings:

	CLOSESPIDER_TIMEOUT = 20
	RETRY_ENABLED = False
	COOKIES_ENABLED = False
	LOGSTATS_INTERVAL = 3
	LOG_LEVEL = 'INFO'

The total number of requests for the site is `1191`. Since the spider was able to perform all the requests within `30 seconds`, I fixed the time to be `20 seconds`. I am calculating the average speed by taking the total number of items scraped and multiplying it by `60/20=3`.

### Statistics (per 20 second)

	Population size:50

	Mean (μ): 975.26
	Median: 971
	Mode: 1006
	Lowest value: 867
	Highest value: 1071
	Range: 204
	Interquartile range: 79.5
	First quartile: 933
	Third quartile: 1012.5
	Variance (σ2): 2470.8323999999
	Standard deviation (σ): 49.707468251762
	Quartile deviation: 39.75
	Mean absolute deviation (MAD): 41.9504

Multiplying this by `3`, the statistics are :

	Population size:50

	Mean (μ): 2925.78
	Median: 2913
	Mode: 3018
	Lowest value: 2601
	Highest value: 3213
	Range: 612
	Interquartile range: 238.5
	First quartile: 2799
	Third quartile: 3037.5
	Variance (σ2): 22237.4916
	Standard deviation (σ): 149.12240475529
	Quartile deviation: 119.25
	Mean absolute deviation (MAD): 125.8512