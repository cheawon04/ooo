import time 

class torch:
    def __init__(self):
        self.name = 'choi su gil'
    def print(self):
        print('thid is torch class'+self.name)

def main():
    print('this is my first python  programming')
    torch1 = torch()
    torch1.print()
    print(torch1.name)

if __name__ == '__main__':
    main()
