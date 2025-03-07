import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from xgboost import XGBClassifier
import xgboost as xgb
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def ReadCSVfile(file_path):
  df = pd.read_csv(file_path, parse_dates=['date', 'issuing_date'])
  # Convert 'date' to datetime format (if not already parsed)
  df['date'] = pd.to_datetime(df['date'])
  df['issuing_date'] = pd.to_datetime(df['issuing_date'])  # Convert issuing_date column
  df['date_minus_issuing_date'] = (df['date'] - df['issuing_date']).dt.days
  # Set MultiIndex
  df.set_index(['customer_id', 'date'], inplace=True)
  # Display the DataFrame
  df = df.reset_index()
  df['date_mouth']=df['date'].dt.month
  #Add colums _total_changes of plan types
  # Create a new column that will store the number of plan type changes
  df['plan_changes'] = (df['plan_type'] != df.groupby('customer_id')['plan_type'].shift()).astype(int)
  # Group by customer and sum the plan changes to get the total number of plan type moves for each customer
  df_plan_changes = df.groupby('customer_id')['plan_changes'].sum().reset_index()
  # Merge the total plan changes with the original DataFrame
  df = df.merge(df_plan_changes, on='customer_id', how='left', suffixes=('', '_total_changes'))
  # Display the updated DataFrame
  # Function to fill NaN values
  def fill_transaction_amount(df):
      df['transaction_amount'] = df.groupby(['customer_id', 'plan_changes'])['transaction_amount'].transform(
          lambda x: x.fillna(x.mean()))
      return df
  # Apply function
  df_filled = fill_transaction_amount(df)
  df=df_filled
  df['chunk_id'] = df['customer_id'].factorize()[0] + 1 
  return df


def XGBOOST_model(df):

  # Drop non-numeric columns (customer_id, date, issuing_date)
  df = df.drop(columns=['customer_id', 'date', 'issuing_date'])

  # One-Hot Encode 'plan_type'
  df = pd.get_dummies(df, columns=['plan_type'], drop_first=True)

  # Split data into features (X) and target (y)
  X = df.drop(columns=['churn'])  # Features
  y = df['churn']  # Target variable

  # Standardize numerical features
  scaler = StandardScaler()
  X_scaled = scaler.fit_transform(X)

  # Split into training & testing sets (80% train, 20% test)
  X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

  # Train XGBoost Model
  xgb_model = XGBClassifier(n_estimators=100, learning_rate=0.1, random_state=42, use_label_encoder=False, eval_metric='logloss')
  xgb_model.fit(X_train, y_train)

  # Predict on test set
  y_pred = xgb_model.predict(X_test)

  # Evaluate model
  accuracy = accuracy_score(y_test, y_pred)
  conf_matrix = confusion_matrix(y_test, y_pred)
  report = classification_report(y_test, y_pred)

  # Print results
  print(f'Accuracy: {accuracy:.2f}')
  print('Confusion Matrix:')
  print(conf_matrix)
  print('Classification Report:')
  print(report)

  # Get feature importance with actual column names
  feature_importance = xgb_model.get_booster().get_score(importance_type='weight')

  #  Map feature names (f0, f1, ...) to actual column names
  feature_mapping = {f"f{i}": col for i, col in enumerate(X.columns)}
  feature_importance_named = {feature_mapping[k]: v for k, v in feature_importance.items()}

  # Print feature importance with correct names
  print("Feature Importance:", feature_importance_named)

  # Plot Feature Importance with correct names
  plt.figure(figsize=(10, 5))
  plt.barh(list(feature_importance_named.keys()), list(feature_importance_named.values()))
  plt.xlabel("Importance Score")
  plt.ylabel("Feature Name")
  plt.title("XGBoost Feature Importance")
  plt.show()
  return xgb_model

def save_pred_csv(df,xgb_model):

  # Load your original dataset (replace 'your_dataset.csv' with the actual file path)
  df_original = df

  # Drop non-numeric columns (customer_id, date, issuing_date)
  df_original_processed = df_original.drop(columns=['customer_id', 'date', 'issuing_date',"churn"])
  # One-Hot Encode 'plan_type'
  df_original_processed = pd.get_dummies(df_original_processed, columns=['plan_type'], drop_first=True)

  # Standardize the numerical features using the same scaler that was used for training
  scaler = StandardScaler()
  df_original_scaled = scaler.fit_transform(df_original_processed)

  # Predict churn using the trained XGBoost model (assuming it's already trained as xgb_model)
  churn_predictions = xgb_model.predict(df_original_scaled)

  # Add the churn predictions back to the original dataset
  df_original['churn_predicted'] = churn_predictions

  # Save the dataframe with the predicted churn column to a new CSV file
  df_original.to_csv('your_dataset_with_predictions.csv', index=False)

  # Print the first few rows to check the added column
  print(datacsv.head())




df=ReadCSVfile("\churn_data (4).csv")
xgb_model=XGBOOST_model(df)
save_pred_csv(df,xgb_model)
