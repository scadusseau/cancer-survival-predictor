import warnings
warnings.filterwarnings('ignore')
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import statsmodels.api as sm
import matplotlib.pyplot as plt



df = pd.read_excel("clean_dataset.xlsx", header=0)

dfo = df.iloc[:,11:].copy()



corr_matrix = dfo.iloc[:,:-1].corr()
col_list = dfo.columns.values.tolist()
count_corr = 0
corr_var = []

for i in range(1,49):
    for j in range(i+1,49):
        if (abs(corr_matrix.iloc[i][j])>0.81 and i!=j):
            string = col_list[i]
            if string not in corr_var:
                corr_var.append(string)
            count_corr = count_corr + 1
print(corr_var)

dfreg = dfo.drop(corr_var, axis=1)



# perform standard normalization
sc = StandardScaler()
dfreg.iloc[:,:-1] = sc.fit_transform(dfreg.iloc[:,:-1])


# Build the new dataframe for the 1st class to predict
dfreg1 = dfreg.copy()
count1 = 0
for i in range (0, dfreg.shape[0]):
    if dfreg['Life_exp'].iloc[i] == 1:
        dfreg1['Life_exp'].iloc[i] = 1
    else:
        dfreg1['Life_exp'].iloc[i] = 0
        count1 = count1 + 1

print("Count 1: " + str(count1))
print(sum(dfreg1["Life_exp"]))


# Build the new dataframe for the 2nd class to predict
dfreg2 = dfreg.copy()
count2 = 0
for i in range (0, dfreg.shape[0]):
    if dfreg['Life_exp'].iloc[i] == 2:
        dfreg2['Life_exp'].iloc[i] = 1
    else:
        dfreg2['Life_exp'].iloc[i] = 0
        count2 = count2 + 1

print("Count 2: " + str(count2))
print(sum(dfreg2["Life_exp"]))


# Build the new dataframe for the 3rd class to predict
dfreg3 = dfreg.copy()
count3 = 0
for i in range (0, dfreg.shape[0]):
    if dfreg['Life_exp'].iloc[i] == 3:
        dfreg3['Life_exp'].iloc[i] = 1
    else:
        dfreg3['Life_exp'].iloc[i] = 0
        count3 = count3 + 1

print("Count 3: " + str(count3))
print(sum(dfreg3["Life_exp"]))



# Train and test the 1st dataframe
X1=dfreg1.iloc[:,:-1]
y1=dfreg1['Life_exp']
print(sum(y1))
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size=0.2, random_state=1995)
#print(sum(y_train1))
#print(sum(y_test1))
lgr1=LogisticRegression(class_weight="balanced")
lgr1.fit(X_train1, y_train1)
pred1=lgr1.predict(X_test1)

tn1, fp1, fn1, tp1 = confusion_matrix(y_test1, pred1).ravel()
print("\n\t\tTrue\tFalse")
print("Positive\t" + str(tp1) + "\t" + str(fp1))
print("Negative\t" + str(tn1) + "\t" + str(fn1))

print("\nAccuracy 1: " + str(accuracy_score(y_test1, pred1)))

auc1 = roc_auc_score(y_test1,pred1)
print("\nAUC 1: " + str(auc1))

fpr1, tpr1, thresholds1 = roc_curve(y_test1, pred1)
plt.plot(fpr1, tpr1)
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()

#log_reg1 = sm.Logit(y_train1, X_train1).fit()
#print(log_reg1.summary())



# Train and test the 2nd dataframe
X2=dfreg2.iloc[:,:-1]
y2=dfreg2['Life_exp']
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.2, random_state=1995)
print(sum(y_train2))
print(sum(y_test2))
lgr2=LogisticRegression(class_weight="balanced")
lgr2.fit(X_train2, y_train2)
pred2=lgr2.predict(X_test2)

tn2, fp2, fn2, tp2 = confusion_matrix(y_test2, pred2).ravel()
print("\n\t\tTrue\tFalse")
print("Positive\t" + str(tp2) + "\t" + str(fp2))
print("Negative\t" + str(tn2) + "\t" + str(fn2))

print("\nAccuracy 2: " + str(accuracy_score(y_test2, pred2)))

auc2 = roc_auc_score(y_test2,pred2)
print("\nAUC 2: " + str(auc2))

fpr2, tpr2, thresholds2 = roc_curve(y_test2, pred2)
plt.plot(fpr2, tpr2)
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()

#log_reg2 = sm.Logit(y_train2, X_train2).fit()
#print(log_reg2.summary())



# Train and test the 3rd dataframe
X3=dfreg3.iloc[:,:-1]
y3=dfreg3['Life_exp']
X_train3, X_test3, y_train3, y_test3 = train_test_split(X3, y3, test_size=0.2, random_state=1995)
lgr3=LogisticRegression(class_weight="balanced")
lgr3.fit(X_train3, y_train3)
pred3=lgr3.predict(X_test3)

tn3, fp3, fn3, tp3 = confusion_matrix(y_test3, pred3).ravel()
print("\n\t\tTrue\tFalse")
print("Positive\t" + str(tp3) + "\t" + str(fp3))
print("Negative\t" + str(tn3) + "\t" + str(fn3))

print("\nAccuracy 3: " + str(accuracy_score(y_test3, pred3)))

conf_mat3 = confusion_matrix(y_test3, pred3)
print(conf_mat3)

auc3 = roc_auc_score(y_test3,pred3)
print("AUC 3: " + str(auc3))

fpr3, tpr3, thresholds3 = roc_curve(y_test3, pred3)
plt.plot(fpr3, tpr3)
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()

#log_reg3 = sm.Logit(y_train3, X_train3).fit()
#print(log_reg3.summary())
