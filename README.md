#Twitter Covid Analysis Project 
This project was completed with three main objectives:

a) work with large scale datasets
b) work with multilingual text
c) use the MapReduce divide and conquer strategy to create parallel code

## The Project

**Background Info:**

This project used the dataset of all geotagged tweets sent each day. These account for a total of 2% of tweets. Whether this data is structurally different than non-geotagged tweets was outside of the scope of this project. It is possible that non-geotagged tweets have differing rates of mentions of coronavirus or coronavirus adjacent words.

**Mapping the Data**

The data had already been partitioned into a file for each day, and within that file all the tweets from each hour. We then used a mapping function to record the data from each day in JSON format.

Two parallel maps were completed, one mapping the mentions of a hashtag per language each day, and one per geotagged country per day.

**Reducing the Data**

The files for each day were then combined, creating one file with country data for 2020 and one for language data for 2020. 

**Visualizing the Data**
The reduced data was formatted onto a bar chart, illustrating the top 10 countries or languages for each hashtag. The two hashtags were `#coronavirus` and `#코로나바이러스`

Below is the bar graph for `#코로나바이러스` by country.

<img src=코로나바이러스_country.png width=100% />

Below is the bar graph for `#코로나바이러스` by language.

<img src=코로나바이러스_lang.png width=100% />

Below is the bar graph for `#coronavirus` by language

<img src=coronavirus_lang.png width=100% />

Below is the bar graph for `#coronavirus` by country

<img src=coronavirus_country.png width=100% />


**Comparing Hashtags**
For a direct method to compare hashtags, I created `alternative_reduce.py`, which combined reducing and visualizing into one file. This program was built to allow for the comparison of hashtag use for multiple hashtags throughout 2020. I created the graphic below using this method

<img src=covid19_coronavirus_covid-19.png width=100% />
