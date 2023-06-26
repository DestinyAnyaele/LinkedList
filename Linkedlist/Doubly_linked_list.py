class Node :
  def __init__(self,data,prev = None,next = None) :
    self.data = data
    self.prev = prev
    self.next = next
class LinkedList :
  def __init__(self) :
    self.head = None
  def Append(self,element) :
    current_node = self.head
    previous_node = current_node
    if current_node == None :
      self.head = Node(element)
    else :
      while current_node.next != None :
        current_node,previous_node = current_node.next,current_node
      current_node.next = Node(element,current_node)
  def Display(self) :
    linkedlist = []
    current_node = self.head
    if current_node != None :
      while current_node.next != None :
        linkedlist.append(current_node.data)
        current_node = current_node.next
      linkedlist.append(current_node.data)
    return linkedlist
  def Length(self) :
    current_node = self.head
    count = 0
    if current_node != None :
      while current_node.next != None :
        current_node = current_node.next
        count += 1
      count += 1
      return count
  def Remove(self,element) :
    current_node = self.head
    if self.Length() == 1 :
      if current_node.data == element :
        self.head = None
        return None
    while current_node.next != None :
      if current_node.data == element :
        if current_node.prev == None :
          self.head = current_node.next
        elif current_node.next == None :
          current_node.prev.next = None
        else :
          current_node.prev.next = current_node.next
        return None
      current_node = current_node.next
    raise ValueError
  def Getindex(self,element) :
    count = 0
    current_head = self.head
    
  def Pop(self,Index) :
    pass
  def Insert(self,Index) :
    pass
