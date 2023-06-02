'''
Linked List learning
Check out this linked list i created,it has basic functions like your normal list e.g remove,append,pop, length,getindex except that it is a linked list 😁
To use it first create your object
>>> example = Linked_List()
Then perform various methods on them like Apppend,Length,Pop, Display,Remove,Get

ps : i am sorry i didn't comment my code
'''
class Node :
  def __init__(self,value = None) :
    self.data = value
    self.next = None
class Linked_List :
  def __init__(self) :
    self.head = Node()
  def Append(self,new_data) :
    current_node = self.head
    if current_node.data == None :
      current_node.data = new_data
    else :
      while current_node.next != None :
        current_node = current_node.next
      current_node.next = Node(new_data)
  def Display(self) :
    current_node = self.head
    Linked_List = []
    while current_node.next != None :
      Linked_List.append(current_node.data)
      current_node = current_node.next
    else :
      Linked_List.append(current_node.data)
    return Linked_List
  def Get(self,index) :
    current_node = self.head
    count = 0
    while count < index :
      if current_node.next == None :
        return 'INDEX OUT OF RANGE'
      current_node = current_node.next
      count += 1
    return current_node.data
  def Length(self) :
    count = 0
    current_node = self.head
    while current_node.next != None :
      current_node = current_node.next
      count += 1
    if current_node.data != None :
      count += 1
    return count
  def Pop(self,index = -1) :
    current_node = self.head
    length = self.Length()
    count = 0
    if index < 0 :
      index += length 
    if (index >= length) or (index < 0) :
      raise IndexError
    while count < index :
      previous_node,current_node = current_node, current_node.next
      count += 1
    if index == 0 :
      self.head = current_node.next
    else :
        previous_node.next = current_node.next
    return current_node.data
  def Remove(self,element) :
    current_node = self.head
    previous_node = current_node
    while current_node.next != None :
      if current_node.data == element :
        previous_node.next = current_node.next
        break
      current_node, previous_node = current_node.next, current_node
    if current_node.data == element :
      previous_node.next = None
    else :
      raise ValueError
