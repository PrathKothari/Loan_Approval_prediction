import requests

url = 'http://127.0.0.1:8000/predict'
data = {
"Married" : 1,
"Dependents": 0,
"Education" : 1,
"Self_Employed":0,
"LoanAmount":175.0,
"Loan_Amount_Term":360.0,
"Credit_History":1.0,
"Property_Area":1,
"Total_Income":9862.0
} #Sample Data

response = requests.post(url, json=data)
print(response.json())
