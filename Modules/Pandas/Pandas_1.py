import pandas as pd

df = pd.read_csv(r'Book2.csv')  #As long as the file is apart of the project structure there no need to put the path.
print(df)

# Simple calculations

median = df['Salary'].median()  #This will get the Median value
mean = df['Salary'].mean()  #This will get the mean of all the values in the Salary table
sum1 = df['Salary'].sum()  #This will get the sum of all the data set
max1 = df['Salary'].max()  #This will get the max value
min1 = df['Salary'].min()  #This will get the min value
count = df['Salary'].count()  #This will count the number of items in a list
std = df['Salary'].std()  #This will get the Standard deviation in a data set
var = df['Salary'].var()  #This will get the Variance(Standard deviation) in the set

print(var)


# Group by
group_by_sum = df.groupby(['Country']).sum()  #This will group by country and give the sum
group_by_count = df.groupby(['Country'])

# Print Block
print('Mean Salary: ' + str(mean))
print('The sum of Salaries: ' + str(sum1))
