
Reverse Linked List

''' Non Recursive Way : using array'''
        '''
        curr=head
        arr=[]
        i=0
        while (curr):
            arr.append(curr.data)
            i+=1
            curr=curr.next
        i=i-1
        
        while(i>=0):
            print(arr[i],end=' ')
            i-=1
            
        print() 
        '''
       
       ''' Non Recursive Method: Using Linked List'''
       '''
         curr=head
        
        nxt=curr.next
        curr.next=None
        
        while(nxt):
            prev=curr
            curr=nxt
            nxt=nxt.next
            curr.next=prev
        return curr    
        '''    
