class Entry:
    def __init__(self, name:str, content:str) -> None:
        self.name = name
        self.content = content
    
    def setContent(self, content:str) -> None:
        self.content = content
    
    def __str__(self) -> str:
        return f"{self.name} :\n{self.content}"