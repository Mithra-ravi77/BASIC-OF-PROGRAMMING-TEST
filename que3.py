3.request_count = int(input())
if request_count <= 5:
    print("Status: Allowed")
else:
    print("Status: Blocked (Rate Limit Exceeded)")

output
6
Status: Blocked (Rate Limit Exceeded)
