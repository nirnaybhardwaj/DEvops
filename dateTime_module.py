
from datetime import datetime, timedelta

# Today date and time

# print(datetime.now())

curr_datetime = datetime.now()
print(curr_datetime.date())
print(curr_datetime.time())
print(curr_datetime.month)

# Date formatting 2024/03/14
formated_date = curr_datetime.strftime('%Y=%m=%d')
print(formated_date)

future__date = curr_datetime + timedelta(days=10)
print(future__date)




