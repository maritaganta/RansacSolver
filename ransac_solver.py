import numpy as np
import skimage
from skimage.measure import LineModelND

class RansacSolver:

    def __init__(self):
        self.model = LineModelND()

    def fit(self, data: Data, threshold=25, iter_num=1500, sample_num=2):

        counter = 0
        max_inliers = 0
        best = None

        prob_out = 0.5
        prob_desired = 0.95

        while counter < iter_num:

          counter = counter + 1

          np.random.shuffle(data.data)
          sample = data.data[:sample_num, :]

          self.model.estimate(data.data)

          y_model = self.model.predict_y(data.x)
          error = np.abs(data.y - y_model.T)
          inliers = np.count_nonzero(error < threshold)

          if inliers > max_inliers:
            max_inliers = inliers
            best = self.model.params


        return best
