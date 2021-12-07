#Marco Troper
#December 7th, 2021

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data.csv")

#First Plots
df_female = df.loc[df["gender"] == "female",
["pref_o_attractive", "pref_o_sincere","pref_o_intelligence","pref_o_funny","pref_o_ambitious", "pref_o_shared_interests"]]
df_male = df.loc[df["gender"] == "male",
["pref_o_attractive", "pref_o_sincere","pref_o_intelligence","pref_o_funny","pref_o_ambitious", "pref_o_shared_interests"]]
female = pd.DataFrame({'value': [df_female['pref_o_attractive'].sum(),
                                 df_female["pref_o_sincere"].sum(),
                                 df_female['pref_o_intelligence'].sum(),
                                 df_female['pref_o_ambitious'].sum(),
                                 df_female['pref_o_shared_interests'].sum()]},
index=["Physical Attractiveness", "Sincere", "Intelligence", "Ambitious", "Shared Interests"])
male = pd.DataFrame({'value': [df_male['pref_o_attractive'].sum(),
                               df_male["pref_o_sincere"].sum(),
                               df_male['pref_o_intelligence'].sum(),
                               df_male['pref_o_ambitious'].sum(),
                               df_male['pref_o_shared_interests'].sum()]},
index=["Physical Attractiveness", "Sincere", "Intelligence", "Ambitious", "Shared Interests"])

plot_f = female.plot.pie(y="value", legend=None,autopct='%1.1f%%', title="What traits do females value in their partner?")
plot_m = male.plot.pie(y="value", legend=None,autopct='%1.1f%%', title="What traits do males value in their partner?")
plt.show()

#Second plot

age_list = []
#I use 37 because that is the last age that has enough data to include in the plot
for i in range(int(df["age"].min()), 37):
    age_list.append(df.loc[df["age"] == i, ["pref_o_attractive",
                                            "pref_o_sincere",
                                            "pref_o_intelligence",
                                            "pref_o_funny",
                                            "pref_o_ambitious",
                                            "pref_o_shared_interests"]])
attractive = []
sincere = []
intelligence = []
funny = []
ambitious = []
interests = []
for a in age_list:
    x = 0
    for b in range(6):
        x += a.iloc[:, b].sum()
    attractive.append(a.iloc[:, 0].sum() / x)
    sincere.append(a.iloc[:, 1].sum() / x)
    intelligence.append(a.iloc[:, 2].sum() / x)
    funny.append(a.iloc[:, 3].sum() / x)
    ambitious.append(a.iloc[:, 4].sum() / x)
    interests.append(a.iloc[:, 5].sum() / x)
ages = []
for i in range(18,37):
    ages.append((i))
data = pd.DataFrame({
    "Attractiveness": attractive,
    "Sincerity": sincere,
    "Intelligence":intelligence,
    "Funny":funny,
    "Ambition":ambitious,
    "Shared interests": interests},
    index = ages
)
lines = data.plot.line(title="Preferred Characteristics as a Function of Age")
lines.set_xlabel("Age (years)")
lines.set_ylabel("Percentage (%)")
plt.show()

#Third Plot

traits = ["pref_o_attractive", "pref_o_sincere", "pref_o_intelligence", "pref_o_funny", "pref_o_ambitious", "pref_o_shared_interests"]
frames = []
frames.append(df.loc[df["field"] == "business", traits])
frames.append(df.loc[df["field"] == "law", traits])
frames.append(df.loc[df["field"] == "social work", traits])
frames.append(df.loc[df["field"] == "electrical engineering", traits])

attractive = []
sincere = []
intelligence = []
funny = []
ambitious = []
shared_interests = []
for profession in frames:
    sum = profession.iloc[:,0].sum() + \
          profession.iloc[:,1].sum() + \
          profession.iloc[:,2].sum() + \
          profession.iloc[:,3].sum() + \
          profession.iloc[:,4].sum() + \
          profession.iloc[:,5].sum()
    attractive.append((profession.iloc[:,0].sum() / sum))
    sincere.append((profession.iloc[:,1].sum() / sum))
    intelligence.append((profession.iloc[:,2].sum() / sum))
    funny.append((profession.iloc[:,3].sum() / sum))
    ambitious.append((profession.iloc[:,4].sum() / sum))
    shared_interests.append((profession.iloc[:,5].sum() / sum))
index = ["Business", "Law", "Social Work", "Electrical Engineering"]
df = pd.DataFrame({'Attractive': attractive,
                   'Sincere': sincere,
                   "Intelligence": intelligence,
                   "Funny": funny,
                   "Ambitious": ambitious,
                   "Shared Interests": shared_interests
                   }, index=index)
ax = df.plot.bar(stacked=True)
plt.title("Proportions of preferred characteristics by field")
plt.show()
