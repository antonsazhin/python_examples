
class BasicFunction(object):
    def __init__(self):
        self.state = 0

    def increment_state(self):
        self.state += 1

    def clear_state(self):
        self.state = 0


if __name__ == '__main__':
    basicFunction = BasicFunction()
    basicFunction.increment_state()
    print("Hello world with basic state: " + str(basicFunction.state))
