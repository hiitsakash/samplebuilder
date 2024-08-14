class ComputerDirector:
    def __init__(self, ComputerBuilder):
        self.ComputerBuilder = ComputerBuilder

    def construct(self):
        #  set values as per user

        self.ComputerBuilder.set_cpu(11)

    def get_computer(self):
        return self.ComputerBuilder.build()