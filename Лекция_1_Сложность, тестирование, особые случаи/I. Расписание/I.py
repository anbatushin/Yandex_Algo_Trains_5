n = int(input())
year = int(input())

if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    count = 366
else:
    count = 365

lst = [52] * 7
delta = [0] * 7
dct = {}
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]
for i in range(12):
    dct[months[i]] = i
# print(dct)
holidays = [[] for i in range(12)]
for i in range(n):
    s = input().split()
    holidays[dct[s[1]]].append(int(s[0]))

# print(holidays)

start = input()
index = days.index(start)
lst[index] += 1
if count == 366:
    if index == 6:
        lst[0] += 1
    else:
        lst[index + 1] += 1

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if count == 366:
    days_in_month[1] += 1

# print(lst)

for month in holidays:
    if month:
        day = 0
        for i in range(holidays.index(month)):
            day += days_in_month[i]
        for elem in month:
            # print(elem)
            delta[(index + day + elem - 1) % 7] += 1

# print(lst)
# print(delta)

for i in range(7):
    for j in range(7):
        if i != j:
            lst[i] += delta[j]

# print(lst)
# print(delta)

print(days[lst.index(max(lst))], days[lst.index(min(lst))])
