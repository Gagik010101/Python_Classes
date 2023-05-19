class Animal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
    def __del__(self):
        print(f"MISSION COMPLETED +")
