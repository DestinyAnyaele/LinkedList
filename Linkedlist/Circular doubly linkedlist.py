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
      current_node.next = Node(data,current_node,self.head)
    self.tail = current_node.next
  def Display(self) :
    linkedlist = []
    current_node = self.head
    while current_node is not self.tail : #None
      linkedlist.append(current_node.data)
      current_node = current_node.next
    linkedlist.append(current_node.data)
    return linkedlist
  def Length(self) :
    return len(self.Display())
  def Insert(self,Index,data) :
    if Index < 0 :
      Index += self.Length()
    if Index < 0 :
      self.head = Node(data,self.tail,self.head)
      self.tail.next = self.head
      return
    if Index >= self.Length() :
      self.Append(data)
    elif Index == 0 :
      self.head = Node(data,self.tail,self.head)
    elif self.head is None :
      self.head = Node(data)
      self.head.prev = self.head.next = self.head
    else :
      current_node = self.head
      for Index in range(Index - 1) :
        current_node = current_node.next
      current_node.next = Node(data,current_node,current_node.next)
  def Remove(self,data) :
    current_node = self.head
    if current_node is None :
      raise ValueError
    if current_node.data == data :
      self.head = current_node.next
      self.head.prev = self.tail
      return
    while current_node is not self.tail :
      if current_node.data == data :
        current_node.prev.next = current_node.next
        current_node.next.prev = current_node.prev
        return
      current_node = current_node.next
    if current_node.data == data :
      self.tail = current_node.prev
      current_node.prev.next = self.head
      self.head.prev = current_node.prev
      return
    raise ValueError
