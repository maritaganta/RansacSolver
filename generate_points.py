import numpy as np

class Data():
# Initializes a line and then adds noise and faulty measurements
    def __init__(self, x_range=(-100,100), slope=0.67, scalar=8):
        self.x = np.arange(x_range[0], x_range[1])
        self.y = slope * x + scalar
        self.data = np.column_stack((self.x,self.y))

    def generate_random_points(self):
        self.add_noise()
        self.add_faulty()
        self.x, self.y = self.data[:,0], self.data[:,1]

    def add_noise(self):
        data_noise = np.random.normal(size=self.data.shape)

        self.data += 4 * data_noise
        self.data[::2] += 45 * data_noise[::2] 
        self.data[::7] += 20 * data_noise[::7] 
        self.data[::11] += 87 * data_noise[::11] 
        self.x, self.y = self.data[:,0], self.data[:,1]

    def add_faulty(self):
        data_faulty = np.random.normal(size=(round(0.25*self.data.shape[0]), 2))
        self.data[::4] += 34 * data_faulty
        self.x, self.y = self.data[:,0], self.data[:,1]
