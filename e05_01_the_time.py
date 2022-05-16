#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 5.1 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Exercise 5.1: The Time Module

from os import system
from time import gmtime, strftime, localtime
from calendar import timegm


def time_passed(start, end):
    ''' Calculates the amount of time that past between 'start' and 'end'.
    It returns a dictionary in the form: {"days": 5, "hours": 22,
    "minutes": 40, "seconds": 59}.

    You must be careful when calculating those values from the original
    struct_times values, using the correct conversion functions,
    acording to the original time representations

    Of course, 'end' has to be equal of bigger than 'start'.
    Negatives values are alowed for both parameters, they correspond to
    dates before epoch. '0' correspond to epoch.
    '''
    duration = {}
    if start > end:
        print("Error: 'start' must be a time before 'end'")
    elif start == end:
        duration = {
                    "days": 0, "hours": 0,
                    "minutes": 0, "seconds": 0
                    }
    else:
        # Calculates seconds and minutes
        total_seconds = abs(end - start)
        seconds = total_seconds % 60
        total_minutes = total_seconds // 60
        minutes = total_minutes % 60
        # Calculates hours and days
        total_hours = total_minutes // 60
        hours = total_hours % 24
        days = total_hours // 24
        duration = {
                    "days": days, "hours": hours,
                    "minutes": minutes, "seconds": seconds
                    }
    return duration


def print_time_passed(start, end, time_passed):
    start = strftime("%c", start)
    end = strftime("%c", end)
    days = time_passed["days"]
    hours = time_passed["hours"]
    minutes = time_passed["minutes"]
    seconds = time_passed["seconds"]
    d_str1 = f"{days} day(s), "
    d_str2 = f"{hours} hour(s), {minutes} minute(s), "
    d_str3 = f"and {seconds} second(s)."
    duration_string = d_str1 + d_str2 + d_str3
    print(f"Between {start} and {end} passed –both in local time–: ",
          duration_string)


if __name__ == "__main__":
    system('clear')
    # Stablishes epoch's value:
    epoch = gmtime(0)
    # Stablishes 'start' and 'end' both in UTC and seconds-since-epoch
    # representations:
    start_utc, end_utc = epoch, gmtime()
    start, end = timegm(start_utc), timegm(end_utc)
    # Calculates the time past between 'start' and 'end'
    # using a pre-defined function:
    duration = time_passed(start, end)
    # Prints the dates in local representations and the time that
    # passed between them:
    start_local, end_local = localtime(start), localtime(end)
    print_time_passed(start_local, end_local, duration)
    print("\n\n")
