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

 ### Date-dependent Features: Five relevant date-dependent features were created to enhance the model:

**date_month:** The month of the year corresponding to the transaction date.

**plan_changes:** Binary feature indicating whether the customer changed their plan type (1 = change, 0 = no change).

**plan_changes_total_changes:** The total number of plan changes for the customer in 2023.

**date_minus_issuing_date:** The number of days between the transaction date and the issuing date

**chunk_id**: customer_id  we used it to verify when we split the data into train and test, we don't cut the customer in the middle of the year.
 
### Exploratory data analysis of the data frame

#### Corrlation Matrix

I performed a correlation analysis to examine relationships between numerical features. The correlation matrix showed no significant linear relationships between the features.

| Feature                      | transaction_amount | plan_changes_total_changes | date_minus_issuing_date | chunk_id |
|------------------------------|--------------------|---------------------------|-------------------------|----------|
| **transaction_amount**        | 1.000000          | -0.034869                 | 0.003824                | 0.022387 |
| **plan_changes_total_changes** | -0.034869         | 1.000000                  | 0.022887                | -0.122174 |
| **date_minus_issuing_date**   | 0.003824          | 0.022887                  | 1.000000                | -0.149505 |
| **chunk_id**                  | 0.022387          | -0.122174                 | -0.149505               | 1.000000 |


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
**Accuracy:** 0.71  

###### Confusion Matrix  
| Actual \ Predicted | 0  | 1  |
|--------------------|----|----|
| **0** (Stay)      | 153 | 10 |
| **1** (Churn)     | 60  | 17 |

###### Classification Report  

| Class               | Precision | Recall | F1-Score | Support |
|---------------------|-----------|--------|----------|---------|
| **0** (Stay)        | 0.72      | 0.94   | 0.81     | 163     |
| **1** (Churn)       | 0.63      | 0.22   | 0.33     | 77      |
| **Accuracy**        |           |        | 0.71     | 240     |
| **Macro Avg**       | 0.67      | 0.58   | 0.57     | 240     |
| **Weighted Avg**    | 0.69      | 0.71   | 0.66     | 240     |

###### Feature Importance  

| Feature                         | Coefficient  |
|---------------------------------|--------------|
| **date_mouth**                  | 0.804456     |
| **transaction_amount**          | 0.058123     |
| **plan_type_Premium**           | -0.013092    |
| **plan_type_Standard**          | -0.054059    |
| **plan_changes**                | -0.054871    |
| **chunk_id**                    | -0.202946    |
| **plan_changes_total_changes**  | -0.226702    |
| **date_minus_issuing_date**     | -0.452507    |


##### Random Forest performance : 
 


###### Accuracy  
**Accuracy:** 0.83  

###### Confusion Matrix  
| Actual \ Predicted | 0  | 1  |
|--------------------|----|----|
| **0** (Stay)      | 153 | 10 |
| **1** (Churn)     | 31  | 46 |

###### Classification Report  

| Class               | Precision | Recall | F1-Score | Support |
|---------------------|-----------|--------|----------|---------|
| **0** (Stay)        | 0.83      | 0.94   | 0.88     | 163     |
| **1** (Churn)       | 0.82      | 0.60   | 0.69     | 77      |
| **Accuracy**        |           |        | 0.83     | 240     |
| **Macro Avg**       | 0.83      | 0.77   | 0.79     | 240     |
| **Weighted Avg**    | 0.83      | 0.83   | 0.82     | 240     |

###### Feature Importance  

| Feature                         | Importance  |
|---------------------------------|-------------|
| **chunk_id**                    | 0.243748    |
| **date_minus_issuing_date**     | 0.223735    |
| **transaction_amount**          | 0.184039    |
| **date_mouth**                  | 0.160879    |
| **plan_changes_total_changes**  | 0.122486    |
| **plan_type_Standard**          | 0.023030    |
| **plan_changes**                | 0.021459    |
| **plan_type_Premium**           | 0.020624    |



##### XGBOOST performance: 

###### Accuracy  
**Accuracy:** 0.90  

###### Confusion Matrix  
| Actual \ Predicted | 0  | 1  |
|--------------------|----|----|
| **0** (Stay)      | 156 | 7  |
| **1** (Churn)     | 16  | 61 |

###### Classification Report  

| Class               | Precision | Recall | F1-Score | Support |
|---------------------|-----------|--------|----------|---------|
| **0** (Stay)        | 0.91      | 0.96   | 0.93     | 163     |
| **1** (Churn)       | 0.90      | 0.79   | 0.84     | 77      |
| **Accuracy**        |           |        | 0.90     | 240     |
| **Macro Avg**       | 0.90      | 0.87   | 0.89     | 240     |
| **Weighted Avg**    | 0.90      | 0.90   | 0.90     | 240     |

###### Feature Importance  

