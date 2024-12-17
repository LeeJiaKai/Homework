class MinStack:
    def __init__(self):
        self.stack = [] #main stack for storing pigs
        self.min_stack = [] #co stack for storing min val pigs
    
    def push(self, x):
        self.stack.append(x) #push the pig into the top of the main stack
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x) #and if min then push here too

    def pop(self):
        if self.stack:
            top = self.stack.pop() #pop the top pig
            if top == self.min_stack[-1]: #if the top pig is the current min value pig
                self.min_stack.pop() #pop it too
    
    def min(self):
        if self.stack:
            return self.min_stack[-1] #return the current min
        else:
            return None

min_stack = MinStack()
while True:
    try:
        action = input().strip()

        if action.startswith("push"):
            min_stack.push(int(action.split()[1]))
        
        elif action.startswith("pop"):
            min_stack.pop()
        
        elif action.startswith("min"):
            min_pig = min_stack.min()
            if min_pig is not None:
                print(min_pig)
            
    except EOFError:
        break
