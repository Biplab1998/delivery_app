from dataclasses import dataclass

@dataclass
class Waiter:
    name: str
    place: str
    phone_number: int
ram = Waiter("Ram", "Jharkhand", 8006633543)

print(ram.name)

