class CPU:
    def __init__(self,cores) -> None:
        self.cores=cores
class RAM:
    def __init__(self,size) -> None:
        self.size=size
class HardDisc:
    def __init__(self,hd_capacity) -> None:
        self.hd_capacity=hd_capacity
# in computer 'has a' relation
class Computer:
    def __init__(self,cores,size,hd_capacity) -> None:
        self.cpu=CPU(cores)
        self.ram=RAM(size)
        self.hard_disc=HardDisc(hd_capacity)