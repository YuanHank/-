class node():
    def __init__ (self,data =None):
        self.data = data    
        self.next = None
'''
運作邏輯幾乎和linked list顛倒，注意這邊要與linked list顛倒的原因是因為，資料的推移是從新到舊，雖然使用linkedlist的方式也可達到類似的結果，
但是在linked list內就必須使用while執行很多步驟，而此方式則不需要while(因為不需要使用while就能得到最新的值) ***資料的推移方式很重要!!!!

堆疊(Stack)建立的方法
    push: 新增元素
    pop: 從頂端移除元素
    peek: 查看頂端(top)元素
    size: 查看此堆疊的元素量
'''
class linked_stack():
    def __init__(self,top = None):
        self.top = top  #定義在stack 裡面的top 部分

    def push(self,data): #從頂端增加元素
        if self.top is None:
            self.top = node(data)
            return 
        else:
            current = node(data) #創建一個現在的node
            current.next = self.top #將創建的node的下一個位置放入原先的值
            self.top = current #將新創見的值設定為self.top，這樣的設計會讓self.top.data =>新輸入的值，self.top.next =>舊的值
            return 

    def pop(self):# 從頂端移除元素
        if self.top is None:
            return
        else:
            self.top = self.top.next
            return
        
    def peek(self): #觀看頂端的元素
        if self.top is None:
            return None
        return print('the top element is:',self.top.data)


    def size(self): #觀看總元素量
        current = self.top
        time  = 1
        while current.next:
            time +=1
            current = current.next
        return (print('size of stack is:',time))

if __name__=='__main__':
    stack = linked_stack()
    stack.push(3)
    stack.push(5)
    stack.push(7)
    stack.push(9)
    stack.push(10)
    stack.peek()
    stack.size()
