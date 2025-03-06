## Customer-Churn-Classification
Atidot - DS Assignment 

In this assignment, I have developed a robust classification model that predicts customer churn between January 1, 2024, and February 28, 2024, using time-series data with a double index (customer_id and date). This task demonstrates my skills in modeling, feature engineering, and production-aware design practices.

### Dataset Overview
The dataset contains the following features:

**customer_id:** Unique identifier for each customer.
**date:** The date of the transaction, ranging from January 1, 2023, to December 31, 2023.
**transaction_amount:** Numerical feature representing the amount spent by the customer.
**plan_type:** Categorical feature indicating the type of plan (Basic, Standard, Premium).
**churn:** Binary target variable where 1 indicates the customer has churned, and 0 means they have stayed.
**issuing_date:** The date when the customer first purchased the insurance.

### Data Preprocessing and Feature Engineering
Handling Missing Values: I filled missing values in the transaction_amount feature using the mean value of the transaction_amount for the same plan_type. 

For example, for a customer with a missing value, I replaced it with the average of the transaction_amount values for customers with the same plan_type.
 
| customer_id | date                   | transaction_amount | plan_type | churn | issuing_date          |
|------------|------------------------|--------------------|-----------|-------|------------------------|
| CUST_1     | 2023-06-01 00:00:00     | **NaN**            | Premium   | 0     | 2021-03-01 00:00:00     |


 **NaN** = (356.9555631 + 233.4742923 )/2

 ### Date-dependent Features: Three relevant date-dependent features were created to enhance the model:

**date_month:** The month of the year corresponding to the transaction date.
**plan_changes:** Binary feature indicating whether the customer changed their plan type (1 = change, 0 = no change).
**plan_changes_total_changes:** The total number of plan changes for the customer in 2023.
**date_minus_issuing_date:** The number of days between the transaction date and the issuing date

### Exploratory data analysis of the data frame

#### Corrlation Matrix

I performed a correlation analysis to examine relationships between numerical features. The correlation matrix showed no significant linear relationships between the features.

| Feature                      | transaction_amount | plan_changes_total_changes | date_minus_issuing_date |
|------------------------------|--------------------|---------------------------|-------------------------|
| **transaction_amount**        | 1.000000          | -0.034869                 | 0.003824                |
| **plan_changes_total_changes** | -0.034869         | 1.000000                  | 0.022887                |
| **date_minus_issuing_date**   | 0.003824          | 0.022887                  | 1.000000                |


#### Histogram of the date_minus_issuing_date belonging to the customers that leave the company 

Histogram of date_minus_issuing_date: This visualization shows the distribution of date_minus_issuing_date for customers who churned.

<img src="https://github.com/Amityaron/customer-churn-classifi-cation/blob/main/Plots/Histogram%20of%20the%20date_minus_issuing_date%20.png" width="40%" height="40%">


#### Box plot of transaction_amount for each plan type for customers that leave/stay in the company 

<img src="https://github.com/Amityaron/customer-churn-classifi-cation/blob/main/Plots/Box%20plot%20transaction_amount%20for%20each%20plan%20type.png" width="40%" height="40%">

#### Box plot of transaction_amount and Statiscal Summary

Box plot of transaction_amount for each plan type: 

The box plot illustrates the distribution of transaction amounts for customers who stayed versus those who churned.

<img src="https://github.com/Amityaron/customer-churn-classifi-cation/blob/main/Plots/Box%20plot%20transaction_amount.png" width="40%" height="40%">

##### Summary of Transaction Amount  

<table>
  <tr>
    <th colspan="2">Churned Customers</th>
    <th colspan="2">Retained Customers</th>
  </tr>
  <tr>
    <td><b>Statistic</b></td><td><b>Value</b></td>
    <td><b>Statistic</b></td><td><b>Value</b></td>
  </tr>
  <tr>
    <td>Count</td><td>47</td>
    <td>Count</td><td>53</td>
  </tr>
  <tr>
    <td>Mean</td><td>232.45</td>
    <td>Mean</td><td>244.96</td>
  </tr>
  <tr>
    <td>Std Dev</td><td>154.67</td>
    <td>Std Dev</td><td>147.75</td>
  </tr>
  <tr>
    <td>Min</td><td>10.07</td>
    <td>Min</td><td>14.89</td>
  </tr>
  <tr>
    <td>25%</td><td>89.22</td>
    <td>25%</td><td>122.90</td>
  </tr>
  <tr>
    <td>50% (Median)</td><td>248.14</td>
    <td>50% (Median)</td><td>206.42</td>
  </tr>
  <tr>
    <td>75%</td><td>364.89</td>
    <td>75%</td><td>387.75</td>
  </tr>
  <tr>
    <td>Max</td><td>492.64</td>
    <td>Max</td><td>490.78</td>
  </tr>
