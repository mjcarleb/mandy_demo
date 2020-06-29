class my_ndarray:

    def __init__(self, l):

        self.l = l

    def __str__(self):

        return f"my_ndarray<{self.l}>"

    def __repr__(self):

        return f"my_ndarray<{self.l} with shape={self.shape()}>"

    def shape(self):

        return f"[{len(self.l)}, 1]"




