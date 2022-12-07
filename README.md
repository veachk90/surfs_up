# surfs_up

#### Overview
The purpose of this analysis was to use the available data for the weather at and around Oahu in order to finally determine whether it would be a location to open a surf shop that sells ice cream. The weather had been gathered by multiple weather stations around the island, which generally served to improve the quality and volume of the data. In order to develop a sense of the range of the temperatures and weather patterns around Oahu, data from June and December of the same year were analyzed. 

#### Methods
The raw weather data had previously been provided in a SQLite file. The first step, then, was to first look at the relevant data and disseminate any findings with both colleagues and shareholders. Since they may not be familiar with navigating Github, I decided to use Python to conduct my initial analysis. Once this was done, I could then use Flask to display the data in a URL on a server I hosted that could easily be shared during the next meeting. The SQLalchemy package allowed me to easily access and manipulate the raw data, which in turn allowed me to use Pandas to create dataframes and matplotlib to graph the initial results. The method for the next analysis of the island's temperature throughout the year was similar, though I judged that it would be more useful to use summary statistics instead of graphs as the results. This is because summary statistics are able to convey a lot of information about a dataset's behavior in a very condensed format. 

The purpose of the analysis is well defined. (3 pt)
Results:

#### Results
Perhaps underwhelmingly, the analysis shows that there is generally little variation in the temperatures between June and December. 

![Summary Statistics for June](https://github.com/veachk90/surfs_up/blob/main/June_Temps_Summary.png) ![Summary Statistics for December](

There is a bulleted list that addresses the three key differences in weather between June and December. (6 pt)
Summary:

There is a high-level summary of the results and there are two additional queries to perform to gather more weather data for June and December. (5 pt)
