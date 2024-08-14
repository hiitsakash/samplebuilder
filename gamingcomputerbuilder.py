
from computerbuilder import ComputerBuilder
from computer import Computer


class GamingComputerBuilder(ComputerBuilder):
    def __init__(self, ):
        self.cpu = 0

    def set_cpu(self, cpu):
        if self.cpu <= 2:
            raise ValueError("Cpu should be greater than 2")
        self.cpu = cpu

    def build(self):
        c = Computer()
        c.set_cpu(self.cpu)
        return c
