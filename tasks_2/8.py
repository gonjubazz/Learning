# не решено

from datetime import datetime

while True:
    year = datetime.now().year  # год текущий
    try:
        day, month = input().split(" ")
        start_date = datetime(year, int(month), int(day))
        end_date = datetime(year, 12, 31)
    except ValueError as err:
        print(err)
    else:
        break

print((end_date - start_date).days)
