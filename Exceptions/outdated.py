months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date_typed = input("Date:")
    if "/" in date_typed:
        month, day, year = date_typed.split("/")
        if int(month) > 12 or int(day) > 31:
            pass
        else:
            day, month, year = int(day), int(month), int(year)
            print(year, "-", f"{day:02}", "-", f"{month:02}", sep="")
            break
    elif "," in date_typed:
        month, day, year = date_typed.split(" ")
        if month in months:
            month = months.index(month) + 1
        else:
            pass
        day = day.replace(",", "")
        if int(month) > 12 or int(day) > 31:
            pass
        else:
            day, month, year = int(day), int(month), int(year)
            print(year, "-", f"{day:02}", "-", f"{month:02}", sep="")
            break
