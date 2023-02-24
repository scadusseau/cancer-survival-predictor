# This code file aims to analyse the dataset in terms of living and dead patients
# with respect to their age and the timelapse between the diagnosis and the
# main event occurence.


import pandas as pd

classeur = pd.read_excel("Classeur_TP_fevr2023.xlsx", header=1)

deces = classeur.loc[classeur["statut"] == 1]
survie = classeur.loc[classeur["statut"] == 0]

print("Dimensions Total:")
print(classeur.shape)

print("\nDimensions deces:")
print(deces.shape)

print("\nDimensions survie:")
print(survie.shape)

print(deces.at[2, "time_months"])

# average event timelapse
time_months_bar_D = deces["time_months"].mean()
time_months_bar_V = survie["time_months"].mean()



# timelapse slices for dead patients
time_months_0_D = 0
time_months_12_D = 0
time_months_24_D = 0
time_months_36_D = 0
time_months_48_D = 0
time_months_60_D = 0
time_months_72_D = 0
time_months_84_D = 0
time_months_96p_D = 0

# timelapse slices for living patients
time_months_0_V = 0
time_months_12_V = 0
time_months_24_V = 0
time_months_36_V = 0
time_months_48_V = 0
time_months_60_V = 0
time_months_72_V = 0
time_months_84_V = 0
time_months_96p_V = 0

for i in range(0, classeur.shape[0]):
    time = classeur.at[i, "time_months"]

    if classeur.at[i, "statut"] == 1:

        if time < 12:
            time_months_0_D += 1

        elif time < 24:
            time_months_12_D += 1

        elif time < 36:
            time_months_24_D += 1

        elif time < 48:
            time_months_36_D += 1

        elif time < 60:
            time_months_48_D += 1

        elif time < 72:
            time_months_60_D += 1

        elif time < 84:
            time_months_72_D += 1

        elif time < 96:
            time_months_84_D += 1

        else:
            time_months_96p_D += 1


    else:

        if time < 12:
            time_months_0_V += 1

        elif time < 24:
            time_months_12_V += 1

        elif time < 36:
            time_months_24_V += 1

        elif time < 48:
            time_months_36_V += 1

        elif time < 60:
            time_months_48_V += 1

        elif time < 72:
            time_months_60_V += 1

        elif time < 84:
            time_months_72_V += 1

        elif time < 96:
            time_months_84_V += 1

        else:
            time_months_96p_V += 1


# average age at diagnosis
age_bar_D = deces["Age_months"].mean()
age_bar_V = survie["Age_months"].mean()

# dead patients' age at diagnosis
age_0_D = 0
age_12_D = 0
age_24_D = 0
age_36_D = 0
age_48_D = 0
age_60_D = 0
age_72_D = 0
age_84_D = 0
age_96_D = 0
age_108_D = 0
age_120p_D = 0


# living patients' age at diagnosis
age_0_V = 0
age_12_V = 0
age_24_V = 0
age_36_V = 0
age_48_V = 0
age_60_V = 0
age_72_V = 0
age_84_V = 0
age_96_V = 0
age_108_V = 0
age_120p_V = 0

for i in range(0, classeur.shape[0]):
    age = classeur.at[i, "Age_months"]

    if classeur.at[i, "statut"] == 1:

        if age < 12:
            age_0_D += 1

        elif age < 24:
            age_12_D += 1

        elif age < 36:
            age_24_D += 1

        elif age < 48:
            age_36_D += 1

        elif age < 60:
            age_48_D += 1

        elif age < 72:
            age_60_D += 1

        elif age < 84:
            age_72_D += 1

        elif age < 96:
            age_84_D += 1

        elif age < 108:
            age_96_D += 1

        elif age < 120:
            age_108_D += 1

        else:
            age_120p_D += 1


    else:

        if age < 12:
            age_0_V += 1

        elif age < 24:
            age_12_V += 1

        elif age < 36:
            age_24_V += 1

        elif age < 48:
            age_36_V += 1

        elif age < 60:
            age_48_V += 1

        elif age < 72:
            age_60_V += 1

        elif age < 84:
            age_72_V += 1

        elif age < 96:
            age_84_V += 1

        elif age < 108:
            age_96_V += 1

        elif age < 120:
            age_108_V += 1

        else:
            age_120p_V += 1


print("---------------------------------------------------------")
print("Analyse du statut des patients.")
print("---------------------------------------------------------")
print("\n\n### DECES ###\n")
print("Duree entre diagnostic et deces:")
print("\t0 - 1 ans : " + str(time_months_0_D) + "\t" + str(round(time_months_0_D / deces.shape[0] * 100, 2)) )
print("\t1 - 2 ans : " + str(time_months_12_D) + "\t" + str(round(time_months_12_D / deces.shape[0] * 100, 2)) )
print("\t2 - 3 ans : " + str(time_months_24_D) + "\t" + str(round(time_months_24_D / deces.shape[0] * 100, 2)) )
print("\t3 - 4 ans : " + str(time_months_36_D) + "\t" + str(round(time_months_36_D / deces.shape[0] * 100, 2)) )
print("\t4 - 5 ans : " + str(time_months_48_D) + "\t" + str(round(time_months_48_D / deces.shape[0] * 100, 2)) )
print("\t5 - 6 ans : " + str(time_months_60_D) + "\t" + str(round(time_months_60_D / deces.shape[0] * 100, 2)) )
print("\t6 - 7 ans : " + str(time_months_72_D) + "\t" + str(round(time_months_72_D / deces.shape[0] * 100, 2)) )
print("\t7 - 8 ans : " + str(time_months_84_D) + "\t" + str(round(time_months_84_D / deces.shape[0] * 100, 2)) )
print("\t+ de 8 ans : " + str(time_months_96p_D) + "\t" + str(round(time_months_96p_D / deces.shape[0] * 100, 2)) )
print("\t duree moyenne (en mois) : " + str(time_months_bar_D) )

