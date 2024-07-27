The program must accept the N entry time and exit time records of an employee during a day as the input. N records are given in chronological order. The program must print the total time the employee worked 
within the office based on the following format. X Hours Y Minutes
If X is 1, then the format will be 1 Hour Y Minutes.
Note:
Entry time and exit time will be in the 24-hour format (HH:MM). 
Entry time and exit time do not occur at the same time.

Example Input/Output 1:
Input:
2
09:52 11:41
13:27 16:55
Output:
5 Hours 17 Minutes
Explanation: Here N = 2.
In the first record, the employee will be inside the office for 1 Hour and 49 Minutes. 
In the second record, the employee will be inside the office for 3 Hours and 28 Minutes. 
The total time the employee worked within the office is 5 Hours and 17 Minutes. Hence the output is 5 Hours 17 Minutes

Example Input/Output 2:
Input:
3
08:00 11:42
12:15 14:50
15:45 17:15
Output:
7 Hours 47 Minutes
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def HHtoMM(time):
    HH, MM = map(int, time.split(":"))
    return HH * 60 + MM

N = int(input())
total_mins = 0
for _ in range(N):
    entry_time, exit_time = input().split()
    total_mins += HHtoMM(exit_time) - HHtoMM(entry_time)
HH = total_mins // 60
MM = total_mins % 60
if HH > 0:
    print(f"{HH} Hours {MM} Minutes")
else:
    print(f"{MM} Minutes")
