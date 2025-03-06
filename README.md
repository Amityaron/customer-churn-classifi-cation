## Customer-Churn-Classification
Atidot - DS Assignment 
In this Assignment, I will present a robust classification model that predicts which customers will churn between
Jan. 1, 2024 and Feb. 28, 2024, using time-series data with a double index (customer_id and date).
Demonstrate modeling and feature engineering skills, as well as production-aware design practices.
The data set contains the following features :

1.customer_id
2.date from 1.1.2023 until the end of the year.
3.transaction_amount	
4.plan_type	(Basic, Strandrad, Premium) categorical feature 
5.churn	(1= The customer leaves the company, 0= The customer stays  the company)
6.issuing_date When the customer buys the insurance.

I start by filling NaN in the data set by the following role, replacing Nan for each customer by the mean of the transaction_amount with the same plan_type.

For example 

| customer_id | date                   | transaction_amount | plan_type | churn | issuing_date          |
|------------|------------------------|--------------------|-----------|-------|------------------------|
| CUST_1     | 2023-01-01 00:00:00     | 193.5246582        | Basic     | 0     | 2021-03-01 00:00:00     |
| CUST_1     | 2023-02-01 00:00:00     | 303.3426573        | Standard  | 0     | 2021-03-01 00:00:00     |
| CUST_1     | 2023-03-01 00:00:00     | 38.46096996        | Standard  | 0     | 2021-03-01 00:00:00     |
| CUST_1     | 2023-04-01 00:00:00     | 356.9555631        | Premium   | 0     | 2021-03-01 00:00:00     |
| CUST_1     | 2023-05-01 00:00:00     | 417.896894         | Standard  | 0     | 2021-03-01 00:00:00     |
| CUST_1     | 2023-06-01 00:00:00     | **NaN**            | Premium   | 0     | 2021-03-01 00:00:00     |
| CUST_1     | 2023-07-01 00:00:00     | 221.6530591        | Standard  | 0     | 2021-03-01 00:00:00     |
| CUST_1     | 2023-08-01 00:00:00     | 78.35199172        | Standard  | 0     | 2021-03-01 00:00:00     |
| CUST_1     | 2023-09-01 00:00:00     | 233.4742923        | Premium   | 0     | 2021-03-01 00:00:00     |
| CUST_1     | 2023-10-01 00:00:00     | 261.9748748        | Standard  | 1     | 2021-03-01 00:00:00     |
| CUST_1     | 2023-11-01 00:00:00     | 307.6969774        | Basic     | 1     | 2021-03-01 00:00:00     |


 **NaN** = (356.9555631 + 233.4742923 )/2

 





