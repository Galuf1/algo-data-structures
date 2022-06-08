from hashlib import new

# ----- Node ------
class Node:
  # store your DATA and NEXT values here
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkList:
  # write your __init__ method here that should store a 'head' value which the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList
  def __init__(self, head = None):
    self.head = head
    self.length = 0
  
  def print_list(self):
    temp = self.head
    while (temp):
      print(temp.data)
      temp = temp.next

  def add(self,new_data):
    # if the list is empty new node is the new head
    new_node = Node(new_data)
    if self.head is None:
      self.head = new_node
    
    # if it's not empty we iterate until we find the tail and we conect it with the new node

    tail = self.head
    while(tail.next):
      tail = tail.next
    tail.next = new_node
    

  def remove(self, data):
    # write your code to REMOVE an element from the Linked List
    temp = self.head

    # in case the head holds the data we just change the head
    if (temp is not None):
      if (temp.data == data):
        self.head = temp.next
        temp = None
        return
    # we search for the node that holds the value while keeping track of the previous node to change it's next property
    while (temp is not None):
      if temp.data == data:
        break
      prev = temp
      temp = temp.next 

    # if it's not in the list
    if (temp == None):
      return

    # remove the node from the list

    prev.next = temp.next
    temp = None

  def get(self, element_to_get):
    # write you code to GET and return an element from the Linked List
    temp = self.head

    while(temp is not None):
      if temp.data == element_to_get:
        return temp
      temp = temp.next




llist = LinkList()
llist.head = Node(1)
second = Node(2)
third = Node(3)
llist.head.next = second
second.next = third
llist.print_list()
llist.add(4)
llist.print_list()
llist.remove(2)
llist.print_list()
get = llist.get(3)
print(get.data)
