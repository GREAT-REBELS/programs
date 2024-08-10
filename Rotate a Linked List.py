Given the head of a singly linked list, the task is to rotate the linked list clockwise by k nodes, i.e., left-shift the linked list by k nodes, where k is a given positive integer smaller than or equal to length 
of the linked list.

Examples:
Input: linkedlist: 2->4->7->8->9 , k = 3
Output: 8->9->2->4->7
Explanation:
Rotate 1: 4 -> 7 -> 8 -> 9 -> 2
Rotate 2: 7 -> 8 -> 9 -> 2 -> 4
Rotate 3: 8 -> 9 -> 2 -> 4 -> 7

Input: linkedlist: 1->2->3->4->5->6->7->8 , k = 4
Output: 5->6->7->8->1->2->3->4
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def rotate(self, head, k):
        tail = head 
        Length = 1 
        
        while tail.next:
            Length+=1 
            tail = tail.next 
        tail.next = head
        
        k = k%Length
        while k:
            head = head.next 
            tail = tail.next 
            k-=1
        tail.next = None 
        
        return head
