class node(object):
  def __init__(self,value):
    self.value=value
    self.next=None
  def __str__(self):
    return str(self.value)
class SinglyLinkedlist(object):
  def __init__(self):
    self.head= node("head")
    self.tail=self.head
    self.length=0
  def addLeft(self,val):
    temp=self.head.next
    self.head.next=node(val)
    self.head.next.next=temp
  def addRight(self,val):
    self.tail.next=node(val)
    self.tail=self.tail.next
  def __len__(self):
    return self.length
  def pop(self):
    head=self.head
    if self.length==0:
      return 
    while(self.next)
