# Node Class

class node:
    def __init__(self, val):
        self.data = val
        self.next = None


#class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        # Code here
        curr=head
        arr=[]
        i=0
        while (curr):
            arr.append(curr.data)
            i+=1
            curr=curr.next
        i=i-1
        st=str(arr[i])
        i=i-1
        while(i>=0):
            st=st+" "+str(arr[i])
            
            i-=1
            
        print(st)       

        
class Linked_List:
    def __init__(self):
        self.head=None
        self.tail=None

    def insert(self,val):
        if self.head is None:
            self.head=node(val)
        else:
            self.tail.next=node(val)
            self.tail= self.tail.next

def printList(head):
    tmp=head
    while tmp:
        print(tmp.data,end=' ')
        tmp=tmp.next
    print() 

if __name__=='__main__':
    for i in range(int(input)):
        n=int(input())
        arr=[int(x) for x in input().split()]

        lis =Linked_List 
        for i in arr:
            lis.insert(i)

        newHead= Solution().reverseList(lis.head)
        printList(newHead)             

        
