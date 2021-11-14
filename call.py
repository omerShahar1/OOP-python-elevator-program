class Call:
    def __init__(self, time:float, src:int, dest:int):
        self.time = time
        self.src = src      # src floor of the call
        self.dest = dest    # dest floor of the call

    def type(self):
        """
        return 1 if call type is up. 0 otherwise
        """
        if(self.src < self.dest):
            return 1
        return 0



