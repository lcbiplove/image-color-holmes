class Color:
    red: str
    green: str
    blue: str
    percentage: float
    hex_code: str

    def __init__(self, red: str, green: str, blue: str, percentage: float):
        self.red = red
        self.green = green
        self.blue = blue
        self.percentage = percentage

    def __str__(self) -> str:
        return f"Color: {self.red}, {self.green}, {self.blue}, Percentage: {self.percentage}%"
    
    @property
    def to_dict(self) -> dict:
        return dict({
            "red": self.red,
            "green": self.green,
            "blue": self.blue,
            "percentage": self.percentage,
            "hex_code": self.hex_code,
        })
    
    @property
    def hex_code(self) -> str:
        return f"#{int(self.red):02x}{int(self.green):02x}{int(self.blue):02x}"
