# cancer survival predictor

This project introduces a logistic regression model to predict the survival expectancy (categorical) for children affected by cancer.
The goal is to predict whether the patient's life expectancy is :
 - **Low** *(< 18 months)*
 - **Intermediate** *(< 36 months)*
 - **High** *(+ 36 months)*
 
First of all make sure that the Excel file containing the clinic and radionomic features is located at the root of the project. Otherwise, change the excel reading paths in the codes.

The project is structured in various files :
- ***analyseDeces.py*** : run this code to visualize the distribution of the dataset, in terms of status (DEAD or ALIVE), per patient age, and duration between diagnose and event.
- ***clean_dataset.py*** : this code removes from the dataset the samples that were deamed unreleavant for the considered prediction task. *NaN* values are corrected and categorical values are encoded in integer format. A new Excel file containing the cleaned data is generated.
- ***labels_TP.txt*** : gives the meaning of the new encoded data.
- ***visualize_data.py*** : performs a quick analysis of the dataset. The targets distribution, statistics are computed. The correlation matrix between the predictors is also displayed.
- ***model.py*** : run this code to do the logistic regression. Make sure the *"cleaned_dataset"* was produced before.
- ***Demo.ipynb*** : a simple jupyter notebook that illustrates the results that should be obtained. 
