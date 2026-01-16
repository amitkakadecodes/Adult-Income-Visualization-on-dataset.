import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
dataframe = pd.read_csv('adult.csv')
#print(dataframe)

#1. Display Top 10 rows of the dataset
#print(dataframe.head(10))


#2. Display Last 10 rows of the dataset
#print(dataframe.tail(10))


#3. Find Shape of Our Dataset
'''
print(dataframe.shape)
#print('Number of Rows: ',dataframe.shape[0])
#print('Number of Columns: ', dataframe.shape[1])
'''


#4. Getting information about our project
#print(dataframe.info())


#5. Fetch random samples from the dataset(50%)
#print(dataframe.sample(frac=0.50, random_state=100))


#6. Check Null Values in the dataset. 
#print(dataframe.isnull().sum())
#sns.heatmap(dataframe.isnull())
#plt.show()


#7. Perform Data cleaning [Replace'?' with Nan]
#print(dataframe.isin(['?']).sum())

dataframe['workclass']=dataframe['workclass'].replace('?',np.nan)
dataframe['occupation']=dataframe['occupation'].replace('?',np.nan)
dataframe['native-country']=dataframe['native-country'].replace('?',np.nan)
#print(dataframe.isin(['?']).sum())
#print(dataframe.isnull().sum())
#print(sns.heatmap(dataframe.isnull()))

#8. Drop all the Missing Values
'''
per_missing = dataframe.isnull().sum()*100/len(dataframe)
#print(per_missing)
dataframe.dropna(how='any',inplace=True)
#print(dataframe.shape)
'''

#9. Check for Duplicate data and drop them
'''
duplicate_data = dataframe.duplicated().any()
#print(duplicate_data)

dataframe = dataframe.drop_duplicates()
print(dataframe.shape)
'''


#10. Get Overall Statistics about the dataframe
'''
#print(dataframe.describe(include = 'all'))
#print(dataframe.columns)
df = dataframe['education'].unique()
print(df)
df1 = dataframe['educational-num'].unique()
print(df1)
'''


#11. Drop the columns education-num, capital-gain and capital-loss
#print(dataframe.columns)
dataframe = dataframe.drop(['educational-num', 'capital-gain', 'capital-loss'], axis=1)
#print(dataframe.columns)


#Univariate Analysis
#12. What is the Distribution of Age Columns

#print(dataframe.columns)
#print(dataframe['age'].describe())
#data = dataframe['age'].hist()
#print(data)


#13. Find Total number of person having age between 17 to 48
#using with and without between method
'''
data = sum((dataframe['age']>=17) & (dataframe['age']<=48))
print(data)
'''
'''
data = sum((dataframe['age'].between(17,48)))
print(data)
'''


#14. What is the distribution of workclass column

#print(dataframe.columns)

#data = dataframe['workclass'].describe()
#print(data)
#print(dataframe['workclass'].hist())
#plt.show()


#15. How many persons having bachelors or masters degree?
'''
#print(dataframe.columns)

#data = dataframe['education']
#print(data)
filter1 = dataframe['education']=='Bachelors'
filter2 = dataframe['education']=='Masters'

dataframe[filter1 | filter2]
print(dataframe)
'''


#16. Bivarite Analysis 
#This is matplotlip
#print(dataframe.columns) 
#print(sns.boxplot(x='income', y='age', data=dataframe))
#plt.show()


#17. Replace salary values ['<=50k', '>50k'] with 0 and 1

#print(dataframe['income'].unique()) 
#print(dataframe['income'].value_counts())
'''
def salary_data(sal):
    if sal == '<=50k':
        return 0
    else:
        return 1

dataframe['encoded_salary']=dataframe['income'].apply(salary_data)

#print(dataframe.head(1))

dataframe.replace(to_replace=['<=50k', '>50k'], value=[0,1], inplace=True)

#print(dataframe.head(1))
data = dataframe
#print(sns.countplot('income'))
#plt.show()
'''


#18. Which workclass getting highest salary
'''
#print(dataframe.columns)
data = dataframe.groupby('workclass')['income'].mean().sort_values(ascending=False)
print(data)
'''

#19. Who has better chances to get salary >50k men or women
'''
dataframe = dataframe.groupby('gender')['income'].mean()
print(dataframe)
'''

#20. Convert workclass columns datatype to category datatype
#print(dataframe.info())
'''
dataframe['workclass']=dataframe['workclass'].astype('category')
print(dataframe.info())
'''
