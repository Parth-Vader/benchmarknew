# Testing stability

## Used the total number of items scraped within 20 seconds.

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

### Per minute

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
	

## Making ITEMCOUNT = 1000

Here, I made `CLOSESPIDER_ITEMCOUNT = 1000` and calculated the exact time that the spider ran. By taking `ITEMCOUNT` and dividing it by the time taken, I obtain the average speed.

Statistics : 

### Per-minute estimate

	Population size:50

	Mean (μ): 3654.34
	Median: 3681.5
	Mode: No
	Lowest value: 3104
	Highest value: 4008
	Range: 904
	Interquartile range: 294.5
	First quartile: 3558.75
	Third quartile: 3853.25
	Variance (σ2): 54810.584400001
	Standard deviation (σ): 234.11660428086
	Quartile deviation: 147.25
	Mean absolute deviation (MAD): 187.9392

Another set

	Population size:50

	Mean (μ): 3830.74
	Median: 3891
	Mode: 3884
	Lowest value: 3151
	Highest value: 4082
	Range: 931
	Interquartile range: 232.5
	First quartile: 3710
	Third quartile: 3942.5
	Variance (σ2): 31212.5924
	Standard deviation (σ): 176.67085894397
	Quartile deviation: 116.25
	Mean absolute deviation (MAD): 137.9432

## Per Second data statistics 

	Population size:50

	Mean (μ): 64.72
	Median: 65
	Mode: 65
	Lowest value: 58
	Highest value: 68
	Range: 10
	Interquartile range: 2
	First quartile: 64
	Third quartile: 66
	Variance (σ2): 3.2815999999997
	Standard deviation (σ): 1.8115186998758
	Quartile deviation: 1
	Mean absolute deviation (MAD): 1.2032


Changed settings to 

	CLOSESPIDER_ITEMCOUNT = 1000
	RETRY_ENABLED = False
	COOKIES_ENABLED = False
	LOGSTATS_INTERVAL = 3
	LOG_LEVEL = 'INFO'
	MEMDEBUG_ENABLED = True
	CONCURRENT_REQUESTS = 100

Per second statistics :

	Population size:50

	Mean (μ): 63.88
	Median: 64
	Mode: 65
	Lowest value: 59
	Highest value: 65
	Range: 6
	Interquartile range: 2
	First quartile: 63
	Third quartile: 65
	Variance (σ2): 1.9456
	Standard deviation (σ): 1.394847661933
	Quartile deviation: 1
	Mean absolute deviation (MAD): 1.0576

One of the best results so far.

The speed of the spider varies as follows :


### Discarding first 300 items :


	Population size:20

	Mean (μ): 38.4301944725
	Median: 37.6511886284
	Mode: No
	Lowest value: 35.147985388
	Highest value: 46.2829296263
	Range: 11.1349442383
	Interquartile range: 3.249650584025
	First quartile: 35.94529021805
	Third quartile: 39.194940802075
	Variance (σ2): 10.478846228199
	Standard deviation (σ): 3.237104605693
	Quartile deviation: 1.6248252920125
	Mean absolute deviation (MAD): 2.35329736993