| Feature                         | Importance |
|---------------------------------|------------|
| **chunk_id**                    | 752.0      |
| **date_minus_issuing_date**     | 504.0      |
| **transaction_amount**          | 326.0      |
| **plan_changes_total_changes**  | 196.0      |
| **date_mouth**                  | 162.0      |
| **plan_type_Standard**          | 35.0       |
| **plan_type_Premium**           | 24.0       |
| **plan_changes**                | 16.0       |


### Conclusion

The model achieved a strong performance, with XGBoost yielding the highest accuracy of 0.90, followed by Random Forest (0.83) and Logistic Regression (0.71).

Based on the feature importance analysis, it is evident that 

1. transaction_amount
2. date_minus_issuing_date
3. date_month
4. chunk_id (Verify when you split the data to train&test you don't cut customer in the middle of the year )
   * Pay attention that if a customer churns from the company, he will not return.

are the most influential features in predicting customer churn.

#### XGBOOST model explanation: 

1. SHAP (SHapley Additive exPlanations)
2. XGBOOST model explanation

###### SHAP (SHapley Additive exPlanations)

<img src="https://github.com/Amityaron/customer-churn-classifi-cation/blob/main/Plots/SAHP%20plot.png" width="40%" height="40%">

Based on game theory, SHAP assigns an importance value to each feature for a given prediction.

SHAP aims to fairly assign a value to each feature $x_i$ in our case we have 7 features.

based on its contribution to the model’s prediction for an instance.


$\phi_i(f) = \sum_{S \subseteq N \setminus \{i\}} \frac{|S|! (|N| - |S| - 1)!}{|N|!} \left[ f(S \cup \{i\}) - f(S) \right]$

Explanation of Terms:

* $S$: A subset of all features except feature $i$
* $N$ :  The set of all features.
* $f(S)$ : The model’s prediction when using only the features in subset $S$
*  $f(S∪{i}):$ The model’s prediction when feature $i$ is added to $S$
* $\frac{\left|S\right|! \cdot \left(\left|\left|N\right|\right| - \left|\left|S\right|\right| - 1 \right)!}{\left|\left|N\right|\right|!}$ :A weight that ensures all subsets are considered fairly.

 SHAP values have the following key properties that make them attractive for model interpretability:

Local Accuracy (Model Explanation): The sum of the SHAP values for all features is equal to the model’s prediction. 

That is, for a given instance $x$

we have:

$d=7$



###### XGBoost - Extreme Gradient Boosting

**XGBoost** (Extreme Gradient Boosting) is a powerful machine learning algorithm that builds an ensemble of decision trees using a boosting technique.

The key idea is to combine multiple weak models (trees) to create a stronger predictive model.

###### Core Concept:

###### 1. Boosting:
XGBoost is based on **gradient boosting**, which builds trees sequentially. Each new tree tries to correct the errors (residuals) of the previous tree. In mathematical terms, the model prediction at step \( t \) is updated as:

$F_t(x) = F_{t-1}(x) + \eta \cdot h_t(x)$


Where:
- $\( F_{t-1}(x) \)$ is the prediction from the previous step.
- $\( \eta \)$ is the **learning rate** (a regularization parameter).
- $\( h_t(x) \)$ is the new tree being added at step $\( t \)$.

###### 2. Loss Function:
XGBoost minimizes a **regularized loss function** that combines the residual error and a penalty for the complexity of the tree. The objective function to minimize is:


$L(θ) = \sum_{i=1}^{n} \ell(y_i,\hat{y_i}) + \sum_{k=1}^{T} \Omega(f_k)$



Where:
- $\ell(y_i, \hat{y}_i)$ is the loss function (e.g., mean squared error for regression or log loss for classification).
- $\Omega(f_k) = \gamma T_k + \frac{1}{2} \lambda ||w_k||^2$ is the regularization term that penalizes the complexity of each tree (measured by the number of leaves $T_k$
 and the leaf weights $w_k$.

###### 3. Tree Structure:
Each decision tree $\( h_t(x) \)$ is built by iterating over the data to find the best split for each node, minimizing the residual errors.

###### Optimization:

XGBoost uses **second-order derivatives** (i.e., the gradient and the Hessian) to perform optimization more efficiently, making it faster and more accurate. The update rule for the model parameters \( w \) is:


$w_{t+1} = w_t - \eta \cdot \frac{\partial L}{\partial w_t}$


Where:
- $\( \frac{\partial L}{\partial w_t} \)$ is the gradient of the loss with respect to the model parameters.

###### Key Features:
- **Regularization**: Both L1 and L2 regularization help prevent overfitting.
- **Parallelization**: XGBoost speeds up training by parallelizing tree construction and computation of gradients.
- **Handling Missing Data**: It automatically handles missing values by learning how to deal with them during training.

XGBoost's combination of high accuracy, regularization, and speed makes it one of the most popular algorithms in data science.


$f(x) = \sum_{i=1}^{d} \phi_i(f) + \phi_{\text{bias}}$


  

