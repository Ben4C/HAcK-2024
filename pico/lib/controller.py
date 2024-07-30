class Controller:
    def __init__(self, m1, m2, m3, m4, en1, en2):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.en1 = en1
        self.en2 = en2

    def forward(self):
        self.m1(0) #forward movement
        self.m2(1)
        self.m3(0)
        self.m4(1)

    def right(self):
        self.m1(1)
        self.m2(0)
        self.m3(0)
        self.m4(1)

    def left(self):
        self.m1(0)
        self.m2(1)
        self.m3(1)
        self.m4(0)

    def backward(self):
        self.m1(1)
        self.m2(0)
        self.m3(1)
        self.m4(0)

    def stop(self):
        self.m1(0)
        self.m2(0)
        self.m3(0)
        self.m4(0)