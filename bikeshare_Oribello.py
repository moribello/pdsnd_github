import pandas as pd
import numpy as np
import calendar as cal
import matplotlib.pyplot as plt
import time

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

# Prompts the user for a city name; if city name not found in CITY_DATA list the current list of keys is given and the user is prompted to select one of those. This means that the CITY_DATA list can be updated without having to change this code
    while True:
            city = input("Which city would you like information for? ").lower()
            if city in CITY_DATA.keys():
                break
            else:
                print("That city doesn't appear to be in the list of cities.")
                print("Please select one of the following:")
                for key in CITY_DATA:
                    print('  ', key.title())

    # Prompts the user for a month name; the user will be prompted if they enter an incorrect month. Note that if the user selects "all" the month value will be set to 0.
    while True:
        avail_months = ['january','february','march', 'april', 'may', 'june', 'all']
        month_name = input("Which month would you like information for? (or \"all\" for all) ").lower()
        if month_name in avail_months:
            month = month_name
            break
        else:
            print('That doesn\'t appear to be a valid month. Please try again, using the full name of the month')

# Prompts the user for a day of the week.

    while True:
        days_of_week = ['sunday','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
        day = input("Enter day of week to filter by (or \"all\" for none)").lower()
        if day not in days_of_week:
            print('That doesn\'t appear to be a valid selection. Please enter the name of a day of the week or \"all\" for none')
        else:
            break

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time']= pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['start_hour'] = df['Start Time'].dt.hour

    # Create a new column that gives Start to End station
    df['Start and End'] = df['Start Station'].str.cat(df['End Station'], sep=" to ")

        # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        while True:
            try:
                months = ['january', 'february', 'march', 'april', 'may', 'june']
                month = months.index(month) +1
                break
            except:
                print("There doesn't appear to be any data for that month. Please try again.")
                break

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # displays the most common month.
    # NOTE: If a user chose to filter by a single month only that month's data will be available; this loop checks and, if the user has filtered by a single month, will remind them of this.
    mc_month = df['month'].mode()[0]
    print(mc_month)
    print("The most popular month to rent a bicycle is", cal.month_name[mc_month])

    # displays the most common day of week
    # NOTE: If a user chose to filter by a single month only that month's data will be available; this loop checks and, if the user has filtered by a single month, will remind them of this.
    mc_day = df['day_of_week'].mode()[0]
    print("The most popular day of the week to rent a bicycle is", mc_day)


    # display the most common start hour
    mc_hour = df['start_hour'].mode()[0]
    # NOTE: For ease in user reading, this loop converts the 24 hour format to 12 hour format.
    am_pm = ()
    if mc_hour > 12:
        mc_hour = mc_hour - 12
        am_pm = "pm"
    else:
        am_pm = "am"
    print("The most common hour of the day to start a trip is", mc_hour, am_pm)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    mc_starts = df['Start Station'].mode()[0]
    mc_starts_value = df['Start Station'].value_counts().index[0]
    print("The most commonly used start station is: ", mc_starts)

    # display most commonly used end station
    mc_ends = df['End Station'].mode()[0]
    print("The most commonly used end station is", mc_ends)

    # display most frequent combination of start station and end station trip
    mc_start_end = df['Start and End'].mode()[0]
    print("The most frequent combination of start station and end station trip is: ", mc_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_min = df['Trip Duration'].sum()
    print("The total number of minutes traveled by all bicycles in this range is {} minutes.".format(total_travel_min))
    total_travel_days = total_travel_min // 1440
    total_travel_hours = (total_travel_min % 1440) // 60
    total_travel_hour_leftover = total_travel_hours % 60

    print("This is {} days, {} hours, {} minutes".format(total_travel_days, total_travel_hours, total_travel_hour_leftover))

    # display mean travel time
    print("The average trip time was {} minutes".format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    try:
        # Display counts of user types
        user_types = df['User Type'].value_counts()
        print("The following are counts for user types: \n")
        print(user_types)

        # Display counts of gender
        gender = df['Gender'].value_counts()
        print("The following are counts for gender: \n")
        print(gender)

        # Display earliest, most recent, and most common year of birth
        earliest_by = int(df['Birth Year'].min())
        mrecent_by = int(df['Birth Year'].max())
        mcommon_by = int(df['Birth Year'].mode())

        print("The earliest birth year is", earliest_by)
        print("The most recent birth year is", mrecent_by)
        print("The most common birth year for subscribers is", mcommon_by)
    except:
        print("There doesn't appear to be any additional user data for that city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def graph_user_data(df):
    try:
        show_usertypes = input("Would you like to see a graph of user type data for this city? ").lower()
        if show_usertypes == "y" or show_usertypes == "yes":
            ut_values = df['User Type'].value_counts().to_list()
            ut_labels = df['User Type'].unique()
            bar_colors = ['pink', 'yellowgreen', 'blue']
            y_pos = np.arange(len(ut_labels))
# Create bars and labels
            plt.bar(ut_labels, ut_values, color=bar_colors)
            plt.xticks(y_pos, ut_labels)
            plt.xlabel('User by Type')
            plt.ion()
            plt.show()
# Prompts for user to press enter to continue
            plt.pause(0.001)
            input("\n Press \'Enter\' to continue \n")
        else:
            print("Ok. \n")

        display = input("Would you like to see a graph of user gender data for this city? ").lower()
        if display == "y" or display == "yes":
            genders = df['Gender'].value_counts().to_list()
            labels = ('Male', 'Female')
            colors = ['blue', 'yellowgreen']
            fig1, ax1 = plt.subplots()
            ax1.pie(genders, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=90)
            ax1.axis('equal')
            plt.ion()
            plt.show()
            plt.pause(0.001)
            input("Press \'Enter\' to continue")
        else:
            print("Ok. \n")
    except:
        print("There doesn't appear to be any data to graph")

def show_rawdata(df):
    count = 0
    while True:
        showdata = input("Would you like to view the next five rows of raw data (y/n)?").lower()
        if showdata == "y":
            for i in range(5):
                print(df.iloc[count])
                count +=1
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        graph_user_data(df)
        show_rawdata(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
