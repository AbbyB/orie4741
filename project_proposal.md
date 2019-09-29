# Using News to Predict Stock Performance

### Introduction 
Stock prediction is one of the most widely demanded services today, and with more data available now than ever before, there are new approaches to stock prediction that deserve exploration. We plan to use a combination of news articles, traditional quantitative stock prediction methods, and categorization of stocks into different types based on their fundamentals to develop an effective stock prediction model. News articles reach hundreds of millions of people each day, so it would make sense that they have the power to influence people's choices, including whether they buy or sell stocks. Even if the news on a certain day has a small causal effect on the stock market, its effect should precede any resulting movement in the stock market, making it a good feature to use in stock prediction. Finding correlation between news and stock movement could be a valuable tool in making sound investment decisions. Even if the news can't reliably predict the stock market, perhaps it could serve as a filter to weed out bad investment decisions. Either way, we hope that this project will allow us to gain insight into how alternative data sources like the news can help offer information on the stock market. 

### Question
Can news articles that mention a stock provide information that can be used to predict the future performance of that stock? 

### Data
Kaggle has a dataset on using news to predict stock movement [here](https://www.kaggle.com/c/two-sigma-financial-news). We plan to make use of this, but narrow down our focus to a few stocks in different categories so we can analyze their fundamentals in combination with the news. For this, Kaggle also has several datasets on historical stock prices that we can use. For example, [this dataset](https://www.kaggle.com/ehallmar/daily-historical-stock-prices-1970-2018) contains historical daily stock data from 1970 to 2018. If we want more recent data on particular stocks, we can find current data on Yahoo Finance (e.g. [Apple stock data](https://finance.yahoo.com/quote/AAPL/history/)). For additional and current news data, we can scrape archives from the Wall Street Journal, the New York Times, and more. Most news sites keep easily accessible archives. 


