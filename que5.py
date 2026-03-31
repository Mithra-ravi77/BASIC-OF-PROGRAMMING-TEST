5.logs = input().split()
total = 0
streak = 0
max_streak = 0
for i in logs:
    if i == "ERROR":
        total = total + 1
        streak = streak + 1

        if streak > max_streak:
            max_streak = streak
    else:
        streak = 0

print("Total errors:", total)
print("Longest streak:", max_streak)

output
1w6nh6
Total error:5
Longest streak:3
