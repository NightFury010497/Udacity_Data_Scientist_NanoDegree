# Starbucks Capstone Challenge  
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
![image](https://user-images.githubusercontent.com/56355704/83692361-73762980-a611-11ea-83b6-62373fdf1b7e.png)  

### Customer Subsriptions by Month and Year  
![image](https://user-images.githubusercontent.com/56355704/83692273-4de92000-a611-11ea-9f6f-1b74984f900f.png)  


