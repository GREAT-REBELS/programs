The program must accept the N entry time and exit time records of an employee during a day as the input. N records are given in chronological order. The opening time of the office will be the first entry time of 
the employee. The closing time of the office will be the last exit time of the employee. The program must print the total duration the employee takes the break based on the following format.
X Hours Y Minutes
If X is 1, then the format will be 1 Hour Y Minutes.
Note: Entry time and exit time will be in the 24-hour format (HH:MM). 
Entry time and exit time do not occur at the same time. 

Example Input/Output 1:
Input:
2
09:30 11:30
11:45 14:00
Output:
0 Hours 15 Minutes
Explanation:
Here N = 2.
The opening time of the office is 09:30.
The closing time of the office is 14:00.
In the first record, the employee will be inside the office for 2 Hours 0 Minutes.
In the second record, the employee will be inside the office for 2 Hours 15 Minutes.
The total duration the employee takes the break is 0 Hours 15 Minutes.
Hence the output is 0 Hours 15 Minutes

Example Input/Output 2:
Input:
4
08:00 10:10
10:30 13:50
14:30 17:15
17:25 19:11
Output:
1 Hour 10 Minutes
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
N = int(input())
records = []
for _ in range(N):
    entryTime,exitTime = input().split()
    records.append((entryTime,exitTime))
totalBreak = 0 
for i in range(1,N):
    exitTime = records[i-1][1] #Prev record exit time 
    entryTime = records[i][0] #curr record entry time 
    exit_hr,exit_mins = map(int,exitTime.split(':'))
    entry_hr,entry_mins = map(int,entryTime.split(':'))
    #converting entryTime,exitTime to minutes 
    entryMins = entry_hr*60 + entry_mins
    exitMins = exit_hr*60 + exit_mins 
    
    totalBreak+=(entryMins-exitMins)
#converting the totalBreak(is in minutes) into Hours and Minutes
totalBreakHours = totalBreak//60 
totalBreakMinutes = totalBreak%60
print(f"{totalBreakHours} {'Hours' if totalBreakHours!=1 else 'Hour'} {totalBreakMinutes} Minutes")
