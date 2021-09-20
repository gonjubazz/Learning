data = int(input())

months = {
    "1": "winter",
    "2": "winter",
    "3": "spring",
    "4": "spring",
    "5": "spring",
    "6": "summer",
    "7": "summer",
    "8": "summer",
    "9": "autumn",
    "10": "autumn",
    "11": "autumn",
    "12": "winter",
}

if data > 12 or data<1:
    print("NO")
else:
    print(months[str(data)])