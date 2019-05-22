# =============================================================================
# AM 231 Final Project: Predictive Policing for the City of Boston
# =============================================================================

import csv
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split


mnb = MultinomialNB()
rf = RandomForestClassifier(n_estimators = 50, max_depth = 50)
gb = GradientBoostingClassifier()

X = []
y = []

with open('crimes.csv') as crimes:
    crimes = csv.reader(crimes, delimiter = ',')
    for row in crimes:
         X.append(list(row))
    
with open('labels.csv') as labels:
    labels = csv.reader(labels, delimiter = ',')
    for row in labels:
         y.append(list(row))

del X[0]
del y[0]

for i in range(len(X)):
    del X[i][0]
    del y[i][0]

# encoding y ##########################
crime_types = []
for i in range(len(y)):
    if y[i] not in crime_types:
        crime_types.append(y[i])

encoded_y = []

for i in range(len(y)):
    for j in range(len(crime_types)):
        if y[i] == crime_types[j]:
            encoded_y.append(j)

##############################################

# encoding X #########################
districts = []
days_of_week = []
hours = []

for i in range(len(y)):
    if X[i][0] not in districts:
        districts.append(X[i][0])
    if X[i][1] not in days_of_week:
        days_of_week.append(X[i][1])
    if X[i][2] not in hours:
        hours.append(X[i][2])

encoded_X = []

for i in range(len(y)):
    three_encoded_features = []
    for j in range(len(districts)):
        if X[i][0] == districts[j]:
            three_encoded_features.append(j)
    
    for j in range(len(days_of_week)):
        if X[i][1] == days_of_week[j]:
            three_encoded_features.append(j)
    
    for j in range(len(hours)):
        if X[i][2] == hours[j]:
            three_encoded_features.append(j)
    
    encoded_X.append(three_encoded_features)
#############################################

# randomly split into test and training data
X_train, X_test, y_train, y_test = train_test_split(encoded_X, encoded_y, test_size=0.25)

mnb.fit(X_train, y_train)
rf.fit(X_train, y_train)
gb.fit(X_train, y_train)

mnb_preds = mnb.predict(X_test)
rf_preds = rf.predict(X_test)
gb_preds = gb.predict(X_test
                      )
# calculate accuracy of predictions
mnb_correct_predictions = 0
rf_correct_predictions = 0
gb_correct_predictions = 0

for i in range(len(mnb_preds)):
    if mnb_preds[i] == y_test[i]:
        mnb_correct_predictions += 1
    if rf_preds[i] == y_test[i]:
        rf_correct_predictions += 1
    if gb_preds[i] == y_test[i]:
        gb_correct_predictions += 1

mnb_accuracy = mnb_correct_predictions / len(mnb_preds)
rf_accuracy = rf_correct_predictions / len(rf_preds)
gb_accuracy = gb_correct_predictions / len(gb_preds)

number_of_different_crimes = len(crime_types)
print("Random guessing gives an accuracy baseline of ", 1/number_of_different_crimes)
print("MNB has accuracy ", mnb_accuracy)
print("Random forest has accuracy", rf_accuracy)
print("Gradient boosting has accuracy", gb_accuracy)