import numpy as np
import skimage
from skimage.measure import LineModelND

class RansacSolver:

    def __init__(self):
        # Initialize curve fitting model. Here is a sample N-dimensional line model. It can be swapped with any other desired fitting model.
        self.model = LineModelND()

    def fit(self, data: Data, threshold=25, iter_num=1500, sample_num=2):
        
        # Initialization of parameters to keep track of during execution
        counter = 0
        max_inliers = 0
        best = None

        # Starting the iterative process of the algorithm
        while counter < iter_num:

          counter = counter + 1

          # Shuffling the data and choosing a random sample for line fitting
          np.random.shuffle(data.data)
          sample = data.data[:sample_num, :]

          # Use random pair to estimate the line
          self.model.estimate(sample)

          # Calculate the y coordinates of all x coordinates of the data according to the fitted line
          y_model = self.model.predict_y(data.x)
            
          # Calculate the difference between the y coordinates of the model and the y coordinates of the data
          error = np.abs(data.y - y_model.T)
            
          # Count how many points are within the threshold set as distance from the line
          inliers = np.count_nonzero(error < threshold)

          # Iteratively save the model with the best results
          if inliers > max_inliers:
            max_inliers = inliers
            best = self.model.params

        # Return the parameters of the model
        return best
