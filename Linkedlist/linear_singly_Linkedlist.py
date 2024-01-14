class Node :
  def __init__(self,data) :
    self.data = data
    self.next = None
class LSL :
  def __init__(self) :
    self.head = None
  def Append(self,data) :
    current_node = self.head
    if current_node is None :
      self.head = Node(data)
    else :
      while current_node.next is not None :
        current_node = current_node.next
      current_node.next = Node(data)
  def Display(self) :
    linked_list = []
    current_node = self.head
    if current_node is None :
      return linked_list
    else :
      while current_node.next is not None :
        linked_list.append(current_node.data)
        current_node = current_node.next
      linked_list.append(current_node.data)
      return linked_list
  def Remove(self,element) :
    current_node = self.head
    if current_node.data is element :
      self.head = self.head.next
      return None
    while current_node.next is not None :
      if current_node.data is element :
        previous_node.next = current_node.next
        return None
      previous_node,current_node = current_node,current_node.next
    if current_node.data is element :
      previous_node.next = current_node.next
    else :
      raise ValueError
  def Length(self) :
    count = 0
    current_node = self.head
    if current_node is None :
      return count
    while current_node.next is not None :
      count += 1
      current_node = current_node.next
    count += 1
    return count
