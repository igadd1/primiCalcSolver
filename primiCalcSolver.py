class Node():
    def __init__(self, parent, state, action):
        self.parent = parent
        self.state = state
        self.action = action

#queue frontier for bfs
class Frontier():
    def __init__(self):
        self.frontier = []  

    def add(self, node):
        self.frontier.append(node)
    def remove(self):
        tmp = self.frontier[0]
        self.frontier = self.frontier[1:]
        return tmp
    def notEmpty(self):
        return len(self.frontier) > 0

def addOne(x):
    return x + 1

def mulTwo(x):
    return x * 2

def mulThree(x):
    return x * 3

def foundTarget(node):
    nodes = []
    while node.parent is not None:
        nodes.append(node)
        node = node.parent
    for node in nodes:
        print(node.action)
    exit()


startingValue = int(input("Choose starting integer: "))
targetValue = int(input("Choose target integer: "))

actions = [addOne, mulTwo, mulThree]
startNode = Node(None, startingValue, None)
frontier = Frontier()
frontier.add(startNode)

while frontier.notEmpty():
    node = frontier.remove()
    for action in actions:
        tmpNode = Node(node, action(node.state), action)
        if action(node.state) == targetValue:
            foundTarget(tmpNode)
        frontier.add(tmpNode)



