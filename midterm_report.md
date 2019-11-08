# Midterm Report

### Problem Statement
Can using relevant news articles make a significant addition to stock price prediction models?

### Dataset

Our dataset consists of news articles from the NY Times, stock data from Facebook, Netflix, Amazon, Google, and Apple, and stock index data for the Dow Jones Industrial Average and the S&P 500. All of our data ranges over the span of nearly three years, from January 1, 2017 to October 31, 2019, although our stock and index data does not include weekends or holidays, as the markets are closed on these days.

#### NY Times Articles
Our article data came from the NY Times Article Search API. For each day, we collected all news produced in the "Business Day", "U.S.", and "World" sections. So far, we have collected 51,253
news pieces from 2015 - 2019. We will continue to collect more years, but we are rate limited by the API. 

Surprisingly, this also included some articles from other sources such as the AP and Reuters. The news came in the form of articles, multimedia, and audio. However, we will just be using the metadata. It's impossible to determine if we are missing articles, but there were some columns that were missing values. Some of the missing data had reasonable interpretations such as an article not having a subtitle or otherwise could be placed in an "Other" category. 

For our primary data cleaning, we removed columns that weren't relevant or had a very large proportion of missing data. Additionally, we used one-hot encoding for several text columns (such as section, source, material type, and news desk) to make them more useful. This will also help us determine if we should filter the articles by the above categories later in the project. The API also provided keywords, from which we picked the 100 most common across all articles to encode as many-hot. 

##### Sentiment Analysis

![](Sentiment.png)

The metadata also included larger text blocks such as headlines and abstracts. Our first attempt at using this data was performing sentiment analysis. We used a library that gave a polarity and subjectivity score. As you can see in the graph on the left, the average sentiment does vary by day. We are also considering training our own sentiment analysis model that will be able to better learn how to read headlines and abstracts that may be more sensationalized than typical text. 

Each day has a varying number of articles (roughly 18 - 37). We have tried different methods of condensing the articles to features, such as taking the sum or mean across each day. We have also considered trying to pick the day's "top" news or looking at articles one by one. There are 1,765 days covered by these news articles. With the different encodings, we currently have 186 features.

#### Stock and Index Data
Our stock and index data is in the following format:

For each date, we have the open, close, high, low, and adjusted close prices, as well as the volume. For any of these columns, we can calculate the percent difference between the previous date and the current date to indicate whether a feature increased or decreased and by how much since the past day. For example, we computed Close_Diff, the percent difference between the closing price on the current date and the closing price on the previous date. This can be useful as a target variable rather than directly using price since it takes into account that changes in price are more or less significant depending on what the current price is. 

In all of our stock and index datasets, there are 713 dates present. We will continue to add to this as we get news data for more years. The only missing data are the days for which the markets were closed (weekends and holidays). 

Here is a visualization of our stock data, with each stock’s prices scaled by its mean. 

![](Stocks.png)


### Modeling
For our modeling, we plan to compare baseline models that do not incorporate news data with more advanced models that do incorporate news data. For training, validation, and testing purposes, our dataset can be split by taking the most recent 20% as testing and the least recent 70% as training, with the rest as validation. 

#### Baseline
We plan on using models that are trained without news data as our baseline models. If we can see a significant improvement after modeling with the news data as a feature, then we will have good evidence that news data can be used as a supplemental data source to usefully improve stock price prediction. 

Some simple methods we can use to produce baseline predictions include:
    - Predicting the previous day's price as the current day's price (last value prediction)
    - Using a moving average of prices for the past n days to predict the current day's price
    - Using a time series based linear regression without news data and with the previous n days as features

#### Advanced 
We plan on testing out several additional models that incorporate news data to compare to our baseline models. Besides working with more complex models, we will also be creating features that could be useful to these models. These features include:
Average news article sentiment of the past n days
The output of a model trained to predict an index’s movement from the past n days of news articles
Moving average of percent price change of the last n days

Models we plan to test include:
    - Linear regression
    - ARIMA
    - LSTM

Note: We can additionally train and test these models with and without news-related features and compare their performance to look for any significant performance increases after adding news-related features.

### Testing 
To test the effectiveness of our models, we plan on comparing the RMSE of our baseline models with the RMSE of our advanced models as they perform on our testing portion of our dataset.

### What Next?

Data collection has taken up the  majority of the time we have spent working on our project thus far. Now that we have collected an adequate amount of data, our next steps include actually developing models to evaluate whether news data can be used to supplement price-based stock price prediction models. 

Since our idea involves using business articles to predict stock trends, we hope to make the best use out of the news articles we have in our dataset. This means feature engineering will be a large part of what we do with respect to the news data. For example, we intend to create many-hot encodings for each article and evaluate the sentiment of different parts of each article (title, abstract, content, etc.). As mentioned earlier, to create a more comprehensive and accuraate representation of our news data, we might train our own sentiment analysis model if no positive results come out of using the sentiment analysis built into libraries we use. Lastly, we could consider using something similar to the USE NLP tool shown in class, and consider the stock movements of days with similar USE results on news as a feature in our price prediction model. 

When training our models, we should be careful of over- or underfitting by keeping track of training vs. validation accuracy. In the event that our model overfits, we intend on evaluating the complexity of our model and the number of features we trained on. Perhaps a bag of words encoding would result in too many features to be useful, and we'd be better off just using sentiment analysis. Perhaps we trained our model too long, or perhaps we needed a less complex model in general. In the event that our model underfits, we intend to employ a similar yet opposite strategy. Perhaps adding features would help, or simply getting more data (further back in time), or using a more complex model able to predict more complex relationships between independent and target variables. As we proceed, we need to ensure that we are aware of whether we are over- or underfitting, and take steps to prevent either situation. 
