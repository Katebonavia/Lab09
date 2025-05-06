from dataclasses import dataclass

from model.airport import Airport


@dataclass
class Arco:
    o1: Airport
    o2: Airport
    peso: int