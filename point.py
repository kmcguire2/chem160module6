class point:
    #initialize
    def __init__(self, dim, data):
        self.dim = dim
        self.data = []
        for i in range(dim):
            self.data.append(float(data[i]))

    #how it will be printed
    def __repr__(self):
        output = ""
        for i in self.data:
            output += str(i) + " " #convert to string
        return output

    #scales all elements by a factor
    def scale(self, x):
        for i in range(self.dim):
            self.data[i] *= x
    #dot product
    def dot(self, apoint):
        sum = 0
        for i in range(self.dim):
            sum += self.data[i] * apoint.data[i]
        return sum
