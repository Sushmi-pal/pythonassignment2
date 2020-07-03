class Mario:
    def __init__(self,height,colorofdress):
        self.height=height
        self.dress=colorofdress

    def jump(self):
        self.key=input("Enter a key, j or n:")
        if "key"=="j":
            print("Jump")

    def takecoins(self):
        pass

marioperson=Mario(20,'red')
marioperson.jump()