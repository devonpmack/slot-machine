import random

class slot(object):
    def __init__(self):
        self.curslot = 0
        self.possibilities = ['apple','grape','banana','mango','orange']
        random.shuffle(self.possibilities)
        self.max = len(self.possibilities)
    def draw(self):
        print(self.possibilities[self.curslot])
    def inc(self, n):
        for i in range(0,n):
            self.curslot += 1
            if self.curslot > self.max-1:
                self.curslot = 0
    def get(self, n=1):
        if n == 0:
            if self.curslot+1 < self.max:
                return self.possibilities[self.curslot+1]
            else:
                return self.possibilities[0]
        if n == 1:
            return self.possibilities[self.curslot]
        if n == 2:
            if self.curslot-1 < 0:
                return self.possibilities[self.max-1]
            else:
                return self.possibilities[self.curslot-1]
slots = [slot(),slot(),slot()]
def button():
    print("---------------------------")
    for thing in slots:
        thing.inc(random.randint(0,10))

    if slots[0].get() == slots[1].get() and slots[1].get() == slots[2].get():
        print("WINNER! %s,%s,%s" % (slots[0].get(), slots[1].get(), slots[2].get()))

    for t in range(0,3):
        print(str(t) + ": " +slots[0].get(t) + " " + slots[1].get(t) + " " + slots[2].get(t))
    print("---------------------------")

while True:
    if input("Press? ") != 'n':
        button()
    else:
        break
