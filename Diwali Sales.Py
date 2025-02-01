#EDA Project On Diwali Sales Data

#step 1: Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt # visualizing data
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

#step 2: Load the data
# import csv file
df = pd.read_csv('Diwali Sales Data.csv', encoding= 'unicode_escape')


#step 3: Data overview
print("Dataset information:\n")
print(df.info())

print("\nsummary statistics:\n")
print(df.describe())

print("\nmissing values:\n")
print(df.isnull().sum())

print("\nunique values per column:\n")
print(df.nunique())

("\nDuplicate Rows:",df.duplicated().sum())

#step 4: Handle missing  and  duplicate data
#Drop duplicates
df=df.drop_duplicates()


#step 5: drop unrelated/blank columns
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)

#step 6: drop null values
df.dropna(inplace=True)

#step 7: change data type
df['Amount'] = df['Amount'].astype('int')
df['Amount']=pd.to_numeric(df['Amount'],errors='coerce')

#step 8:initialize list of list
data_test=[['madhav',11],['Gopi',15],['keshav',],['lilita',16]]

#step 9:Create the pandas dataframe using list
df_test=pd.DataFrame(data_test,columns=['Name','Age'])
df_test.dropna()
df_test=df_test.dropna()

#step 10:change data type
df['Amount']=df['Amount'].astype('int')

#step 11:rename column
df.rename(columns= {'Marital_Status':'Shaadi'})

#step 12:describe() method returns description of the data in the DataFrame (i.e. count, mean, std, etc)
print(df.describe())

#step 13: use describe() for specific columns
df[['Age', 'Orders', 'Amount']].describe()

#Visualization
#Gender
# plotting a bar chart for Gender and it's count
plt.figure(figsize = (4,4)) 
ax = sns.countplot(x = "Gender", data = df) 
ax.bar_label(ax.containers[0]) 
plt.title("plotting a bar chart for Gender and it's count")
plt.show()

# plotting a bar chart for gender vs total amount
plt.figure(figsize = (4,4)) 
sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)
plt.title("plotting a bar chart for gender vs total amount")
plt.show()

#Age
plt.figure(figsize = (4,4)) 
ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')
ax.bar_label(ax.containers[0])
plt.title("Age")
plt.show()

# Total Amount vs Age Group
plt.figure(figsize = (4,4)) 
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)
plt.title("Total Amount vs Age Group")
plt.show()

#State
# "total number of orders from top 10 states"
plt.figure(figsize = (4,4))
sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,10)})
sns.barplot(data = sales_state, x = 'State',y= 'Orders')
plt.xticks(rotation=45)
plt.title("total number of orders from top 10 states")
plt.show()


# total amount/sales from top 10 states
plt.figure()
sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Amount')
plt.xticks(rotation=45)
plt.title("total amount/sales from top 10 states")
plt.show()

#Marital Status
plt.figure()
ax = sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(7,5)})
plt.title("Marital Status")
plt.show()

#Marital Status By Gender
plt.figure()
sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')
plt.title("Marital Status By Gender")
plt.show()


#Occupation
plt.figure()
sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation')
ax.bar_label(ax.containers[0])
plt.xticks(rotation=45)
plt.title("Occupation")
plt.show()

#Occupation VS Amount
plt.figure()
sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')
plt.xticks(rotation=45)
plt.title("Occupation VS Amount")
plt.show()


#Product Category
plt.figure()
sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')
ax.bar_label(ax.containers[0])
plt.xticks(rotation=45)
plt.title("Product Category")
plt.show()

#States Sales
plt.figure()
sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')
plt.xticks(rotation=45)
plt.title("States Sales")
plt.show()


#Product ID VS Order
plt.figure()
sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')
plt.xticks(rotation=45)
plt.title("Product ID VS Order")
plt.show()



# top 10 most sold products (same thing as above)
plt.figure()
fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')
plt.title("top 10 most sold products (same thing as above)")
plt.show()



















