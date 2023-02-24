import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

#import statsmodels.api as sm
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import roc_auc_score
from sklearn.metrics import classification_report
#import statsmodels.api as sm


df = pd.read_excel("clean_dataset.xlsx", header=0)
df_copy = df.copy()



# display the target distribution
print(df["Life_exp"].value_counts())
sns.countplot(x=df["Life_exp"])
plt.show()
plt.close()



# display barplots of each feature, per target
fig, ax = plt.subplots(7, 7, figsize=(20, 10))
for value, subplot in zip(range(11,60), ax.flatten()):
    sns.barplot(x=df['Life_exp'], y=df[df.columns[value]], ax=subplot)
plt.show()
plt.close()



# display target distribution per feature
dfo = df.iloc[:,11:].copy()
fig2, ax2 = plt.subplots(7, 7, figsize=(20, 10))
for value, subplot in zip(range(0,49), ax2.flatten()):
    sns.histplot(data=dfo, x=dfo[dfo.columns[value]], hue=dfo["Life_exp"], kde=True,legend=False, ax=subplot)
plt.show()
plt.close()



# display the correlation matrix
corr_matrix = dfo.iloc[:,:-1].corr()
sns.heatmap(corr_matrix.round(2), annot=True)
plt.show()


col_list = dfo.columns.values.tolist()
count_corr = 0
corr_var = []
print(corr_matrix.shape)
for i in range(1,49):
    for j in range(i+1,49):
        if (abs(corr_matrix.iloc[i][j])>0.81 and i!=j):
            mlt = "  *  "
            string = col_list[i] + mlt + col_list[j]
            corr_var.append(string)
            count_corr = count_corr + 1

print("Number of correlations : " + str(count_corr))
for l in corr_var:
    print("\t" + l)


"""
df1=df.copy()
count1=0
for i in range (0,df.shape[0]):
    if df['Life_exp'].iloc[i]==1:
        df1['Life_exp'].iloc[i]=1
        print("youhou")

    else:
        df1['Life_exp'].iloc[i]=0
        count1=count1+1

print("Count 1: " + str(count1))
print(sum(df1["Life_exp"]))

df2=df.copy()
count2=0
for i in range (0,df.shape[0]):
    if (df['Life_exp'].iloc[i]==2):
        df2['Life_exp'].iloc[i]=1

    else:
        df2['Life_exp'].iloc[i]=0
        count2=count2+1

print("Count 2: " + str(count2))


df3=df.copy()
count3=0
for i in range (0,df.shape[0]):
    if (df['Life_exp'].iloc[i]==3):
        df3['Life_exp'].iloc[i]=1

    else:
        df3['Life_exp'].iloc[i]=0
        count1=count1+1

print("Count 3: " + str(count3))


print(sum(df1["Life_exp"]))
X1=df1.iloc[:,11:60]
y1=df1['Life_exp']
print(sum(y1))
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size=0.2,random_state=1996)
print(sum(y_train1))
print(sum(y_test1))
lgr1=LogisticRegression()
lgr1.fit(X_train1, y_train1)
pred1=lgr1.predict(X_test1)

auc1 = roc_auc_score(y_test1,pred1)
print("AUC 1: " + str(auc1))



X2=df2.iloc[:,11:60]
y2=df2['Life_exp']
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.2,random_state=1996)
lgr2=LogisticRegression()
lgr2.fit(X_train2, y_train2)
pred2=lgr2.predict(X_test2)

auc2 = roc_auc_score(y_test2,pred2)
print("AUC 2: " + str(auc2))



X3=df3.iloc[:,11:60]
y3=df3['Life_exp']
X_train3, X_test3, y_train3, y_test3 = train_test_split(X3, y3, test_size=0.2,random_state=1996)
lgr3=LogisticRegression()
lgr3.fit(X_train3, y_train3)
pred3=lgr3.predict(X_test3)

auc3 = roc_auc_score(y_test3,pred3)
print("AUC 3: " + str(auc3))
"""
