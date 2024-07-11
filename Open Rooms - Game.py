In a game, there are N rooms numbered from 0 to N-1. Each room has a key to open another room or the same room. The keys are unique and numbered from 0 to N-1 to open the respective rooms. Initially, all the 
rooms are locked. A boy has a magical key to open any room but he can open exactly one room using the magical key. The boy continues to open the other rooms using the keys present in the opened rooms. The game 
ends when the boy gets the key of the room where he started the game. The total number of rooms N and the key present in each room are passed as the input to the program. Finally, the program must print the 
maximum number of rooms that can be opened by the boy as the output.

Example Input/Output 1:
Input:
7
5 4 0 3 1 6 2
Output:
4
Explanation:
One of the possible ways to open four rooms is given below.
0-5-6->2->0
Here the maximum number of rooms that can be opened by the boy is 4, so 4 is printed as the output.

Example Input/Output 2:
Input:
9 
6 7 2 0 1 3 4 5 8
Output:
7
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
N = int(input())
rooms = list(map(int, input().split()))
res = 0
for i in range(0, len(rooms)):
    strtkey = rooms[i]
    temp = rooms[i]
    count = 0
    while True:
        currRoomKey = rooms[temp]
        temp = currRoomKey
        count += 1
        if currRoomKey == strtkey:
            res = max(res, count)
            break
print(res)
