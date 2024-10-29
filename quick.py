class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Llist:
    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)
        if not self.head:
            self.head = node
            return node
        tail.next = node
        return node

# Function to get the tail of the linked list
def get_tail(node):
    while node and node.next:
        node = node.next
    return node

# Partition function for linked list, using the last node as pivot
def partition(head, end):
    if not head or head == end:
        return head, end, head
    
    pivot = end
    prev, curr = None, head
    tail = pivot
    new_head, new_end = None, None

    while curr != pivot:
        if curr.data < pivot.data:
            if new_head is None:
                new_head = curr
            prev = curr
            curr = curr.next
        else:
            if prev:
                prev.next = curr.next
            temp = curr.next
            curr.next = None
            tail.next = curr
            tail = curr
            curr = temp
    
    if new_head is None:
        new_head = pivot
    
    new_end = tail
    return new_head, new_end, pivot

# Recursive quicksort function
def quick_sort_recursive(head, end):
    if not head or head == end:
        return head

    new_head, new_end, pivot = partition(head, end)

    # Sort the list before pivot
    if new_head != pivot:
        temp = new_head
        while temp.next != pivot:
            temp = temp.next
        temp.next = None

        new_head = quick_sort_recursive(new_head, temp)
        temp = get_tail(new_head)
        temp.next = pivot

    # Sort the list after pivot
    pivot.next = quick_sort_recursive(pivot.next, new_end)
    return new_head

# Wrapper function for quick sort
def quickSort(head):
    end = get_tail(head)
    return quick_sort_recursive(head, end)

# Helper function to print the linked list
def printList(head, dic):
    while head:
        if id(head) not in dic[head.data]:
            print("Don't swap data, swap pointer/node")
            return
        print(head.data, end=' ')
        head = head.next

# Driver code
if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        arr = [int(x) for x in input().split()]
        ll = Llist()
        tail = None
        for nodeData in arr:
            tail = ll.insert(nodeData, tail)
        dic = defaultdict(list)
        nodeID(ll.head, dic)
        resHead = quickSort(ll.head)
        printList(resHead, dic)
        print()
        print("~")
