# This code aims to clean the dataset:
# - remove unreleavent samples
# - fill out missing values
# - encode categorical features in a digital format
# - define and compute the new target variable

import pandas as pd
from sklearn.preprocessing import LabelEncoder



classeur_init = pd.read_excel("Classeur_TP_fevr2023.xlsx", header=1)
print("\nInitial dataset shape :")
print(classeur_init.shape)


# Remove living patients with time_months < 24

index_u24 = classeur_init[ classeur_init["time_months"] + 24*classeur_init["statut"] < 24 ].index
classeur_sub1 = classeur_init.drop(index_u24, inplace = False)
print("\nDataset with living patients with time_months < 24 removed :")
print(classeur_sub1.shape)



# Remove living patients with time_months < 36
# and high risk of death

labelEncoder = LabelEncoder()

classeur_sub1["Failure_first_ttt"] = labelEncoder.fit_transform(classeur_sub1["Failure_first_ttt"])
classeur_sub1["Relapse_after_CR"] = labelEncoder.fit_transform(classeur_sub1["Relapse_after_CR"])
classeur_sub1["Intitial_global_response"] = labelEncoder.fit_transform(classeur_sub1["Intitial_global_response"])


index_u36 = classeur_sub1[ classeur_sub1["time_months"] + 36*classeur_sub1["statut"] +
                            (1-classeur_sub1["Failure_first_ttt"]) *
                            (1-classeur_sub1["Relapse_after_CR"]) *
                            (1-classeur_sub1["Intitial_global_response"]) *
                            (2-classeur_sub1["Intitial_global_response"]) * 36 < 36 ].index

classeur_sub2 = classeur_sub1.drop(index_u36, inplace = False)
print("Final dataset shape, with living patients with too short feedback removed :")
print(classeur_sub2.shape)



# Convert qualitative features to integer

classeur_sub2["Initial_ttt"] = labelEncoder.fit_transform(classeur_sub2["Initial_ttt"])
classeur_sub2["Sex"] = labelEncoder.fit_transform(classeur_sub2["Sex"])
classeur_sub2["Lower_18m"] = labelEncoder.fit_transform(classeur_sub2["Lower_18m"])
classeur_sub2["MKI"] = labelEncoder.fit_transform(classeur_sub2["MKI"]) #
classeur_sub2["INPC"] = labelEncoder.fit_transform(classeur_sub2["INPC"]) #
classeur_sub2["Genomic_class"] = labelEncoder.fit_transform(classeur_sub2["Genomic_class"]) #
classeur_sub2["MYCN"] = labelEncoder.fit_transform(classeur_sub2["MYCN"]) #
classeur_sub2["INRGSS"] = labelEncoder.fit_transform(classeur_sub2["INRGSS"])
classeur_sub2["Primitif_compartment"] = labelEncoder.fit_transform(classeur_sub2["Primitif_compartment"])
classeur_sub2["IDRF"] = labelEncoder.fit_transform(classeur_sub2["IDRF"])
classeur_sub2["NRB_sabliers_variantes"] = labelEncoder.fit_transform(classeur_sub2["NRB_sabliers_variantes"])
classeur_sub2["M_node"] = labelEncoder.fit_transform(classeur_sub2["M_node"])
classeur_sub2["M_bone"] = labelEncoder.fit_transform(classeur_sub2["M_bone"])
classeur_sub2["M_om"] = labelEncoder.fit_transform(classeur_sub2["M_om"])
classeur_sub2["M_liver"] = labelEncoder.fit_transform(classeur_sub2["M_liver"])
classeur_sub2["MSI_Index"] = labelEncoder.fit_transform(classeur_sub2["MSI_Index"])
classeur_sub2["Subtype"] = labelEncoder.fit_transform(classeur_sub2["Subtype"]) #
classeur_sub2["Baseline_LDH"] = labelEncoder.fit_transform(classeur_sub2["Baseline_LDH"]) #
classeur_sub2["Baseline_ratio_VMA_HVA"] = labelEncoder.fit_transform(classeur_sub2["Baseline_ratio_VMA_HVA"]) #
classeur_sub2["Baseline_risk_group"] = labelEncoder.fit_transform(classeur_sub2["Baseline_risk_group"])
classeur_sub2["Visual_uptake"] = labelEncoder.fit_transform(classeur_sub2["Visual_uptake"])
classeur_sub2["Visual_heterogeneity"] = labelEncoder.fit_transform(classeur_sub2["Visual_heterogeneity"])


# For this feature, use 0.0 to fill NaN values
classeur_sub2["Post_ttt_siopen"].fillna(0.0, inplace=True)



# Add the new label to predict "Life_exp"
# 1: < 18 months
# 2: < 36 months
# 3: >= 36 months

Life_exp = []

for i in range(classeur_sub2.shape[0]):
    if classeur_sub2["statut"].iloc[i] == 0:
        Life_exp.append(3)

    else:
        if classeur_sub2["time_months"].iloc[i] < 18:
            Life_exp.append(1)

        elif classeur_sub2["time_months"].iloc[i] < 36:
            Life_exp.append(2)

        else:
            Life_exp.append(3)

classeur_sub2["Life_exp"] = Life_exp


# Save the cleaned dataset
classeur_sub2.to_excel("clean_dataset.xlsx", index=False, startrow=0)