print("\n\nAge au diagnostic:")
print("\t0 - 1 ans : " + str(age_0_D) + "\t" + str(round(age_0_D / deces.shape[0] * 100, 2)) )
print("\t1 - 2 ans : " + str(age_12_D) + "\t" + str(round(age_12_D / deces.shape[0] * 100, 2)) )
print("\t2 - 3 ans : " + str(age_24_D) + "\t" + str(round(age_24_D / deces.shape[0] * 100, 2)) )
print("\t3 - 4 ans : " + str(age_36_D) + "\t" + str(round(age_36_D / deces.shape[0] * 100, 2)) )
print("\t4 - 5 ans : " + str(age_48_D) + "\t" + str(round(age_48_D / deces.shape[0] * 100, 2)) )
print("\t5 - 6 ans : " + str(age_60_D) + "\t" + str(round(age_60_D / deces.shape[0] * 100, 2)) )
print("\t6 - 7 ans : " + str(age_72_D) + "\t" + str(round(age_72_D / deces.shape[0] * 100, 2)) )
print("\t7 - 8 ans : " + str(age_84_D) + "\t" + str(round(age_84_D / deces.shape[0] * 100, 2)) )
print("\t8 - 9 ans : " + str(age_96_D) + "\t" + str(round(age_96_D / deces.shape[0] * 100, 2)) )
print("\t9 - 10 ans : " + str(age_108_D) + "\t" + str(round(age_108_D / deces.shape[0] * 100, 2)) )
print("\t+ de 10 ans : " + str(age_120p_D) + "\t" + str(round(age_120p_D / deces.shape[0] * 100, 2)))
print("\t age moyen (en mois) : " + str(age_bar_D) )


print("\n\n\n\n### SURVIE ###\n")
print("Duree entre diagnostic et prise de nouvelle:")
print("\t0 - 1 ans : " + str(time_months_0_V) + "\t" + str(round(time_months_0_V / survie.shape[0] * 100, 2)) )
print("\t1 - 2 ans : " + str(time_months_12_V) + "\t" + str(round(time_months_12_V / survie.shape[0] * 100, 2)) )
print("\t2 - 3 ans : " + str(time_months_24_V) + "\t" + str(round(time_months_24_V / survie.shape[0] * 100, 2)) )
print("\t3 - 4 ans : " + str(time_months_36_V) + "\t" + str(round(time_months_36_V / survie.shape[0] * 100, 2)) )
print("\t4 - 5 ans : " + str(time_months_48_V) + "\t" + str(round(time_months_48_V / survie.shape[0] * 100, 2)) )
print("\t5 - 6 ans : " + str(time_months_60_V) + "\t" + str(round(time_months_60_V / survie.shape[0] * 100, 2)) )
print("\t6 - 7 ans : " + str(time_months_72_V) + "\t" + str(round(time_months_72_V / survie.shape[0] * 100, 2)) )
print("\t7 - 8 ans : " + str(time_months_84_V) + "\t" + str(round(time_months_84_V / survie.shape[0] * 100, 2)) )
print("\t+ de 8 ans : " + str(time_months_96p_V) + "\t" + str(round(time_months_96p_V / survie.shape[0] * 100, 2)) )
print("\t duree moyenne : " + str(time_months_bar_V) )

print("\n\nAge au diagnostic:")
print("\t0 - 1 ans : " + str(age_0_V) + "\t" + str(round(age_0_V / survie.shape[0] * 100, 2)) )
print("\t1 - 2 ans : " + str(age_12_V) + "\t" + str(round(age_12_V / survie.shape[0] * 100, 2)) )
print("\t2 - 3 ans : " + str(age_24_V) + "\t" + str(round(age_24_V / survie.shape[0] * 100, 2)) )
print("\t3 - 4 ans : " + str(age_36_V) + "\t" + str(round(age_36_V / survie.shape[0] * 100, 2)) )
print("\t4 - 5 ans : " + str(age_48_V) + "\t" + str(round(age_48_V / survie.shape[0] * 100, 2)) )
print("\t5 - 6 ans : " + str(age_60_V) + "\t" + str(round(age_60_V / survie.shape[0] * 100, 2)) )
print("\t6 - 7 ans : " + str(age_72_V) + "\t" + str(round(age_72_V / survie.shape[0] * 100, 2)) )
print("\t7 - 8 ans : " + str(age_84_V) + "\t" + str(round(age_84_V / survie.shape[0] * 100, 2)) )
print("\t8 - 9 ans : " + str(age_96_V) + "\t" + str(round(age_96_V / survie.shape[0] * 100, 2)) )
print("\t9 - 10 ans : " + str(age_108_V) + "\t" + str(round(age_108_V / survie.shape[0] * 100, 2)) )
print("\t+ de 10 ans : " + str(age_120p_V) + "\t" + str(round(age_120p_V / survie.shape[0] * 100, 2)) )
print("\t age moyen (en mois) : " + str(age_bar_V) )
