from abc import ABC, abstractmethod


class PluginBase(ABC):
    @abstractmethod
    def meta(self):
        pass

    @abstractmethod
    def run(self):
        pass