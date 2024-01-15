class Node2:
    def __init__(self,data=None):
        self.data=data
        self.next=None
        self.prev=None
class LinkedList2:
    def __init__(self):
        self.head=None
    def addToHead(self,x):
        new=Node2(x)
        new.next=self.head
        if self.head is not None:
            self.head.prv=new
        self.head=new
    def addToTail(self,x):
        new=Node2(x)
        if self.head is None:
            self.head=new
        else:
            last=self.head
            while last.next:
                last=last.next
            last.next=new
            new.prev=last
    def addAfter(self,p,x):
        new=Node2(x)
        curr=self.head
        while curr:
            if curr.data==p:
                break
            curr=curr.next
        if curr is not None:
            return
        new.prv=curr
        new.next=curr.next
        if curr.next is not None:
            curr.next.prv=new
        curr.next=new
    def traverse(self):
        curr=self.head
        while curr:
            print(curr.data)
            curr=curr.next
    def deleteFromHead(self):
        if self.head is None:
            return
        else:
            self.head.next.prv=None
            self.head=self.head.next
    def deleteFromTail(self):
        if self.head is None:
            return
        curr=self.head
        prev=curr
        while curr.next:
            prev=curr
            curr=curr.next
        if prev is None:
            self.head=None
        else:
            prev.next=None
            curr=None
    def deleteAter(self,p):
        curr=self.head
        if curr.data is None:
            self.deleteFromHead()
        while curr:
            if curr.data==p:
                break
            curr=curr.next
        if curr is None or curr.next is None:
            return
        delete=curr.next
        curr.next=delete.next
        if delete.next is not None:
            delete.next.prev=curr
         delete=None
    def delete(self,x):
        curr=self.head
        prev=None
        if curr.data==x:
            self.deleteFromHead()
        while curr:
            if curr.data==x:
                break
            curr=curr.next
        if curr is None:
            return
        if curr.prev is None:
            self.head=curr.next
        else:
            curr.prev.next=curr.next
        if curr.next is not None:
            curr.next.prev=curr.prev
    def search(self, x):
        curr = self.head
        index = 0 
        while curr is not None:
            if curr.data == x:
                return index
            curr = curr.next
            index += 1
        return -1
    def count(self):
        num=0
        curr=self.head
        while curr is not None:
            num+=1
            curr=curr.next
        return num
    def deleteIndex(self, i):
        if self.head is None:
            return
        curr = self.head
        if i == 0:
            self.head = curr.next
            if curr.next is not None:
                curr.next.prev = None
            return
        for _ in range(i-1):
            curr = curr.next
            if curr is None:
                break
        if curr is None or curr.next is None:
            return
        next_ = curr.next.next
        if next_ is not None:
            next_.prev = curr
        curr.next = next_
    def sort(self):
        if self.head is None:
            return
        else:
            current = self.head
            while current is not None:
                index = current.next
                while index is not None:
                    if current.data > index.data:
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index = index.next
                current = current.next
    def deleteNode(self, p):
        curr = self.head
        while curr is not None and curr.data != p:
            curr = curr.next
        if curr is None:
            return
        if curr.prev is not None:
            curr.prev.next = curr.next
        if curr.next is not None:
            curr.next.prev = curr.prev
        if curr == self.head:
            self.head = curr.next
    def merge(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.data < list2.data:
            list1.next = self.merge(list1.next, list2)
            list1.next.prev = list1
            list1.prev = None
            return list1
        else:
            list2.next = self.merge(list1, list2.next)
            list2.next.prev = list2
            list2.prev = None
            return list2
    def toArray(self):
        res = []
        curr = self.head
        while curr:
            res.append(curr.data)
            curr = curr.next
        return res
    def addBefore(self, x, p):
        new = Node(x)
        curr = self.head
        while curr is not None and curr.data != p:
            curr = curr.next
        if curr is None:
            return
        new.next = curr
        new.prev = curr.prev
        if curr.prev is not None:
            curr.prev.next = new
        curr.prev = new
        if curr == self.head:
            self.head = new
    def attach(self, list1, list2):
        if list1.head is None:
            list1.head = list2.head
        else:
            curr1 = list1.head
            while curr1.next is not None:
                curr1 = curr1.next
            curr1.next = list2.head
            list2.head.prev = curr1

    def max_(self):
        if self.head is None:
            return None
        max_val = self.head.data
        curr = self.head.next
        while curr:
            if curr.data > max_val:
                max_val = curr.data
            curr = curr.next
        return max_val

    def min_(self):
        if self.head is None:
            return None
        min_val = self.head.data
        curr = self.head.next
        while curr:
            if curr.data < min_val:
                min_val = curr.data
            curr = curr.next
        return min_val

    def sum_(self):
        total = 0
        curr = self.head
        while curr:
            total += curr.data
            curr = curr.next
        return total

    def avg(self):
        total = 0
        count = 0
        curr = self.head
        while current:
            total += curr.data
            count += 1
            curr = curr.next
        return total / count if count > 0 else None
    def sorted_(self):
        if self.head is None:
            return True
        current = self.head
        while current.next is not None:
            if current.data > current.next.data:
                return False
            current = current.next
        return True
    def insert(self, x):
        new_node = Node2(x)
        if self.head is None or self.head.data >= new_node.data:
            new_node.next = self.head
            new_node.prev = None
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None and curr.next.data < new_node.data:
                curr = curr.next
            new_node.next = curr.next
            if curr.next is not None:
                curr.next.prev = new_node
            curr.next = new_node
            new_node.prev = curr
    def reverse(self):
        temp = None
        curr = self.head
        while curr is not None:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.prev
        if temp is not None:
            self.head = temp.prev
    def same(self, list1, list2):
        while list1 and list2:
            if list1.data != list2.data:
                return False
            list1 = list1.next
            list2 = list2.next
        return list1 == list2
    
class Node3:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class CircularLinkedList2:
    def __init__(self):
        self.head = None

    def addToHead(self, x):
        new = Node3(x)
        if self.head is None:
            self.head = new
            new.next = new
            new.prev = new
        else:
            new.next = self.head
            new.prev = self.head.prev
            self.head.prev.next = new
            self.head.prev = new
            self.head = new

    def addToTail(self, x):
        new = Node3(x)
        if self.head is None:
            self.head = new
            new.next = new
            new.prev = new
        else:
            new.next = self.head
            new.prev = self.head.prev
            self.head.prev.next = new
            self.head.prev = new

    def traverse(self):
        if self.head is None:
            return
        curr = self.head
        while True:
            print(curr.data)
            curr = curr.next
            if curr == self.head:
                break
    def deleteFromHead(self):
        if self.head is None:
            return
        elif self.head.next == self.head:
            self.head = None
        else:
            self.head.prev.next = self.head.next
            self.head.next.prev = self.head.prev
            self.head = self.head.next

    def deleteFromTail(self):
        if self.head is None:
            return
        elif self.head.next == self.head:
            self.head = None
        else:
            self.head.prev.prev.next = self.head
            self.head.prev = self.head.prev.prev

    def deleteAfter(self, p):
        curr = self.head
        while curr is not None and curr.data != p:
            curr = curr.next
            if curr == self.head:
                return
        if curr is None or curr.next == self.head:
            return
        curr.next.next.prev = curr
        curr.next = curr.next.next

    def delete(self, x):
        curr = self.head
        if curr is None:
            return
        while curr.data != x:
            curr = curr.next
            if curr == self.head:
                return
        if curr.next != self.head:
            curr.next.prev = curr.prev
        if curr.prev != self.head:
            curr.prev.next = curr.next
        if curr == self.head:
            self.head = curr.next

    def deleteIndex(self, i):
        if self.head is None:
            return
        curr = self.head
        for _ in range(i):
            curr = curr.next
            if curr == self.head:
                return
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        if curr == self.head:
            self.head = curr.next
    def sort(self):
        curr = self.head
        if self.head is None:
            return
        else:
            while True:
                index = curr.next
                while index != self.head:
                    if curr.data > index.data:
                        temp = curr.data
                        curr.data = index.data
                        index.data = temp
                    index = index.next
                curr = curr.next
                if curr == self.head:
                    break
    def deleteNode(self, p):
        curr = self.head
        while curr is not None and curr.data != p:
            curr = curr.next
            if curr == self.head:
                return
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        if curr == self.head:
            self.head = curr.next
    def toArray(self):
        res = []
        curr = self.head
        while True:
            res.append(curr.data)
            curr = curr.next
            if curr == self.head:
                break
        return res
    def merge(self, list1, list2):
        if list1.head is None:
            return list2
        if list2.head is None:
            return list1

        head1 = list1.head
        head2 = list2.head
        dummy = Node(0)
        tail = dummy

        while True:
            if head1.data <= head2.data:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next

            tail = tail.next

            if head1 == list1.head:
                tail.next = head2
                break
            if head2 == list2.head:
                tail.next = head1
                break

        return dummy.next
    def addBefore(self, x, p):
        new = Node2(x)
        curr = self.head
        while curr.data != p:
            curr = curr.next
            if curr == self.head:
                return
        new.next = curr
        new.prev = curr.prev
        curr.prev.next = new
        curr.prev = new
        if curr == self.head:
            self.head = new
    def attach(self, list1, list2):
        if list1.head is None:
            list1.head = list2.head
        else:
            curr1 = list1.head
            while curr1.next != list1.head:
                curr1 = curr1.next
            curr1.next = list2.head
            curr2 = list2.head
            while curr2.next != list2.head:
                curr2 = curr2.next
            curr2.next = list1.head

    def max_(self):
        if self.head is None:
            return None
        max_val = self.head.data
        curr = self.head.next
        while curr != self.head:
            if curr.data > max_val:
                max_val = curr.data
            curr = curr.next
        return max_val

    def min_(self):
        if self.head is None:
            return None
        min_val = self.head.data
        curr = self.head.next
        while curr != self.head:
            if curr.data < min_val:
                min_val = curr.data
            curr = curr.next
        return min_val

    def sum_(self):
        if self.head is None:
            return 0
        total = 0
        curr = self.head
        while True:
            total += curr.data
            curr = curr.next
            if curr == self.head:
                break
        return total

    def avg(self):
        if self.head is None:
            return None
        total = 0
        count = 0
        curr = self.head
        while True:
            total += curr.data
            count += 1
            curr = curr.next
            if curr == self.head:
                break
        return total / count if count > 0 else None
    def sorted_(self):
        if self.head is None:
            return True
        curr = self.head
        while curr.next != self.head:
            if curr.data > curr.next.data:
                return False
            curr = curr.next
        return True
    def insert(self, x):
        new_node = Node3(x)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        elif self.head.data >= new_node.data:
            new_node.next = self.head
            curr = self.head
            while curr.next != self.head:
                curr= curr.next
            curr.next = new_node
            self.head = new_node
        else:
            curr = self.head
            while curr.next != self.head and curr.next.data < new_node.data:
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node
    def reverse(self):
        prev = None
        curr = self.head
        next_node = None
        while True:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            if curr == self.head:
                break
        self.head.next = prev
        self.head = prev
    def same(self, list1, list2):
        temp1 = list1.head
        temp2 = list2.head
        if temp1 is None and temp2 is None:
            return True
        if (temp1 is None and temp2 is not None) or (temp1 is not None and temp2 is None):
            return False
        while temp2 is not None and temp1 is not None and temp1.data == temp2.data:
            temp1 = temp1.next
            temp2 = temp2.next
            if temp1 == list1.head or temp2 == list2.head:
                break
        return temp1 == list1.head and temp2 == list2.head

            