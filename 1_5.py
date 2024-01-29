import math

def sin(minimum, maximum, counter):
    for i in range(counter):
        x = minimum + (maximum - minimum) * i / (counter - 1)
        result = math.sin(x)
        print(f"{x:.3f}  |   {result:.3f}")

def main():
    min = 0
    max = 2 * math.pi
    counter = 1000
    print("x       |        sin(x)")
    print("-----------------------")
    
    sinTable = sin(min, max, counter)
    
if __name__=="__main__":
    main()
