class Stack:
    """Stack Implementation
    
    Stack implemented using a static array (implicit).
    Stack associated methods are implemented (push, pop, peak).
    Helper methods used to implement main method (stack_full, stack_empty).
    
    Attributes:
        _stack_size (int): The maximum length of the stack
        _stack (:obj:`list` of :obj:`int`): Array storing values of stack
        _head (int): Pointer pointing to head (top) of stack
    """
    def __init__(self, stack_size: int = 10):
        """Initialise Stack

        Args:
            stack_size (int, optional): The maximum length of the stack. Defaults to 10.
        """
        self._stack_size = stack_size
        self._stack = [None] * stack_size
        self._head = -1
    
    def push(self, value: int) -> bool:
        """Push method

        Args:
            value (int): Value that will be pushed on top of stack

        Returns:
            bool: 
                True, if `value` was pushed on top of stack.
                False, if action failed (stack was full).
        """
        if self.stack_full():
            # unsuccessful action (full stack)
            return False
        
        # push value to next available position (on top) of stack
        self._head += 1
        self._stack[self._head] = value
        
        return True

    def pop(self) -> [int, bool]:
        """Pop method

        Returns:
            [int, bool]:
                False, if action failed (stack was empty)
                Int, which is item popped off stack
        """
        if self.stack_empty():
            # unsuccessful action (stack was empty)
            return False
        
        # copy and pop off item at head (on top) of stack
        return_value = self._stack[self._head]
        self._stack[self._head] = None
        self._head -= 1
        
        return return_value
    
    def peak(self) -> [int, None]:
        """Peak method

        Returns:
            [int, None]:
                int, which is item below head (top) of stack
                None, if there is no item below head
        """
        return self._stack[self._head - 1] if self._head > 0 else None
    
    def stack_empty(self) -> bool:
        """Helper method: Checks if stack is empty

        Returns:
            bool: 
                True, if stack is empty
                False, if stack is not empty
        """
        return self._head == -1
    
    def stack_full(self) -> bool:
        """Helper method: Checks if stack is full

        Returns:
            bool: 
                True, if stack is full
                False, if stack is not full 
        """
        return self._head == self._stack_size - 1
    
    
def main():
    """Main function
    
    Tests methods in class `Stack`
    """
    myStack = Stack(5)
    names = ["Aman", "Dawud", "Pratyush", "Tom", "Mr. Wood", "Unkown"]
    
    # populate stack - reject `Unkown` value
    for name in names:
        myStack.push(name)
    print(f"Populate: {myStack._stack}")
    
    print(f"Peak: {myStack.peak()}")
    
    # depopulate stack - reject pop when stack is empty
    for i in range(100):
        myStack.pop()
    print(f"Depopulate: {myStack._stack}")

if __name__ == "__main__":
    main()