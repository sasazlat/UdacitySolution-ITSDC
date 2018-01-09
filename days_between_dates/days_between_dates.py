###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1) (even though December really has
###    31 days)
###
def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    # YOUR CODE HERE
    if day < daysInMonth(year,month):
        return year, month, day + 1
    if month == 12:
        return year + 1, 1, 1
    else:
        return year, month + 1, 1

#Check if year is lep year
def isLeapYear(year):
    import calendar
    return calendar.isleap(year)

#Return true if date second date is after first one
def isDateBrfore(y1, m1, d1, y2, m2, d2):
    if y2 > y1:
        return True
    if m2 > m1:
        return True
    if d2 > d1:
        return True
    else:
        return False

def daysInMonth(year, month):
    numberOfDays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31 ,30, 31]
    if not isLeapYear(year):
        return numberOfDays[month]
    if month == 2:
        return 29
    return numberOfDays[month]
    


def days_between_dates(y1, m1, d1, y2, m2, d2):
    """
    Calculates the number of days between two dates.
    """
    #assert not isDateBrfore(y2, m2, d2, y1, m1, d1)
    # TODO - by the end of this lesson you will have
    #  completed this function.  You do not need to complete
    #  it yet though!
    days = 0
    while isDateBrfore(y1, m1, d1, y2, m2, d2):
        y1, m1, d1 = nextDay(y1,m1,d1)
        days += 1 
    
    return days

def test_days_between_dates():
    
    # test same day
    assert(days_between_dates(2017, 12, 30,
                              2017, 12, 30) == 0)
    # test adjacent days
    assert(days_between_dates(2017, 12, 30, 
                              2017, 12, 31) == 1)
    # test new year
    assert(days_between_dates(2017, 12, 30, 
                              2018, 1,  1) == 2)
    # test full year difference
    assert(days_between_dates(2012, 6, 29,
                              2013, 6, 29) == 365)
    
    print("Congratulations! Your days_between_dates")
    print("function is working correctly!")
    
test_days_between_dates()
