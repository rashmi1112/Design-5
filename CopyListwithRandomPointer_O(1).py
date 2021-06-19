# TC: O(N) since we have to iterate over all the nodes of the original list. 
# SC: O(1) since we do not use any extra space. 

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: 
            return
        
#         create the clones of the nodes of original list
        curr = head
        while curr: 
            newNode = Node(curr.val)
            newNode.next = curr.next
            curr.next = newNode
            curr = curr.next.next
        
#         establish the random pointers
        curr = head
        while curr:
            if curr.random: 
                curr.next.random = curr.random.next
            curr = curr.next.next
            
#         split the lists
        curr = head
        copyHead = head.next
        while curr:
            if curr.next: 
                copyCurr = curr.next
                curr.next = curr.next.next
                if curr.next: 
                    copyCurr.next = copyCurr.next.next
            curr = curr.next
        
        return copyHead
