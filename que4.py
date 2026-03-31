4.amount = int(input())
location = input()
time = input()
failed_attempts = int(input())
if failed_attempts >= 3:
    print("Risk Level: LOCK")
else:
    risk = 0
    if amount > 50000:
        risk = risk + 1
    hour = int(time[0:2])   # take hour part
    if hour < 5:
        risk = risk + 1
    if location == "new":
        risk = risk + 1
    if risk >= 2:
        print("Risk Level: High")
    else:
        print("Risk Level: Low")

output
60000
new
03:00
1
Risk Level: High



   
