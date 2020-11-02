
from queue import Queue 
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = Queue()           #inbuilt queues
        self.q2 = Queue()
        
        self.cur_size = 0 #contains number of elements        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.cur_size+=1 
        self.q2.put(x)
        
        while (not self.q1.empty()):
            self.q2.put(self.q1.queue[0])
            self.q1.get()
            
        self.q = self.q1
        self.q1 = self.q2
        self.q2 = self.q
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if (self.q1.empty()):
            return 
        return self.q1.get()
        self.cur_size -= 1
            

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.q1.empty():
            return -1
        return self.q1.queue[0]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if self.q1.empty():
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
