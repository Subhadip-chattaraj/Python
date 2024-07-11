def compute(head):
    #return True/False
    arr=[]
    while head:
        arr.append(head.data)
        head=head.next
    st=''.join(map(str,arr))
    i=0
    j=len(st)-1
    while i<j:
        if st[i]!=st[j]:
            return False
        else:
            i+=1
            j-=1
    return True

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


if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):

        n1 = int(input())
        arr1 = input().split()
        ll1 = Llist()
        tail = None
        for nodeData in arr1:
            tail = ll1.insert(nodeData, tail)

        if compute(ll1.head):
            print('true')
        else:
            print('false')
