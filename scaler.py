# create min max scaler
class MinMaxScaler:

    # pass data as list
    def __init__(self, min_val, max_val):
        self.min = min_val
        self.max = max_val

    # perform transformation
    def transform(self, value):
        return (self.max - value)/(self.max - self.min)