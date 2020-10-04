
daily_sched = dict()
daily_sched["08:00"] = "sport activity"
daily_sched["09:00"] = "shower"
daily_sched["10:00"] = "Breakfast"
print("the length of the dictionary is: ", len(daily_sched))
daily_sched["08:00"] = "Keep Sleeping"
print("our daily schedule is: ", daily_sched)
daily_sched.pop("08:00")
print("After pop command: ", daily_sched)
daily_sched.popitem()
print("After popitem command: ", daily_sched)



