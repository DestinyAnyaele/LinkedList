class Node :
  def __init__(self,data,next = None) :
    self.next = next
    self.data = data
class LinkedList :
  def __init__(self) :
    self.head = None
    self.tail = None
  def Append(self,element) :
    # get the head nods for traversing
    # get the tail node so to know the last nide when traversing
    current_node = self.head
    last_node = self.tail
    if current_node == None :
      current_node = Node(element)
      current_node.next = self.head
      last_node = current_node
    else :
      while current_node is not last_node :
        current_node = current_node.next
      current_node.next = Node(element,self.head)
      last_node = current_node.next
