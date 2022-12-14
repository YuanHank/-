#Queue
class QueueNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedQueue():
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear
    
    def enqueue(self, data):
        if self.front is None:
            self.front = QueueNode(data)
            self.rear = self.front
        else:
            self.rear.next = QueueNode(data)
            self.rear = self.rear.next

    def dequeue(self):
        if self.rear is None:
            return None
        if self.front == self.rear:
            self.rear = None
        self.front = self.front.next

    def peek(self):
        if self.front is None:
            return None
        return self.front.data

    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count
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

queue = LinkedQueue()
queue.enqueue('20')
queue.enqueue('30')
queue.enqueue('40')
# print(queue.peek())#20
# print(queue.size())#3
# queue.dequeue()
# print(queue.peek())#30
# print(queue.size())#2
# queue.dequeue()
# print(queue.peek())#40
# print(queue.size())#1
# queue.dequeue()
# print(queue.peek())#None
# print(queue.size())#0
queue.print()