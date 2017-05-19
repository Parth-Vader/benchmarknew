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

## The speed of the spider varies as follows :

![Spider 1](https://raw.githubusercontent.com/Parth-Vader/benchmarknew/master/stability/Page-Shot-2017-5-17%20Online%20Graph%20Maker%20%C2%B7%20Plotly(1).png?token=APhACHm3y1vw0l7QEmUcyWkbuWbydBJoks5ZJXoRwA%3D%3D)
![Spider 2](https://raw.githubusercontent.com/Parth-Vader/benchmarknew/master/stability/Page-Shot-2017-5-17%20Online%20Graph%20Maker%20%C2%B7%20Plotly.png?token=APhACMS4wmXftozNxlzluo9Dkm8hvuv_ks5ZJXoUwA%3D%3D)
![Spider 3](https://raw.githubusercontent.com/Parth-Vader/benchmarknew/master/stability/Screenshot-2017-5-17%20Online%20Graph%20Maker%20%C2%B7%20Plotly.png?token=APhACP8kfEr5K7ZXxC9Ri5v6pzUJLQsVks5ZJXoXwA%3D%3D)

We can observe that the speed stabilises after around 300 items, so I would now be discarding the first 300 items.
### Discarding first 300 items :
	
When CONCURRENT_REQUESTS = 10 :

	Population size:50

	Mean (μ): 57.914509901472
	Median: 57.49577374755
	Mode: No
	Lowest value: 48.3399842982
	Highest value: 66.6062245625
	Range: 18.2662402643
	Interquartile range: 7.20653028805
	First quartile: 54.612051058325
	Third quartile: 61.818581346375
	Variance (σ2): 18.473481862359
	Standard deviation (σ): 4.2980788571592
	Quartile deviation: 3.603265144025
	Mean absolute deviation (MAD): 3.6365766199846

When CONCURRENT_REQUESTS = 100 :

	Population size:20

	Mean (μ): 58.068316935185
	Median: 58.89404859485
	Mode: No
	Lowest value: 50.2820789954
	Highest value: 66.6083017011
	Range: 16.3262227057
	Interquartile range: 4.901280544625
	First quartile: 55.180792304725
	Third quartile: 60.08207284935
	Variance (σ2): 13.726370736525
	Standard deviation (σ): 3.7049117042819
	Quartile deviation: 2.4506402723125
	Mean absolute deviation (MAD): 2.898659479338

Histogram : 

![Histogram](https://raw.githubusercontent.com/Parth-Vader/benchmarknew/master/stability/Page-Shot-2017-5-19%20Histogram%20Maker%20%C2%B7%20Plotly%20Online%20Chart%20Editor.png?token=APhACN1g6il9tOz1iImwk2ZHTiigI9bZks5ZJ9xkwA%3D%3D)

When CONCURRENT_REQUESTS = 120 :

	
	Population size:20

	Mean (μ): 64.629335444995
	Median: 65.1046648778
	Mode: No
	Lowest value: 58.6573798789
	Highest value: 67.5569293799
	Range: 8.899549501
	Interquartile range: 2.640101009925
	First quartile: 63.9208027457
	Third quartile: 66.560903755625
	Variance (σ2): 5.91760829821
	Standard deviation (σ): 2.4326134707779
	Quartile deviation: 1.3200505049625
	Mean absolute deviation (MAD): 1.849888751116

