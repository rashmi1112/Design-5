# TC: O(N) since we iterate over the original linked list exactly once. 
# SC: O(N) as we store the hashmap with all the nodes as keys and the clones of nodes as values. 

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: 
            return 
        
        hmap = {}
        def clone(node): 
            if not node: 
                return None
            
            if node in hmap: 
                return hmap.get(node)
                            
            copyNode = Node(node.val, None, None)
            hmap[node] = copyNode
            return copyNode
        
        curr = head
        copyHead = clone(head)
        
        while curr: 
            copyCurr = clone(curr)
            copyCurr.next = clone(curr.next)
            copyCurr.random = clone(curr.random)
            curr = curr.next
        
        return copyHead
            
            
