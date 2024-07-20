In a college, N students have attended a campus interview. The name of each student and the marks scored in the technical round T and the aptitude round A are passed as the input to the program. The interviewer
has decided to select the students who have scored at least X marks in the technical round and Y marks in the aptitude round. The values of X and Y are also passed as the input to the program. The program must 
sort and print the names of selected students based on the marks scored in the technical round in descending order. If two or more students have scored the same marks in the technical round, then those students
must be sorted based on the marks scored in the aptitude round in descending order. If two or more students have scored the same marks in both the technical round and the aptitude round, then those students must 
be sorted based on their names in ascending order. If there is no such student, then the program must print -1 as the output.

Example Input/Output 1:
Input:
6
xyz 65 86
PQR 95 90
BCD 70 92
mno 95 96
Efg 70 90
ABC 70 92
70 85
Output:
mno
PQR
ABC
BCD
Efg
Explanation:
Here X = 70 and Y = 85.
The names of the students who have scored at least 70 marks in the technical round and 85 marks in the aptitude round are PQR, BCD, mno, Efg and ABC.
After sorting the students based on their technical score in descending order, the names become PQR, mno, BCD, Efg and ABC.
Here, the students PQR and mno scored the same marks (95) in the technical round. So they are sorted based on their aptitude marks in descending order. 
Similarly, the students BCD, Efg and ABC the scored same marks (70) in the technical round.
So they are sorted based on their aptitude marks in descending order.
The students BCD and ABC scored the same marks in both the technical round and the aptitude round. So they are sorted based on their names in ascending order.
Hence the output is
mno
POR
ABC
BCD
Efg

Example Input/Output 2:
Input:
3
EFG 60 73
abcd 75 45
Pqr 55 46
75 75
Output:
-1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
N = int(input())
students = []
for _ in range(N):
    name, T, A = input().split()
    students.append([name, int(T), int(A)])
X, Y = map(int, input().split())

students = [student for student in students if (student[1] >= X and student[2] >= Y)]

if not students:
    print("-1")
    quit()
students.sort(key=lambda student: (-student[1], -student[2], student[0]))
for student in students:
    print(student[0])
