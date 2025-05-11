def issundays(n, a):
    days = {
        "monday": 6,
        "tuesday": 5,
        "wednesday": 4,
        "thursday": 3,
        "friday": 2,
        "saturday": 1,
        "sunday": 0
    }

    if a.lower() not in days:
        return "Invalid day input"

    start_index = days[a.lower()]
    count = 0

    for i in range(n):
        day_index = (start_index - i) % 7
        if day_index == 0:  # Sunday
            count += 1

    return count


a = input("Enter the day of the week: ")
n = 13
print("Number of Sundays:", issundays(n, a))
