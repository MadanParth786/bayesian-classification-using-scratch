#import libraries
import pandas as pd
import numpy as np 
import math

#import Dataset:
dataset =pd.read_csv(r"C:\Users\Parth Madan\Documents\dataset_03.csv")
dataset

# to classify tupple X:
X=[(dataset["Age"]=="youth"),(dataset["Income"]=="medium"),(dataset["Student"]=="yes"),(dataset["Credit_rating"]=="fair")]

#To find the probability of label class(buys_computer):
buys_yes = dataset[dataset["buys_computer"]=="yes"]["buys_computer"].count()
buys_no = dataset[dataset["buys_computer"]=="no"]["buys_computer"].count()
buys = dataset["buys_computer"].count()
Prob1= buys_yes/buys
print("P(buys_computer=yes):",Prob1)
Prob2 = buys_no/buys
print("P(buys_computer=no):",Prob2)

#to find probability of each attribute of tupple with respect to label class:
youth_yes = dataset[(dataset["Age"]=="youth") & (dataset["buys_computer"]=="yes")]["Age"].count()
prob3=youth_yes/buys_yes
youth_no = dataset[(dataset["Age"]=="youth") & (dataset["buys_computer"]=="no")]["Age"].count()
prob4=youth_no/buys_no
medium_yes = dataset[(dataset["Income"]=="medium") & (dataset["buys_computer"]=="yes")]["Income"].count()
prob5=medium_yes/buys_yes
medium_no = dataset[(dataset["Income"]=="medium") & (dataset["buys_computer"]=="no")]["Income"].count()
prob6= medium_no/buys_no
student_yes = dataset[(dataset["Student"]=="yes") & (dataset["buys_computer"]=="yes")]["Student"].count()
prob7 =student_yes/buys_yes
student_no = dataset[(dataset["Student"]=="yes") & (dataset["buys_computer"]=="no")]["Student"].count()
prob8 =student_no/buys_no
credit_fair_yes = dataset[(dataset["Credit_rating"]=="fair") & (dataset["buys_computer"]=="yes")]["Credit_rating"].count()
prob9 = credit_fair_yes/buys_yes
credit_fair_no = dataset[(dataset["Credit_rating"]=="fair") & (dataset["buys_computer"]=="no")]["Credit_rating"].count()
prob10=credit_fair_no/buys_no

#print the probabilities of each attribute with respect to class:
print("P(age=youth/buys_computer=yes):",prob3)
print("P(age=youth/buys_computer=no):",prob4)
print("P(income=medium/buys_computer=yes):",prob5)
print("P(income=medium/buys_computer=no):",prob6)
print("P(Student=yes/buys_computer=yes:",prob7)
print("P(Student=yes/buys_computer=no:",prob8)
print("P(Credit_rating=fair/buys_computer=yes):",prob9)
print("P(Credit_rating=fair/buys_computer=no):",prob10)

# to find conditional probability with respect to tupple X:
X_yes = prob3*prob5*prob7*prob9
print("P(X/buys_computer=yes):",X_yes)
X_no = prob4*prob6*prob8*prob10
print("P(X/buys_computer=no):",X_no)

# print final result:
if(X_yes>X_no):
    print("Bayesian classifier predicts buys computer = yes")
else:
    print("Bayesian classifier predicts buys computer = no")
    
    
