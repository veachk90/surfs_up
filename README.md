# surfs_up

#### Overview
The purpose of this analysis was to use the available data for the weather at and around Oahu in order to finally determine whether it would be a location to open a surf shop that sells ice cream. The weather had been gathered by multiple weather stations around the island, which generally served to improve the quality and volume of the data. In order to develop a sense of the range of the temperatures and weather patterns around Oahu, data from June and December of the same year were analyzed. 

#### Methods
The raw weather data had previously been provided in a SQLite file. The first step, then, was to first look at the relevant data and disseminate any findings with both colleagues and shareholders. Since they may not be familiar with navigating Github, I decided to use Python to conduct my initial analysis. Once this was done, I could then use Flask to display the data in a URL on a server I hosted that could easily be shared during the next meeting. The SQLalchemy package allowed me to easily access and manipulate the raw data, which in turn allowed me to use Pandas to create dataframes and matplotlib to graph the initial results. The method for the next analysis of the island's temperature throughout the year was similar, though I judged that it would be more useful to use summary statistics instead of graphs as the results. This is because summary statistics are able to convey a lot of information about a dataset's behavior in a very condensed format. 

#### Results
Perhaps underwhelmingly, the analysis shows that there is generally little variation in the temperatures between June and December. 

![Summary Statistics for June](https://github.com/veachk90/surfs_up/blob/main/June_Temps_Summary.png) ![Summary Statistics for December](https://github.com/veachk90/surfs_up/blob/main/December_Temps_Summary.png)

There are three key differences between the temperature in June and the temperature in December:
1. June's temperature is greater than December's in the minimum recorded temperature, the mean temperature, and the maximum recorded temperature, with the mean being nearly four degrees warmer.
2. There were almost 200 more obersvations made in June than were made in December. It is possible that this is a source of bias in the data. As data analysts, we almost always wish that we had more data of higher quality, but we often must make do with what we have.
3. The greatest difference in temperatures between June and December appear in the minimum recorded temperatures, with June at 64 degrees and December at 56 degrees. Further analysis could show that this difference correlates with a difference in customer traffic through the surf shop, and could have an affect on ice cream sales.

Thus, even though the differences in temperatures between June and December appear to be minor, it may be the case that the surfing community could be sensitive to these differences, and that customer traffic may be greater in one time of the year over the other. The original vision is to have a surf shop that sells ice cream, but it could be worth while to have some hot food to sell as well on the cooler December days in order to draw customers. Of course, it remains to be seen how much the temperature differences affect the waves, which is the main attraction for drawing crowds!
