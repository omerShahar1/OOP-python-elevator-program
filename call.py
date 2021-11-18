class Call:
    def __init__(self, time:float, src:int, dest:int):
        self.time = time
        self.src = src      # src floor of the call
        self.dest = dest    # dest floor of the call
        self.start = True   # if start = true, then we need still need to insert the call data (src and dest) to our elivator floor lists.
        if self.src < self.dest:
            self.type = 1   # up call
        else:
            self.type = -1  # down call



