import time as time	
from datetime import datetime

my_time = time.time()

months = [
        "", "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]

now = datetime.now()
print("Seconds since January 1, 1970: ", my_time,  " or ", f"{my_time:.2e}", " in scientific notation")

if now.day < 10:
	print(f"{months[now.month]} 0{now.day} {now.year}")
else:
	print(f"{months[now.month]} {now.day} {now.year}")
