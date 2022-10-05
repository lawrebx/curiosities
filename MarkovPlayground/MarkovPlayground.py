import random

class randomWalker1D():
    
    def __init__(self, x_lim, weights):
        self.state = [0,0]
        self.returns = 0
        self.steps = 0
        self.direction_list = ["up","down","stay"]
        self.cross_count = 0
        self.weights = weights
        if x_lim > 0:
            self.x_ulim = x_lim
            self.x_llim = x_lim * -1
        else:
            raise Exception('x_lim and y_lim must be positive integers!')
            
    def move(self):
        
        self.steps = self.steps + 1 
        
        direction = random.choices(self.direction_list,self.weights,k=1)
        
        if direction[0] == "up":
            self.state = [self.state[0]+1,self.steps]
        elif direction[0] == "down":
            self.state = [self.state[0]-1,self.steps]  
        elif direction[0] == "stay":
            self.state = [self.state[0],self.steps] 
        else:
            raise Exception(f'Please provide valid direction - {direction} passed. {self.state}')
        
        if self.x_llim > self.state[0] or self.state[0] > self.x_ulim:
            return 1, self.state[0], direction[0]
        
        return 0, self.state[0], direction[0]     
            
    def get_returns(self):  
        return self.returns
    
    def get_state(self):  
        return self.state

    def get_steps(self):  
        return self.steps    

    def reset(self):
        self.state = [0,0]
        self.returns = 0
        self.steps = 0
        self.direction_list = ["up","down","stay"]

class randomWalker2D():
    
    def __init__(self,x_lim,y_lim):
        self.state = [0,0]
        self.returns = 0
        self.steps = 0
        self.direction_list = ["north","south","east","west"]
        if x_lim > 0 and y_lim > 0:
            self.x_ulim = x_lim
            self.y_ulim = y_lim
            self.x_llim = x_lim * -1
            self.y_llim = y_lim * -1
        else:
            raise Exception('x_lim and y_lim must be positive integers!')
            
    def move(self):
        
        self.steps = self.steps + 1
        
        if self.steps > 1:
            self.direction_list.append("stay")
            
        direction = random.choice(self.direction_list)
        
        if direction == "north":
            self.state = [self.state[0],self.state[1]+1]
        elif direction == "south":
            self.state = [self.state[0],self.state[1]-1]  
        elif direction == "east":
            self.state = [self.state[0]+1,self.state[1]]
        elif direction == "west":
            self.state = [self.state[0]-1,self.state[1]]
        elif direction == "stay":
            pass
        else:
            raise Exception(f'Please provide valid direction - {direction} passed. {self.state}')
        
        if self.x_llim > self.state[0] > self.x_ulim or self.y_llim > self.state[1] > self.y_ulim:
            return 1
        
        if self.state == [0,0]:
            return 2
        
        return 0     
            
    def get_returns(self):  
        return self.returns
    
    def get_state(self):  
        return self.state

    def get_steps(self):  
        return self.steps    

    def reset(self):
        self.state = [0,0]
        self.returns = 0
        self.steps = 0
        self.direction_list = ["north","south","east","west"]

class randomWalker3D():
    
    def __init__(self):
        self.state = [0,0,0]
        self.returns = 0
        self.steps = 0
        self.direction_list = ["north","south","east","west","up","down"]
        
    def move(self):
        
        self.steps = self.steps + 1
        
        if self.steps > 1:
            self.direction_list.append("stay")
            
        direction = random.choice(self.direction_list)
        
        if direction == "north":
            self.state = [self.state[0],self.state[1]+1,self.state[2]]
        elif direction == "south":
            self.state = [self.state[0],self.state[1]-1,self.state[2]]   
        elif direction == "east":
            self.state = [self.state[0]+1,self.state[1],self.state[2]]
        elif direction == "west":
            self.state = [self.state[0]-1,self.state[1],self.state[2]]
        elif direction == "up":
            self.state = [self.state[0],self.state[1],self.state[2]+1]
        elif direction == "down":
            self.state = [self.state[0],self.state[1],self.state[2]-1]
        elif direction == "stay":
            pass
        else:
            return('Please provide valid direction - north, south, east, west, up, down')
        
        if self.state == [0,0,0]:
            self.returns = self.returns + 1
        
        return f'Current position is [{self.state[0]},{self.state[1]}.'       
            
    def get_returns(self):  
        return self.returns
    
    def get_state(self):  
        return self.state

    def get_steps(self):  
        return self.steps    

    def reset(self):
        self.state = [0,0,0]
        self.returns = 0
        self.steps = 0
        self.direction_list = ["north","south","east","west","up","down"]

def run_walker_1D():
    myWalker = randomWalker1D(4,[10,30,5])

    step_data = []
    step_dir = []
    step_results = []
    end_state = []
    move_val = 0

    while move_val == 0:
        move_val, x_state, x_dir = myWalker.move()
        step_data.append(x_state)
        step_dir.append(x_dir)
        
    step_results.append(myWalker.get_steps())
    end_state.append(myWalker.get_state())
    myWalker.reset()    

    return step_results, end_state

def run_walker_2D():
    myWalker = randomWalker2D(4,4)

    step_results = []
    end_state = []
    move_val = 0

    while move_val == 0 and myWalker.get_steps() <= 10000:
        move_val = myWalker.move()

    step_results.append(myWalker.get_steps())
    end_state.append(myWalker.get_state())
    myWalker.reset()    

    return step_results, end_state

if __name__ == "__main__":
    steps_1D, state_1D = run_walker_1D()
    steps_2D, state_2D = run_walker_2D()
