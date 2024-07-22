class NepaliDateConverter:
    BS_YEAR_START = 1970
    BS_MONTH_START = 1
    BS_DAY_START = 1
    BS_YEAR_END = 2100
    
    BS = [
        [0, 30, 32, 31, 32, 31, 30, 29, 30, 29, 31, 30, 30],  # 1970
        [0, 31, 32, 31, 32, 31, 30, 29, 30, 29, 31, 30, 30],
        # Add more years as needed
    ]
    
    def __init__(self):
        pass
    
    def is_leap_year(self, year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
    def gregorian_to_nepali(self, year, month, day):
        diff_year = 56
        diff_month = 8
        diff_day = 17

        # Nepali year
        np_year = year + diff_year

        # Nepali month
        if month <= 4:
            np_year -= 1
            np_month = month + 8
        else:
            np_month = month - 4

        # Nepali day
        np_day = day + diff_day
        if np_day > 30:
            np_month += 1
            np_day -= 30

        if np_month > 12:
            np_year += 1
            np_month -= 12

        return np_year, np_month, np_day
