# importing libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

#-----------------------------------------------------------------

# creates the dataframe from the csv file 

df = pd.read_csv("hotel_bookings 2.csv")

#  displaying first 5 rows of the dataframe 

print(df.head())                                                       

# displaying last 5 rows of the dataframe

print(df.tail())                                                      

#-----------------------------------------------------------------
# performing operations on the dataframe


# to display columns of the dataframe

print(df.columns)                                        

# to display info of the dataframe

print(df.info()) 

# to check for any null value

print(df.isnull)

# to give description of the statistical data

print(df.describe())


# to convert date column with object type data into datetime data

df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'], format = 'mixed' )

# to search for the object data type and givimg its description

df.describe(include = 'object')

for col in df.describe(include = 'object').columns :
    print(col)
    print(df[col].unique())


# to drop unrelevant columns

print(df.drop(['company','agent'],axis = 1,inplace =True))

# to drop rows having null values
print(df.dropna(inplace = True))
print(df.isnull())

print(df.describe())

canceled_perc = df['is_canceled'].value_counts(normalize = True)
print(canceled_perc)

#--------------------------------------------------------------------------

# graphical analysis


# displayong the reservation status through pie chart

value = df['is_canceled'].value_counts()

plt.figure(figsize = (10,8))
plt.pie(value, labels = ['Not cancelled','Cancelled'],colors = ['lightblue', 'coral'], shadow = True)
plt.title('Reservation status', color = 'red', size = 20)
plt.legend()
plt.show()


# Reservation status in different years  depicted by a countplot

df['year'] = df['reservation_status_date'].dt.year
print(df.year)

plt.figure(fisize = (10,8))
sns.countplot(x = 'year', hue = 'is_canceled', data = df, palette = 'Reds')
plt.title('Reservation status in deifferent years', color ='lightblue', size = 20)
plt.xlabel('Years', size = 15, color = 'pink')
plt.ylabel('No of reservations', size = 15 , color = 'pink')
plt.legend(['Not cancelled','Cancelled'])
plt.show()



# Reservation status in city and resort hotels

plt.figure(figsize=(10,8))                                                               
ax1 = sns.countplot(x = 'hotel',hue = 'is_canceled',data = df, palette= 'Blues')
plt.title('Reservation Status in Different hotels', color = 'maroon',size = 20)
plt.xlabel('Hotel', size = 15 , color = 'magenta')
plt.ylabel('No of cancellation', size = 15, color = 'magenta')
plt.legend(['Not cancelled', 'Cancelled'])
plt.show()


#  Top 5 countries having most cancellations

country = df.country.value_counts()[:5]
print(country)

plt.figure(figsize = (10,8))
plt.pie(country, labels = country.index , colors = ['skyblue','fuchsia','seagreen','coral','navy'], 
        explode = (0,0.1,0,0.1,0), shadow = True)
plt.title('Top 5 countries having most cancellation', size = 20 , color = 'gray')
plt.legend()
plt.show()

# percentage of repaeted guests in a particular hotel depicted by a pie chart

repeated_guests = df.is_repeated_guest.value_counts()

plt.figure(figsize = (10,8))
plt.pie(repeated_guests, colors= ['lightpink','lightblue'], explode = (0,0.1), autopct = '%1.1f%%',shadow = True )
plt.title('Rate of repetation of guests',size = 20, color = 'r' )
plt.legend(['Repeated_guests','Non_repeated guests'])
plt.show()

#-----------------------------------------------------------------------------
