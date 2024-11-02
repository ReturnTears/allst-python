import datetime
current_time = datetime.datetime.now().hour
username = "Alice"

if 5 <= current_time < 12:
    print("Good Morning, %s" % username)
elif 12 <= current_time < 18:
    print("Good Afternoon, %s" % username)
else:
    print(f"Good Evening, {username}")


