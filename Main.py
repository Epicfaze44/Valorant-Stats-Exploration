import pandas as pd #Imports the necessary modules
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns

plt.style.use("dark_background")

df = pd.read_csv("Data.csv")#Reads the data 
df = df.drop(columns = ["Total Plants", "Post-Plant Holds", "Retakes/Defuses"])#Drops the columns that aren't needed

df = df.rename(columns = {"Plant Site" : "Site"})#renames the Plant Site column


plot = sns.barplot(x="Map", y="Retake Success %", data=df, ci= False, color = "#196e5f", hue="Site")
plot.figure.savefig("output.png")


print(df)#prints
