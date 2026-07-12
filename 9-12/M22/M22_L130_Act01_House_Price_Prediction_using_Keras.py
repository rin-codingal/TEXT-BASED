import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# load dataset
df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M22\housing_data.csv")
print(df.head())
print()

# split into input (X) and output (Y) variables
y = df.pop('AboveMedianPrice')
x = df

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# create model
model = Sequential()
model.add(Dense(10, input_dim=10, kernel_initializer='normal', activation='relu'))
model.add(Dense(6, kernel_initializer='normal', activation='relu'))
model.add(Dense(1, kernel_initializer='normal'))

# Compile model
model.compile(loss='mean_squared_error', optimizer='adam')

# Fitting the ANN to the Training set
model_history=model.fit(X_train, y_train, batch_size = 10, epochs = 100)

# list all data in history
print(model.summary())
#total params are total number of weights and biases

print()
# Predict the Test set results
Y_pred = model.predict(X_test)
print(Y_pred)
print()

# Calculate the Model Performance
mae = mean_absolute_error(y_test, Y_pred)

print(mae)

"""### Model Accuracy = 1-0.30 = 0.70"""

"""
to fix keras problem:
in terminal, write these codes:
python -m pip uninstall tensorflow keras -y
python -m pip install --upgrade tensorflow keras
python -c "from keras.models import Sequential; print('Success!')" #this is to check whether the installation success

if there's error due to windows long path support, open powershell and type these:
Set-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1

then restart vscode
"""