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
          self.head.prev = None
        else :
          current_node.prev.next = current_node.next
          current_node.next.prev = current_node.prev
        return None
      current_node = current_node.next
    if current_node.data == element :
      current_node.prev.next = None
      return None
    raise ValueError
  def Getindex(self,element) :
    index = 0
    current_node = self.head
    if self.Length() >= 1 :
      while current_node.next != None :
        if current_node.data == element :
          return index
        index += 1
        current_node = current_node.next
      if current_node.data == element :
        return index
    raise ValueError
  def Pop(self,index = -1) :
    size = self.Length()
    current_node = self.head
    count = 0
    if index < 0 :
      index += size
    if (index >= size) or (index < 0) :
      raise ValueError
    else :
      if (index == 0) and (size == 1) :
        self.head = None
      elif (index == 0) :
        self.head = current_node.next
        self.head.prev = None
      else :
        while count < index :
          count += 1
          current_node = current_node.next
        current_node.prev.next = current_node.next
    return current_node.data
  def Insert(self,index,element) :
    pass