</table>


#### Histogram of the customers who leave the company by mouth


<img src="https://github.com/Amityaron/customer-churn-classifi-cation/blob/main/Plots/Histogram%20of%20mouth%20for%20custumer%20that%20leave%20the%20company.png" width="40%" height="40%">

#### Model Development and Evaluation

I applied three classification models: Logistic Regression, Random Forest, and XGBoost. The dataset was split into training and testing sets (80% for training, 20% for testing).
 
##### Logistic regression performance  : 

###### Accuracy  
**Accuracy:** 0.69  

###### Confusion Matrix  
| Actual \ Predicted | 0  | 1  |
|--------------------|----|----|
| **0** (Stay)      | 151 | 12 |
| **1** (Churn)     | 62  | 15 |

###### Classification Report

| Class               | Precision | Recall | F1-Score | Support |
|---------------------|-----------|--------|----------|---------|
| **0** (Stay)        | 0.71      | 0.93   | 0.80     | 163     |
| **1** (Churn)       | 0.56      | 0.19   | 0.29     | 77      |
| **Accuracy**        |           |        | 0.69     | 240     |
| **Macro Avg**       | 0.63      | 0.56   | 0.55     | 240     |
| **Weighted Avg**    | 0.66      | 0.69   | 0.64     | 240     |


###### Feature Importance  
| Feature                         | Coefficient  |
|---------------------------------|--------------|
| **date_mouth**                  | 0.790085     |
| **transaction_amount**          | 0.054664     |
| **plan_type_Premium**           | -0.013193    |
| **plan_type_Standard**          | -0.051589    |
| **plan_changes**                | -0.057033    |
| **plan_changes_total_changes**  | -0.193752    |
| **date_minus_issuing_date**     | -0.421579    |


##### Random Forest performance : 
 
###### Accuracy  
**Accuracy:** 0.74  

###### Confusion Matrix  
| Actual \ Predicted | 0  | 1  |
|--------------------|----|----|
| **0** (Stay)       | 145 | 18 |
| **1** (Churn)      | 45  | 32 |

###### Classification Report

| Class               | Precision | Recall | F1-Score | Support |
|---------------------|-----------|--------|----------|---------|
| **0** (Stay)        | 0.76      | 0.89   | 0.82     | 163     |
| **1** (Churn)       | 0.64      | 0.42   | 0.50     | 77      |
| **Accuracy**        |           |        | 0.74     | 240     |
| **Macro Avg**       | 0.70      | 0.65   | 0.66     | 240     |
| **Weighted Avg**    | 0.72      | 0.74   | 0.72     | 240     |

###### Feature Importance  
| Feature                         | Importance  |
|---------------------------------|-------------|
| **date_minus_issuing_date**     | 0.292386    |
| **transaction_amount**          | 0.276920    |
| **date_mouth**                  | 0.198031    |
| **plan_changes_total_changes**  | 0.155698    |
| **plan_type_Standard**          | 0.027657    |
| **plan_changes**                | 0.025918    |
| **plan_type_Premium**           | 0.023391    |



##### XGBOOST performance: 

###### Accuracy  
**Accuracy:** 0.75  

###### Confusion Matrix  
| Actual \ Predicted | 0  | 1  |
|--------------------|----|----|
| **0** (Stay)       | 140 | 23 |
| **1** (Churn)      | 36  | 41 |

###### Classification Report

| Class               | Precision | Recall | F1-Score | Support |
|---------------------|-----------|--------|----------|---------|
| **0** (Stay)        | 0.80      | 0.86   | 0.83     | 163     |
| **1** (Churn)       | 0.64      | 0.53   | 0.58     | 77      |
| **Accuracy**        |           |        | 0.75     | 240     |
| **Macro Avg**       | 0.72      | 0.70   | 0.70     | 240     |
| **Weighted Avg**    | 0.75      | 0.75   | 0.75     | 240     |

###### Feature Importance  
| Feature                         | Importance  |
|---------------------------------|-------------|
| **transaction_amount**          | 736.0       |
| **date_minus_issuing_date**     | 695.0       |
| **date_mouth**                  | 242.0       |
| **plan_changes**                | 37.0        |
| **plan_changes_total_changes**  | 358.0       |
| **plan_type_Premium**           | 61.0        |
| **plan_type_Standard**          | 96.0        |

### Conclusion

The model achieved a strong performance, with XGBoost yielding the highest accuracy of 0.75, followed by Random Forest (0.74) and Logistic Regression (0.69).

Based on the feature importance analysis, it is evident that the transaction_amount, date_minus_issuing_date, and date_month are the most influential features in predicting customer churn.


