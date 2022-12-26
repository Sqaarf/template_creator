class Template:
    def __init__(self) -> None:
        self.entries = []
    
    def addEntry(self, entry) -> None:
        self.entries.append(entry)
    
    def removeEntry(self, entry) -> None:
        self.entries.remove(entry)
    
    def __str__(self) -> str:
        ret = "---------------\n"
        for entry in self.entries:
            ret += f"{entry}\n---------------\n"  
        return ret
                