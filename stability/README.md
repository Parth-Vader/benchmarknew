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

