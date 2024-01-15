class Node: 
	# Khởi tạo 1 node 
      def __init__(self, x): # khởi tạo 2 thuộc tính của node là giá trị và con trỏ
            self.val = x  
            self.next = None

# Linked List class 
class SinglyLinkedList: 
	# Khởi tạo LinkedList  
      def __init__(self): 
            self.head = None
# Câu 1 : chèn 1 node mới với giá trị x vào đầu danh sách 
      def addToHead(self,x):
            new_node = Node(x) # tạo ra một Node mới với giá trị x 
            new_node.next = self.head  # liên kết new_node với object đầu tiên của danh sách
            self.head = new_node # thay đổi đối tượng đầu danh sách thành new node 
# Câu 2 : chèn 1 node mới với giá trị x vào cuối danh sách 
      def addToTail(self,x):
            new_node = Node(x)
            if self.head is None: #kiểm tra xem danh sách có trống ko k
                  self.head = new_node # nếu có thì để new_node thành head mới 
                  return
# nếu ko phải danh sách rỗng thì duyệt đến node cuối 
            last = self.head # gán biến last = giá trị head
            while last.next:    #duyệt đến node cuối 
                  last = last.next    
            last.next  = new_node 
# Câu 3 :Thêm một node với giá trị x vào sau Node p
      def addAfter(p,x):
            new_node = Node(x)
            if p not in SinglyLinkedList: 
                  print('Node p bạn nhập vào phải có trong LinkedList')
                  return 
            new_node.next=p.next # trỏ của new node = trỏ của p 
            p.next = new_node # sau đó cho trỏ tiếp theo của p = node 
# Câu 4 : Duyệt danh sách và in thông tin 
      def traverse(self):
          y = self.head # tạo biến y = head để duyệt 
          while y.next : #duyệt danh sách
                print(y.val, end = '->') #in
                y = y.next
          print()
# Câu 5 : Xóa phần tử đầu tiên sau đó in thông tin 
      def deleteformHead(self):
          if self.head is None : 
                return None 
          del_node = self.head  # tạo biến để gán giá trị self head
          self.head = del_node.next  # gán self.head mới thành giá trị tiếp theo 
          return del_node.val
# Câu 6 : Xóa phần tử ở cuối danh sách 
      def deleteformTail(self):
          if self.head is None : # kiểm tra xem chuỗi có rỗng k
                return None 
          del_node = self.head      #tạo biến và gán đến ptu đầu tiên 
          if del_node.next is None : # nếu chuỗi chỉ chứa giá trị đầu thì giá trị đầu dc xóa luôn
                self.head = None
          while del_node.next.next : # duyệt đến khi nào del_node.next.next là none (trỏ đến phần tử cuối cùng )
                del_node = del_node.next # gán giá trị cuối = giá trị tiếp theo
          value = del_node.next.val #lưu giá trị của ptu cuối 
          del_node.next = None #xóa ptu cuối 
          return value 
# Câu 7 : xóa node đằng sau node p và in ra nó 
      def deleteAfter(self,p):
          if not p or not p.next : # nếu p và p.next là none
                return None 
          value = p.next.val 
          p.next = p.next.next # node đằng sau p mới là node sau ptu vừa xóa  
          return value 
# Câu 8 : Xóa node đầu tiên có giá trị là x 
      def del_x(self,x):
          if not self.head :# nếu self head là none  
                return None 
          if self.head.value == x : 
                self.head = self.head.next 
                return 
          del_node = self.head 
          while del_node.next.next : 
                if del_node.next.val == x :
                      del_node.next = del_node.next.next
                      return 
                del_node = del_node.next 
# Câu 9 : tìm kiếm và trả về phần tử có giá trị x
      def search(self,x): 
            cur = self.head
            while cur or cur.value != x : # điều kiện cur != none để đảm bảo chúng ta đã duyệt hết danh sách mà ko có giá trị x thì vòng lặp sẽ dừng 
                  cur = cur.next 
            return cur 
