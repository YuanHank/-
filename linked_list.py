'''
    node 用來設計每一個節點，裡面的data指向當今節點的值，而next指向下一個節點的位置，
在python裡面若next裡面放另一個node，則可指向新的node，則內部會包含下一個node的值，
以及指向的下一個node
    * append: 在尾部新增節點
    * insertAt: 在特定位置插入節點
    * removeAt: 刪除特定位置節點
    * remove: 刪除特定資料節點
    * indexOf: 回傳第一個出現指定資料的節點位置，空值則回傳-1
    * isEmpty: 確認是否為空串列
    * size: 串列的長度
    * print: 印出串列所有資料
size回傳長度，而index和python的list相同從0開始運作，因為size會包含到最後一層的None
'''
class Node:#設定Node很重要
    def __init__ (self,data =None,next = None):#給定每個節點以及下一個節點的資訊
        self.data = data
        self.next = next

class LinkedList: #資料的推移是從舊的到新的
    def __init__(self,head = None):
        self.head = head

    def append(self,data):
        if not self.head:
            self.head =Node(data) #如果head沒有資料，則會將Node(data)指派給self.head
            return
        current = self.head #將現在的資訊設定為self.head
        while current.next:#若有下一筆資料則會執行迴圈
            current = current.next#每次執行迴圈會將現在資料往後推移，直到沒有下一個節點的值
        current.next = Node(data)#最後在無下一筆資料的情況下，將欲增加的資料加在下一筆資料的點位上

    def print(self):
        if not self.head:
            print(self.head)
        node = self.head
        while node:
            end = " -> "
            print(node.data, end=end)
            node = node.next

    def remove(self,data):
        if not self.head:
            return
        node = self.head
        while node:
            if node.data ==data:
                node.data = node.next.data
                node.next = node.next.next
                return
            node = node.next
    
    def insertAT(self,insert,insert_data):
        current_index = 0
        node = self.head
        if insert <0 or insert >=self.size():
            raise IndexError('out of range or not giving positive index')
        if insert==0:
            new_node = Node(insert_data,self.head)
            self.head = new_node
            return
        else:
            while node:
                
                if current_index == insert-1:
                    temp_next = node.next
                    temp = Node(insert_data,temp_next)
                    node.next = temp
                    return
                node = node.next #這行很重要，因為要一直讓list後移
                current_index +=1

    def size(self):
        node = self.head
        count = 0
        while node:
            if node !=None:
                count +=1
            node = node.next
        return (count)

    def removeAT(self,index):
        node = self.head
        count = 0
        if index ==0:
            new_node = Node()
            new_node.data = node.next.data 
            new_node.next = node.next.next 
            self.head = new_node
            return
        else:
            while node:
                if count ==index-1:
                    node.next = node.next.next
                    return
                count +=1
                node = node.next

    def indexOF(self,value):
        node = self.head
        count =0
        while node:
            if node.data ==value:
                return count
            count +=1
            if count ==self.size():
                return (-1)
            node = node.next

    def isEmpty(self):
        if self.head == None:
            return(print(True))
        else:
            return(print(False))

ll = LinkedList()

ll.append(10)
ll.append(20)
ll.append(40)
ll.append(60)

#print(ll.print())#10 -> 20 -> None
#ll.removeAT(1)
ll.insertAT(3,70)
#print(ll.size())
print(ll.indexOF(70))
#$ll.isEmpty()
print(ll.print())