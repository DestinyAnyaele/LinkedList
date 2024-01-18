class Node :
  def __init__(self,data,prev = None,next = None) :
    self.data = data
    self.prev = prev
    self.next = next
class CDL :
  def __init__(self) :
    self.head = None
    self.tail = None
  def Append(self,data) :
    current_node = self.head
    if current_node is None :
      self.head = current_node = Node(data)
      self.head.prev = self.head.next = self.head
    else :
      while current_node is not self.tail :
        current_node = current_node.next
      current_node.next = self.head.prev = Node(data,current_node,self.head)
    self.tail = current_node.next
  def Display(self) :
    linkedlist = []
    current_node = self.head
    while current_node is not self.tail :
      linkedlist.append(current_node.data)
      current_node = current_node.next
    linkedlist.append(current_node.data)
    return linkedlist
  def Length(self) :
    return len(self.Display())
  def Insert(self,Index,data) :
    if Index < 0 :
      Index += self.Length()
    if (Index >= self.Length()) or (self.head is None) :
      self.Append(data)
    elif (Index >= 1) and (Index < self.Length()) :
      current_node = self.head
      for i in range(Index - 1) :
        current_node = current_node.next
      current_node.next.prev = current_node.next = Node(data,current_node,current_node.next)
    if Index <= 0 :
      self.head.prev = self.head = Node(data,self.tail,self.head)
      self.tail.next = self.head
  def Remove(self,element) :
    current_node = self.head
    if current_node is None :
      raise ValueError
    if current_node.data == element :
      self.head = current_node.next
      self.head.prev = self.tail
      return
    while current_node is not self.tail :
      if current_node.data == element :
        current_node.prev.next = current_node.next
        current_node.next.prev = current_node.prev
        return
      current_node = current_node.next
    if current_node.data == element :
      self.tail = current_node.prev
      current_node.prev.next = self.head
      self.head.prev = current_node.prev
      return
    raise ValueError
