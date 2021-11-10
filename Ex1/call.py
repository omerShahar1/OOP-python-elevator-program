class Call:
    def __init__(self, time:float, src:int, dest:int):
        self.time = time
        self.src = src      # src floor of the call
        self.dest = dest    # dest floor of the call
        self.state = 0      # 1 if elevator been to src floor, 2 if elevator been to the dest floor.