# câu 10 : đếm và trả về số lượng phần tử trong node 
      def count(self):
            count = 0 
            cur = self.head
            while cur : 
                  count += 1
                  cur = cur.next 
            return count 
# Câu 11 xóa node có index i
      def removeByIndex(self,index):
            if index == 0: self.deleteFromHead()
            elif index == self.count() - 1: self.deleteFromTail()
            else: 
                newLink = self.head
                while newLink:
                    if index == 1:
                        newLink.next = newLink.next.next
                        return
                    index -= 1
                    newLink = newLink.next
# Câu 12 sắp xếp 
      def sort(self):
            arr = self.toArray()
            arr.sort()
            newLink = SinglyLinkedList()
            for i in arr:
                  newLink.addToTail(i)
            return newLink
# Câu 13 xóa node p 
      def deleteNodeP(self, nodeP):
            self.addToHead(None)
            newLink = self.head
            while newLink:
                if newLink.next.val == nodeP:
                    newLink.next = newLink.next.next
                    pass
                newLink = newLink.next
            self.deleteFromHead()
# Câu 14 : tạo và trả về thông tin của dãy 
      def toArray(self):
        arr = []
        newLink = self.head
        while newLink:
            arr.append(newLink.val)
            newLink = newLink.next
        return arr
# Câu 15 
      def merge(self, link):
        newLink = self.head
        while newLink.next: newLink = newLink.next
        newLink.next = link.head
# Câu 16 
      def addtoBeforeNodeP(self, nodeP,valueX):
        self.addToHead(None)
        try:
            newNode = Node(valueX)
            newLink = self.head
            while newLink.next.val != nodeP:
                newLink = newLink.next
            newNode.next = newLink.next
            newLink.next = newNode
            
        except: pass
        self.deleteFromHead()
# Câu 17 
      def mergeToList(self, link1):
        arr1 = self.toArray()
        arr2 = link1.toArray()
        arr1.extend(arr2)
        arr1.sort()
        return arr1
# Câu 18 
      def min(self):
        arr = self.toArray()
        return min(arr)
# Câu 19 
      def max(self):
        arr = self.toArray()
        return max(arr)
# Câu 20    
      def sum(self):
        arr = self.toArray()
        return sum(arr)
# Câu 21   
      def avg(self):
        return self.sum() / self.count()
# Câu 22   
      def sorted(self):
           
        arr = self.toArray()
        for index, item in enumerate(arr):
            if arr[index] > arr[index + 1]:
                return False
        return True
# Câu 23
      def insert(self, nopeP):
        arr = self.toArray()
        arr.append(nopeP)
        arr.sort()
        newLink = SinglyLinkedList()
        for i in arr:
            newLink.addToTail(i)
        return newLink
# Câu 24
      def reverse(self):
        arr = self.toArray()
        newLink = SinglyLinkedList()
        for i in arr:
            newLink.addToHead(i)
        return newLink
#Câu 25 
      def sameE(self, link1):
        arr1 = self.head
        arr2 = link1.head
        return arr1 == arr2
linked_list = SinglyLinkedList()
linked_list.addToHead(3)
linked_list.addToHead(2)
linked_list.addToHead(1)
linked_list.addToTail(4)
linked_list.addToTail(5)

linked_list2 = SinglyLinkedList()
linked_list2.addToHead(6)
linked_list2.addToTail(7)

linked_list.traverse()
linked_list2.traverse()

linked_list.merge(linked_list2)
linked_list.traverse()

linked_list.reverse()
linked_list.traverse()

print("Max value:", linked_list.max())
print("Min value:", linked_list.min())
print("Sum:", linked_list.sum())
print("Average:", linked_list.avg())
print("Sorted:", linked_list.sorted())

linked_list.insert(2)
linked_list.traverse()

linked_list.del_node(linked_list.search(4))
linked_list.traverse()

array = linked_list.toArray()
print("Array representation:", array)

linked_list2.addToTail(7)
linked_list2.addToTail(8)

linked_list.attach(linked_list2)
linked_list.traverse()

print("Is same content?", linked_list.isSameContent(linked_list2))
