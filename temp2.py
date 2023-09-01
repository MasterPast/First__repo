from datetime import datetime
import pytz

month = 3
year = 2021
# date = '2021-05-27 17:08:34.149Z'

date = '2021-05-27 17:08:34.149Z'

date = date[:-5:]
print(type(date))
print(date)
date_in = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
print(date_in.strftime('%A %d %B %Y'))
    
    
