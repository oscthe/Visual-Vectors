from math import sqrt, ceil
import matplotlib.pyplot as plt

class Vector:
    setWidth = 0.05
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __len__(self):
        print(f"Len returns rounded but exact length is {round(sqrt(self.x**2 + self.y**2),3)}.")
        return ceil(sqrt(self.x**2 + self.y**2))
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def length(self):
        return sqrt(self.x**2 + self.y**2)
    
    def plot(self, setWidth=setWidth):
        if self.y > 0:
            plt.arrow(0, 0, self.x, self.y, width=setWidth, length_includes_head=True)
            plt.xlim([-abs(self.x)-1, abs(self.x)+1])
            plt.ylim([-abs(self.y)-1, abs(self.y)+1])
            plt.title(f"Vector({self.x}, {self.y})")
            plt.grid()
            plt.show()
        else:
            plt.arrow(0, 0, self.x, self.y, width=setWidth, length_includes_head=True)
            plt.xlim([-abs(self.x)-1, abs(self.x)+1])
            plt.ylim([-abs(self.y)-1, abs(self.y)+1])
            plt.title(f"Vector({self.x}, {self.y})")
            plt.grid()
            plt.show()
            
    def addplot(self, other, setWidth=setWidth):
        third = Vector(self.x, self.y) + Vector(other.x, other.y)
        x_start_pos = [0, 0, self.x]
        y_start_pos = [0, 0, self.y]
        x_end_pos = [third.x, self.x, other.x]
        y_end_pos = [third.y, self.y, other.y]
        colors = ['r', 'g', 'b']
        xMax = max(abs(third.x), abs(self.x), abs(other.x))
        yMax = max(abs(third.y), abs(self.y), abs(other.y))
        if third.y > 0:  
            for number in range(len(x_start_pos)):
                plt.arrow(x_start_pos[number], y_start_pos[number], 
                            x_end_pos[number], y_end_pos[number], 
                            width=setWidth, color=colors[number],
                            length_includes_head=True, head_width=2*setWidth)
                
            plt.xlim([-xMax-1, xMax+1])
            plt.ylim([-yMax-1, yMax+1])
            plt.title(f"Red line: Vector({third.x}, {third.y})")
            plt.grid(linestyle="-", zorder=0)
            plt.show()
        else:
            for number in range(len(x_start_pos)):
                plt.arrow(x_start_pos[number], y_start_pos[number], 
                            x_end_pos[number], y_end_pos[number], 
                            width=setWidth, color=colors[number],
                            length_includes_head=True, head_width=2*setWidth)
            plt.xlim([-xMax-1, xMax+1])
            plt.ylim([-yMax-1, yMax+1])
            plt.title(f"Vector({third.x}, {third.y})")
            plt.grid(linestyle="-", zorder=0)
            plt.arrow(0, 0, third.x, third.y, width=0.05, zorder=1)
            plt.show()