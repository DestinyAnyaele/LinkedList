class Node :
  def __init__(self,data,next = None) :
    self.next = next
    self.data = data
class LinkedList :
  def __init__(self) :
    self.head = None
    self.tail = None
  def Append(self,element) :
    last_node = self.tail
    current_node = self.head
    if current_node == None :
      self.head = current_node = Node(element)
      current_node.next = self.head
      self.tail = last_node = current_node 
    else :
      while current_node is not last_node :
        current_node = current_node.next
      current_node.next = Node(element,self.head)
      self.tail = last_node = current_node.next
  def Display(self) :
    current_node = self.head
    last_node = self.tail
    linkedlist = []
    if self.head is None :
      return linkedlist
    while current_node is not last_node :
      linkedlist.append(current_node.data)
      current_node = current_node.next
    linkedlist.append(current_node.data)
    return linkedlist
  def Length(self) :
    current_node = self.head
    last_node = self.tail
    count = 0
    while current_node is not last_node :
      current_node = current_node.next
      count += 1
    return count + 1
  def Remove(self,*Elements) :
    for element in Elements :
        current_node = self.head
        while current_node.data != element :
          if current_node is self.tail :
            raise ValueError
          current_node, previous_node = current_node.next, current_node
        if current_node is self.head :
          if self.Length() == 1 :
            self.head = self.tail = None
          else :
            self.head = current_node.next
        elif current_node is self.tail :
          self.tail = previous_node
          previous_node.next = self.head
        else :
          previous_node.next = current_node.next
