#Class creation for favorite animal

class Animal:

    #------------------------
    def __init__(self):
        self.armLength = 4.5
        self.legLength = 5.5
        self.numOfEyes = 2
        self.tail = True
        self.furry = True

    def description(self):
        print(f"Length of the Arms:{self.armLength}")
        print()
        print(f"Length of the Legs:{self.legLength}")
        print()
        print(f"Number of Eyes:{self.numOfEyes}")
        print()
        print(f"Does it have a Tail:{self.tail}")
        print()
        print(f"Is it Furry:{self.furry}")
        print()
        
    def main():
        description()

    if __name__=="__main__":
        main()
