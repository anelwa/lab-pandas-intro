# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
import pandas as pd

df = pd.DataFrame({
    'name': ["Tom", "Lisa", "Peter"],
    'height': [1.68, 1.93, 1.72],
    'weight': [48.4, 89.8, 84.2],
    'id': [1, 2, 3],
    'city': ['Stuttgart', 'Stuttgart', 'Berlin']
})

df['bmi'] = round(df['weight'] / (df['height'] * df['height']), 2)
df["name"] = df["name"].astype("category")
df['id'] = df['id'].astype(str)
#
#
#
#
#
#
#
#
#
#
#
#
# | output-location: fragment
df['height'].mean()
#
#
#
#
#
# | output-location: fragment
df['height'].mean().round(2)
#
#
#
#
#
#
#
#
#
#
#
# | output-location: fragment

print(f"The mean of height is {df['height'].mean():.2f}")
#
#
#
#
#
#
# | output-location: fragment
df['height'].median()
#
#
#
#
#
# | output-location: fragment
df['height'].std()
#
#
#
#
#
#
#
#
#
#
#
# | output-location: fragment
df.describe()
#
#
#
#
#
#
# | output-location: fragment
df.describe().T.round(2)
#
#
#
#
#
#
#
#
#
# | output-location: fragment
df[['height', 'city']].groupby(['city']).describe().round(2).T
#
#
#
#
#
#
#
#
#
#
#
#
# | output-location: fragment
df.describe(include="category").T
#
#
#
#
#
#
#
#
#
#
#
# | output-location: fragment
df['city'].value_counts()
#
#
#
#
#
#
#
#
# | output-location: fragment
df['city'].value_counts().Stuttgart
#
#
#
#
#
#
#
#
#
#
#
# | output-location: fragment
count_stuttgart = df['city'].value_counts().Stuttgart

print(f"There are {count_stuttgart} people from Stuttgart in the data")
#
#
#
#
#
#
#
#
#
#
#
#
#
# make a list of numerical columns
list_num = ['height', 'weight']
#
#
#
#
#
# | output-location: fragment

# calculate median for our list and only show 4 digits, then make a new line (\n)
for i in list_num:
    print(f'Median of {i} equals {df[i].median():.4} \n')
#
#
#
#
#
#
#
# | output-location: fragment

for i in list_num:
    print(f'Column: {i}  \n  {df[i].describe().round(2)}   \n')   
#
#
#
#
#
#
#
#
# Pandas needs the module matplotlib to create plots
import matplotlib.pyplot as plt

# show plot output in Jupyter Notebook
%matplotlib inline
#
#
#
#
#
#
# | output-location: fragment
df.boxplot(column=['weight']);
#
#
#
#
#
#
# | output-location: fragment

# obtain plots for our list
for i in list_num:
    df.boxplot(column=[i])
    plt.title("Boxplot for " + i)
    plt.show()
#
#
#
#
