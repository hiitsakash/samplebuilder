from abc import ABC, abstractmethod


class ComputerBuilder(ABC):
    @abstractmethod
    def set_cpu(self, cpu):
        pass

    @abstractmethod
    def build(self):
        pass
