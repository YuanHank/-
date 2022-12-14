class node():
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next
## 先進先出，用linklist實踐
class queue():# 很重要!! 要有一項作為紀錄最後一項的值，這樣比較方便
    def __init__(self,front = None,rear =None):
        self.front = front
        self.rear = rear
        
    def enqueue(self,data):#尾端新增元素
        if self.front is None:
            self.front = node(data)
            self.rear = self.front
        else:
            self.rear.next = node(data) #這一步的時候因為原本的self.rear.next會是front一直往後推移，所以只要在這邊增加到 node，會等同於front增加到node
            self.rear = self.rear.next #修正順序，讓現在的尾端成為真正的尾端
        
    def dequeue(self,data):#從前端移除元素
        if self.rear ==None:
            return(None)
        if self.front == self.rear:
            self.rear = None
        self.front = self.front.next
        
    def peek(self): #查看最前端元素
        if self.front.data != None:
            return(self.front.data)
    def size(self): #此佇列的元素量   
        count =1
        current =self.front
        while current.next != None:
            count +=1
            current = current.next
        return(count)

    def print(self):
        current = self.front
        count = 0
        while (current.data !=None):
            count += 1
            print(current.data)
            if current.next == None:
                break
            current = current.next

        if count ==0:
            print(current.data)


new_queue = queue()
new_queue.enqueue(30)
new_queue.enqueue(40)
print(new_queue.size())
new_queue.print()