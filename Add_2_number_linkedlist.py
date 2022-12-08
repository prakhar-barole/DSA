#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        # code here
        # return head of sum list
        
        ''' Method 2: converting to array then adding digits'''
        f=first
        arr1=[]
        while(f):
            arr1.append(f.data)
            f=f.next
            
        l1=len(arr1)
        
        s=second
        arr2=[]
        while(s):
            arr2.append(s.data)
            s=s.next
           
        l2=len(arr2)
        
        q=0
        d=0
        i=0
        j=0
        x=1
        
        arr3=[]
        if(l1>=l2):
            i=l1
            j=l2
        else:
            i=l2
            j=l1
        
        for x in range(1,i+1):
            if(x<=j):
                d=(q+arr1[l1-x]+arr2[l2-x])%10
                arr3.insert(0,int(d))
                q=int((q+arr1[l1-x]+arr2[l2-x])/10)
            
            else:
                if(l1>l2):
                    d=(q+arr1[l1-x])%10
                    arr3.insert(0,int(d))
                    q=int(q+arr1[l1-x])/10

                else:
                    d=(q+arr2[l2-x])%10
                    arr3.insert(0,int(d))
                    q=int((q+arr2[l2-x])/10)


        if(int(q)>0):
            arr3.insert(0,int(q))
        
        
        node1=Node(arr3[len(arr3)-1])
        i=len(arr3)-2
        
        while (i>=0):
            node2=Node(0)
            node2.data=arr3[i]
            node2.next=node1
            node1=node2
            i-=1
            
        return node1
        
    
        ''' Method 1 by converting to numbers then adding'''
        '''
        f=first
        arr1=[]
        while(f):
            arr1.append(f.data)
            f=f.next
            
        l1=len(arr1)
        i=pow(10,(l1-1))
        j=0
        n1=0
       
        while(i>=1):
            n1=n1+arr1[j]*i
            j+=1
            i=i/10
        
        
            
        s=second
        arr2=[]
        while(s):
            arr2.append(s.data)
            s=s.next
           
        l2=len(arr2)
        i=pow(10,(l2-1))
        j=0
        n2=0
    
        while(i>=1):
            n2=n2+arr2[j]*i
            j+=1
            i=i/10    
        
        
        s=n1+n2
        
        node1=Node(int(s%10))
        s=s/10
        
     
        while(s>=1):
            node2=Node(0)
            d=s%10
            s=s/10
            node2.data=int(d)
            node2.next=node1
            node1=node2
        
        
        return node1    
    
        '''
        
        
        
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input().split() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input().split() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
        res = Solution().addTwoLists(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends