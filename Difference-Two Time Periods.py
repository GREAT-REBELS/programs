The program must accept the entry time and the exit time of an employee as the input. The time will be in 24-hour format HH:MM:SS. The program must print the difference D (in 24- hour format) between the entry time 
and the exit time as the output

Example Input/Output 1:
Input:
08:12:15
12:34:55
Output: 
04:22:40

Explanation:
The entry time of the employee is 08:12:15.
The exit time of the employee is 12:34:55.
The difference between the entry time and the exit time is 04:22:40.
So 04:22:40 is printed as the output.

Example Input/Output 2:
Input: 
09:30:55 
11:12:15
Output: 
01:41:20
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def time_to_seconds(timeStr):
    HH, MM, SS = map(int, timeStr.split(":"))
    return HH * 3600 + MM * 60 + SS  # converting Hours and Minutes to Seconds

entry_time = input().strip()
exit_time = input().strip()
entry_seconds = time_to_seconds(entry_time)
exit_seconds = time_to_seconds(exit_time)
difference = exit_seconds - entry_seconds
HH = difference // 3600  # converting from Seconds to Hours
difference %= 3600
MM = difference // 60  # converting from Seconds to Minutes
SS = difference % 60
print(f"{HH:02d}:{MM:02d}:{SS:02d}")
