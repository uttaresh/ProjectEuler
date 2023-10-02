# You are given the following information, but you may prefer to do some research for yourself.
#
#     1 Jan 1900 was a Monday.
#     Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#     A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def solution():
    # Note: Start counting from 0 not 1
    date = 0
    month = 0
    year = 0
    day = 1  # 1 Jan 1900 is a Monday
    match = 0
    while year < 101:
        # checking if this day meets the condition
        if day == 0 and date == 0 and year > 0:
            match += 1

        # logic for incrementing the date and calculating its details
        days_of_this_month = days_of_month[month]
        if days_of_this_month == 28:
            if year % 400 or (year % 100 != 0 and year % 4 == 0):
                days_of_this_month += 1
        date += 1
        month = month + (date // days_of_this_month)
        date = date % days_of_this_month
        year += month // 12
        month = month % 12
        day = (day + 1) % 7
    return match


print(solution())
