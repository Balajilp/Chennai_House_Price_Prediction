# CHENNAI HOUSE PRICE PREDICTION

![8ea777e7-fdb4-4541-9acb-8c5ef7d61bec_FABaqL6V](https://user-images.githubusercontent.com/88379464/159073263-80867a63-28c2-4232-9b68-3a79705dabdd.gif)



### Problem Statement
Real estate transactions are quite opaque sometimes and it may be difficult for a newbie to know the fair price of any given home. Thus, multiple real estate websites have the functionality to predict the prices of houses given different features regarding it. Such forecasting models will help buyers to identify a fair price for the home and also give insights to sellers as to how to build homes that fetch them more money. Chennai house sale price data is shared here and the participants are expected to build a sale price prediction model that will aid the customers to find a fair price for their homes and also help the sellers understand what factors are fetching more money for the houses?

### PROJECT FLOW
1. Data collection
2. Format the Raw Data
3. Exploratory Data Analysis
4. Feature Engineering
5. Feature Selection
6. Model Building
7. Model Evaluation
8. Create a Flask web application

### Data Collection and Formating:
    Data is collected from kaggle website.  Data contains 7109 records,  All the columns are not in the proper format.  For example Location feature in that many feature are having the spelling mistake.  so many location or repeated example adayar adyar like that.
    
 ### Exploratory Data Analysis
 #### Univariate Analysis
 Loading the data into pandas dataframe and separate the data into Numerical Coninuous, Numerical Discrete, Categorical, TimeStamp, Temporal likewise separated the data fro better analysis.  Then Take the categorical feature and plot using Seaborn bar plot count plots, and find out the distribution of the numerical feature and independent feature and dependent feature relation all these are performed in univariate analysis itself.
 
 #### Bivariate Analysis
 In bivariate analysis take the 2 independet feature and anlyse the distribution of the feature using scatter plots and 3 dimensional plot to how the distribution and relation ship with target all these things are done on bivariate analysis
 
 #### Multivariate Analysis
 We cannot plot the data more than 3 dimensional, because human mind can't able to see that.  for that Seaborn provides pair plot using that plot performed multivariate analysis.  
 
 #### Bucket analysis
 Based on the problem statement performed some extra analysis for that extracted new feature from the existing feature and numerical features also put it into separatet bucket for range of values then performed analysis using bar plots.
 
 ### FEATURE ENGINEERING
 Once i get the exact knowledge about the data and how the distribution or happened what is the relationship with target this all things done.  Now i moved to feature engineering.  In feature engineering we need to handle the missing values.  There is many ways missing values can occur.  We need to check why the values are missing once we get idea about the missing values we can fill theat mmissing values with meaning full values.  But in our case there are very less number of missing values prersent over there.  This al missing values Are completely randomly occured.  So we can fill that using random value imputation and model methods.  After filling the missing values we need to have a look on to the variance of the data is therre any change in the variance for that we need to use kernel density estimator   In our Data is ver less number of missing values present so we cannot have more variance vfariance is eactly equal to the previous variance.
 
 #### Outliers handing 
 Here e try to use linear regression model which is quite sentive to outliers so we can nicely remove the outliers.  We can fill the outliers value with something meaningfull also but in our data we have enough amout of data and very less number of outliers present so we can safely removed it.
 
 ####  Tramsformations
 Transformation We tried with linear regression which is not good in our model xgboost is performed well in our data also all the features are approximately good relatinship with the target,  So we don't want to do any transformation.  But if we use linear regression kind of algorithms definetly we need to do transformation like boxcox, sin, cos, sqrt, exponential like that..   After that we need to scale the data also.
 
 ### FEATURE SELECTION
 30% OF the feature selection done on the eda itself.  Now we need to perform feature selection for remainig features.  For that we used correlation and Mutual information gain regressor, correlation graph is for linear relationship with target, mutual informatin gian is for non linear properties.  After that we need to perform the Chi square test also for feature selection of categorical features chi square test is only give the signifiace of the feature only it doesn't give us how much important that feature is or what is the strengh of the significance.  Fore that we need to use Crammer V Test.
 
 ### Model Selection
 Now we need to select the right model for our data.  If we try with all the data time complexity is high.  so what we will don is we used T-SNE  dimentionality reduction techniques to reduce the number of dimention to plot the data.  here we reduce the dimention 10 to 2  Now we can approximately preserve 30 to 40 percent of the information from the original data.  we plot it and have a look on to the plots.  There is heavy non linear property over there.  So we can go ahead with RANDOM FOREST REGRESSOR OR XTREAME GRADIENT BOOSTING MODELS.    But in our cse this not production this project is for our practice only.  So we can try linear regression kind of algorithms also.
 
 
 ### model building
 We tried with different different regression model out of that xgboost will give us good R2 value.  Now we need to use xgboost to build our model.  
 
 ### model Evaluation
 We evaluate our model with testing data for that we used R2 and adjusted R2 now our accuracy also is fine which is somewhere around 89 %.
 
 ### Creating a Flask web application
 Now we need to create a Flask web application.  In order to get a more interactive web app we can use HTML, CSS also.  Now our model is Ready.
 
 
 
 



