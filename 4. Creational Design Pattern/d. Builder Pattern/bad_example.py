class Laptop:
    def __init__(
        self,
        processor: str,
        ram: str,
        graphic_card: str = None, # type: ignore
        color: str = None, # type: ignore
        screen_size: str = None, # type: ignore
    ):
        self.processor = processor
        self.ram = ram
        self.graphic_card = graphic_card
        self.color = color
        self.screen_size = screen_size

    def display_specs(self):
        print(f"Processor = {self.processor}")
        print(f"Ram = {self.ram}GB")
        if self.graphic_card:
            print(f"Graphic Card = {self.graphic_card}")
        if self.color:
            print(f"Color = {self.color}")
        if self.screen_size:
            print(f"Screen Size = {self.screen_size}")


laptop1 = Laptop("i5-3232", "6")
laptop1.display_specs()

laptop2 = Laptop("i5-3232", "6", None, "Black", None) # type: ignore
laptop2.display_specs()