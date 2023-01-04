#Hash Table
class Node:
    def __init__(self, key=None, data=None):
        self.value = {} #使用dictionary 建立在這個node裡面的的對應值
        self.value[key] = data
        self.next = None #預設next為沒有東西
    def __repr__(self):
        return str(self.data)

class LinkedList:
    def __init__(self, head=None):
        self.head = head 
        self.next = None
        self.count = 0

    def __str__(self):
        str_list = []
        current = self.head
        while current:
            str_list.append(str(current.value))
            current = current.next
        return "[" + "->".join(str_list) + "]"

    def __repr__(self):
        return str(self)

class HashTable:
    def __init__(self, size):
        self.size = size 
        self.length = 0
        self.values = [None] * size
        

    def hash(self, key, size): #用來計算對應到的雜湊值，這邊採用與雜湊表大小取mod的方式
        hashCode = 0
        for i in range(len(key)):
            hashCode += ord(key[i])  #將輸入key值得每個字母轉換成ACII後做加總
        return hashCode % size # 取hashCode 值為與現在hashtable大小取mod

    def add(self, key, value):
        code = self.hash(key,self.size)
        node = Node(key = key,data = value)
        if not self.values[code]:
            self.values[code] = LinkedList(head = node)

        else:
            current = self.values[code].head #先指定現在的指標指在對應雜湊值位置的Linked的第一個head上
            while current.next:
                current = current.next # 如過head的那個node指向的next有值，則往後推移
            current.next = node #直到最後node的next沒有值時候才串接在後頭
        self.values[code].count +=1 #linked list紀錄現在上面有幾個數據
        self.length +=1 # 紀錄表內總共有幾個數據
        return

    def search(self, key):
        code = self.hash(key,self.size) #先查找雜湊值
        current = self.values[code].head #將現在指標放在對應雜湊值位置的Linked的第一個head上
        while current.next: 
            if key in current.value: #如果現在位置內有輸入的key，則返回所對應的key 以及value //這邊的程式碼內的current.value為node內所定義的value與dictionary的不同
                return (current.value)
            else:
                current  = current.next
        return "Data not found"

    def remove(self, key):
        code = self.hash(key,self.size) #先查找雜湊值
        current = self.values[code].head #將現在指標放在對應雜湊值位置的Linked的第一個head上
        while current.next:
            if key in current.next.value: #如果現在位置的下一個node內有輸入的key，則將現在位置的next指標指向原本下一個node的next位置//這邊的程式碼內的current.value為node內所定義的value與dictionary的不同
                current.next = current.next.next
                return('Data was deleted successfully')
            current = current.next
        return

    def __repr__(self):
        return str(self.values)

ht = HashTable(5)
ht.add("John", "111-111-111")
ht.add("Taylor", "222-222")
ht.add("Krish", "333-333")
ht.add("Mack", "444-444")
ht.add("Den", "555-555")
ht.add("Mike", "666-666")
ht.add("Jack", "88-88-88")
ht.add("Jimmy", "99-99")
ht.add("Harry", "121-121")
ht.add("Meet", "232-232")
ht.add("Miraj", "454-454")
ht.add("Milan", "567-567")
print(ht)
#[
# [{'Taylor': '222-222'}->{'Mack': '444-444'}->{'Mike': '666-666'}->{'Meet': '232-232'}], 
# None, 
# [{'Jack': '88-88-88'}->{'Milan': '567-567'}], 
# [{'Krish': '333-333'}->{'Jimmy': '99-99'}->{'Harry': '121-121'}], 
# [{'John': '111-111-111'}->{'Den': '555-555'}->{'Miraj': '454-454'}]
# ]
print(ht.search('Den'))#{'Den': '555-555'}
print(ht.search('Jimmy'))#{'Jimmy': '99-99'}
print(ht.remove('Den'))#Data was deleted successfully
print(ht.search('Den'))#Data not found

print(ht)
#[
# [{'Taylor': '222-222'}->{'Mack': '444-444'}->{'Mike': '666-666'}->{'Meet': '232-232'}], 
# None, 
# [{'Jack': '88-88-88'}->{'Milan': '567-567'}], 
# [{'Krish': '333-333'}->{'Jimmy': '99-99'}->{'Harry': '121-121'}], 
# [{'John': '111-111-111'}->{'Miraj': '454-454'}]
# ]