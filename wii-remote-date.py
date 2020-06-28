import sys

if len(sys.argv) != 2:
    print("Usage: python wii-remote-date.py <date string>")
    sys.exit(1)
 
if len(sys.argv[1]) < 3:
    print("Invalid string")
    sys.exit(1)

if sys.argv[1][0] == "Z":
    year = "2006"
else:
    year = ord(sys.argv[1][0]) + 1942

if ord(sys.argv[1][1]) >= 49 and ord(sys.argv[1][1]) <= 57:
    month = sys.argv[1][1]
elif sys.argv[1][1] == "O":
    month = "10"
elif sys.argv[1][1] == "N":
    month = "11"
elif sys.argv[1][1] == "D":
    month = "12"

if ord(sys.argv[1][2]) >= 49 and ord(sys.argv[1][2]) <= 57:
    day = sys.argv[1][2]
else:
    day = ord(sys.argv[1][2]) - 55

if int(year) > 2016:
    print("Your year is probably incorrect: " + str(year))

if int(month) > 12:
    print("Your month is probably incorrect: " + str(month))

if int(day) > 31:
    print("Your day is probably incorrect: " + str(day))

print(f"{month}/{day}/{year}")