# Starbucks Capstone Challenge [BLOG](https://medium.com/@nightfury010497/starbucks-capstone-challenge-udacity-data-scientist-nanodegree-e2d33956f0d1?sk=a8b4819bcd352b383592710ab218c980)

## Data Sets  
The data is contained in three files:  
  
portfolio.json - containing offer ids and meta data about each offer (duration, type, etc.)  
profile.json - demographic data for each customer  
transcript.json - records for transactions, offers received, offers viewed, and offers completed  
Here is the schema and explanation of each variable in the files:  
### portfolio.json  
  
id (string) - offer id  
offer_type (string) - type of offer ie BOGO, discount, informational  
difficulty (int) - minimum required spend to complete an offer  
reward (int) - reward given for completing an offer  
duration (int) - time for offer to be open, in days  
channels (list of strings)  
### profile.json  
  
age (int) - age of the customer  
became_member_on (int) - date when customer created an app account  
gender (str) - gender of the customer (note some entries contain 'O' for other rather than M or F)  
id (str) - customer id  
income (float) - customer's income  
### transcript.json  
  
event (str) - record description (ie transaction, offer received, offer viewed, etc.)  
person (str) - customer id  
time (int) - time in hours since start of test. The data begins at time t=0  
value - (dict of strings) - either an offer id or transaction amount depending on the record  
  

### Number of Sign up Per DAY  
I was wondering how many Sign up’s must be there on Starbucks Application since years  
![image](https://user-images.githubusercontent.com/56355704/83692361-73762980-a611-11ea-83b6-62373fdf1b7e.png)  

### Customer Subsriptions by Month and Year  
How about we find out the number of Subscriptions as per Customer there are Per Month and Per Year?
![image](https://user-images.githubusercontent.com/56355704/83692273-4de92000-a611-11ea-9f6f-1b74984f900f.png)  

### Age Group Analysis  
What is the age group that prefers to buy Starbuck Coffee?!  
![image](https://user-images.githubusercontent.com/56355704/83928931-1e701a00-a7af-11ea-8b9f-3475d8c6a458.png)
### Gender Analysis  
This might be sexist but how about we explore our data more and let’s find out which GENDER prefers to buy more coffee??
![image](https://user-images.githubusercontent.com/56355704/83928954-2cbe3600-a7af-11ea-92c8-a301439a4e27.png)
  
### Future Work:  
Customer Lifetime Value  
In which we can do an Estimation of calculating the customer value or customer retention which helps a business to run in a much better way!  
I am linking a Customer Lifetime Value BLOG which I really found intriguing and I would like others to EXPLORE as well!  
https://blog.kissmetrics.com/wp-content/uploads/2011/08/calculating-ltv.pdf  
