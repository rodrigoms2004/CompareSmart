from datetime import datetime
from pytz import timezone

# 2019-01-12T15:37:40.000Z
def dateToUnixTimeStamp(dateFormat):
    # hour, minute, second, use map to convert values to integer
    time_array = list(map(int, dateFormat.split('T')[1].split('.')[0].split(':')))
    # year, month, day, use map to convert values to integer
    date_array = list(map(int, dateFormat.split('T')[0].split('-')))
    
    result = datetime(
                    date_array[0],  # year
                    date_array[1],  # month
                    date_array[2],  # day
                    time_array[0],  # hour
                    time_array[1],  # minute
                    time_array[2]   # second
                    ).timestamp()
    return int(result)

def unixTimeStampToDate(unixFormat):
    date_obj = datetime.utcfromtimestamp(int(unixFormat))
    date_utc = date_obj.astimezone(timezone('America/Sao_Paulo'))
    fmt = "%Y-%m-%d %H:%M:%S %Z%z"
    return date_utc.strftime(fmt)

    
date_str = '2019-01-12T15:37:40.000Z'
# date_str = '2019-01-12T15:37:40'
print('Original info:', date_str)

date_unix = dateToUnixTimeStamp(date_str)
print('Unix TimeStamp:', date_unix)

date_h = unixTimeStampToDate(date_unix)
print('Date UTC:', date_h)





