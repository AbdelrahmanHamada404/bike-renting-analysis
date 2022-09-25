import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
       city = input("please enter ur city :").strip()
       cities=["chicago" , "new york city" , " washington" ]
       if city in cities:
           print(city)
           break
       else:
           print("error please try again")
           continue


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("please enter ur month :").strip()
        months = ["junuary", "february" ,"march" ,"april", "may", "june", "all"]
        if month in months:
            print(month)
            break
        else:
            print("error please try again")
            continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input("please enter ur day :").strip()
        days=["monday" , "tuesday" , "wednesday" , "Thursday" , "friday" , "Saturday" ,"sunday" ,"all"]
        if day in days:
            print(day)
            break
        else:
            print("error please try again")
            continue
            
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(CITY_DATA[city])

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start time']=pd.to_datetime(df['Start Time'])
    #print(df['Start Time'])
    # TO DO: display the most common month

    df['month']=df['Start time'].dt.month
    print("The most common month : ",df['month'].mode()[0])
    # TO DO: display the most common day of week
    df['day']=df['Start time'].dt.day_name()
    print("The most common day : ",df['day'].mode()[0])

    # TO DO: display the most common start hour
    df['hour']=df['Start time'].dt.hour
    print("The most common start hour : ",df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most common Start station : ",df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("The most common End station : ",df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print("The most frequent combination of start and end station : ",(df['Start Station'] + df['End Station']).mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time",df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("The mean of the trip : ",df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count of types : " , user_types)
    # TO DO: Display counts of gender
    genders= df['Gender'].value_counts()
    print("The count of gender : " , genders)
    
    # TO DO: Display earliest, most recent, and most common year of birth
    birthDay_min= df ['Birth Year'].min()
    print("The most recent year : ",birthDay_min)
    
    birthDay_max = df ['Birth Year'].max()
    print("The earliest year : ",birthDay_max)
    
    birthDay_mode = df ['Birth Year'].mode()[0]
    print("the most common year of birth : ",birthDay_mode)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
