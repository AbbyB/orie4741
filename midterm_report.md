# Midterm Report

### Problem Statement
Can using relevant news articles make a significant addition to stock price prediction models?

### Dataset

Our dataset consists of news articles from the NY Times, stock data from Facebook, Netflix, Amazon, Google, and Apple, and stock index data for the Dow Jones Industrial Average and the S&P 500. All of our data ranges over the span of nearly three years, from January 1, 2017 to October 31, 2019, although our stock and index data does not include weekends or holidays, as the markets are closed on these days.

#### NY Times Articles

#### Stock and Index Data

### Modeling

#### Baseline
We plan on using models that are trained without news data as our baseline models. If we can see a significant improvement after modeling with the news data as a feature, then we will have good evidence that news data can be used as a supplemental data source to usefully improve stock price prediction. 

Some simple methods we can use to produce baseline predictions include:
    - Predicting the previous day's price as the current day's price (last value prediction)
    - Using a moving average of prices for the past n days to predict the current day's price
    - Using a time series based linear regression without news data and with the previous n days as features

#### Advanced 


### Testing 
To test our models, we plan on comparing the RMSE of our baseline models with the RMSE of our advanced models. 

### What Next?



By this time, you should have made some progress in cleaning up and understanding your data, and in running a few preliminary analyses. Your project midterm report should be no more than 3 pages, written in LaTeX or markdown, and posted in your project repository with the filename “midterm_report”. (The file extension should be either .tex + .pdf, or just .md.)

In the report, you should describe your data set in greater detail. Describe how you plan to avoid over (and under-)fitting, and how you will test the effectiveness of the models you develop. Include a few histograms or other descriptive statistics about the data. How many features and examples are present? How much data is missing or corrupted? How can you tell? You should also run a few preliminary analyses on the data, including perhaps some regressions or other supervised models, describing how you chose which features (and transformations) to use. Finally, explain what remains to be done, and how you plan to develop the project over the rest of the semester.