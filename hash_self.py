#Hash Table
class Node:
    def __init__(self, key=None, data=None):

    def __repr__(self):
        return str(self.data)

class LinkedList:
    def __init__(self, head=None):


    def __str__(self):


    def __repr__(self):
        return str(self)

class HashTable:
    def __init__(self, size):

        
    def hash(self, key, size):


    def add(self, key, value):


    def search(self, key):


    def remove(self, key):


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