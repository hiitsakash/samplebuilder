from gamingcomputerbuilder import GamingComputerBuilder
from computerdirector import ComputerDirector

if __name__ == '__main__':
    gb = GamingComputerBuilder()
    d = ComputerDirector(gb)
    d.construct()
    c = d.get_computer()
    print(c.cpu)
