1.cs = int(input())
inc = int(input())
emi = int(input())
emp = input()

result = "Approved"
rate = "N/A"
if cs < 600:
    result = "Rejected"
elif cs < 750:
    result = "Review"
else:
    if inc < 25000 or emi > inc / 2:
        result = "Rejected"
    elif emp not in ["Salaried", "Self-Employed"]:
        result = "Rejected"
    else:
        if cs >= 800:
            rate = "7%"
        else:
            rate = "8%"

print("Status:", result)
print("Interest Rate:", rate)

output
780
50000
10000
Salaried
Status: Approved
Interest Rate:8%


