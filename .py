The program must accept N messages shared between the two persons A and B in a single day (from 00:00:00 to 23:59:59) as the input. Each message contains the author's name, the time of the message sent (in 24-hour 
format HH:MM:SS) and the content of the message. The program must sort and print those N messages in the chronological order as the output. Note: More than one messages at a time are not possible.

Example Input/Output 1:
Input:
4
A 07:32:21 u can upload first
A 07:32:30 then you can tag
A 07:33:10 please ping me once it is done.
B 07:32:41 okay

Output:
A:u can upload first
A:then you can tag
B:okay
A:please ping me once it is done.
Explanation:
The first message u can upload first was sent at 07:32:21.
The second message then you can tag was sent at 07:32:30.
The third message please ping me once it is done was sent at 07:33:10.
The fourth message okay was sent at 07:32:41.
After sorting the 4 messages in chronological order, the order of the messages become 1, 2, 4 and 3.
Hence the output is
A:u can upload first
A:then you can tag
B:okay
A:please ping me once it is done.

Example Input/Output 2:
Input:
5
A 12:15:29 hey are you there?
B 12:59:55 bye see you later
A 12:45:13 have you done the work?
B 12:30:16 yes
B 12:45:59 yes i have completed

Output:
A:hey are you there?
B:yes
A:have you done the work?
B:yes i have completed
B:bye see you later

Example Input/Output 3:
Input:
6
A 15:17:03 SURE
B 15:16:46 Can we go for a movie?
B 15:15:54 are you free this weekend?
A 15:15:24 Hi, B!
A 15:16:17 I think so, why?
B 15:13:03 HELLO, AI

Output:
B:HELLO, A!
A:Hi, B!
B:are you free this weekend?
A:l think so, why?
B:Can we go for a movie?
A:SURE
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from datetime import datetime
N = int(input())
messages = []
for _ in range(N):
    author,time_str,content = input().split(maxsplit=2)
    messages.append((author,time_str,content))
ordered_messages = sorted(messages, key=lambda x: datetime.strptime(x[1], '%H:%M:%S'))
for message in ordered_messages:
    print(f"{message[0]}:{message[2]}")
