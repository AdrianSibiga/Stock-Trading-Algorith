from datetime import datetime
from datetime import timedelta

a = datetime.fromisoformat('2011-11-04T00:05')
a = datetime(2011, 11, 4, 0, 5)
b = timedelta(days=10)


print(a + b)