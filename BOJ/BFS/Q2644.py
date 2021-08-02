from collections import deque

class Person:

    def __init__(self, num, parent=None, child=None):
        self.num = num
        self.parent = parent
        self.children = [child]

    def setParent(self, parent):
        self.parent = parent

    def addChild(self, child):
        self.children.append(child)
        if None in self.children:
            self.children.remove(None)

    def getParent(self):
        return self.parent

    def getChildren(self):
        return self.children


n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
person = {}
for _ in range(m):
    parent, child = map(int, input().split())
    if parent not in person:
        p_parent = Person(parent, child=child)
        person[parent] = p_parent
    else:
        person[parent].addChild(child)

    if child not in person:
        p_child = Person(child, parent=parent)
        person[child] = p_child
    else:
        person[child].setParent(parent)

queue = deque([[p1, 0]])
check = set()
isFound = False

while queue:
    p, cnt = queue.popleft()
    if p == p2:
        isFound = True
        print(cnt)
        break
    check.add(p)
    n_person = person[p]
    parent = n_person.getParent()
    child = n_person.getChildren()

    if parent not in check and parent is not None:
        queue.append([parent, cnt + 1])
    child = list(set(child) - check)
    child = list(zip(child, [cnt+1 for _ in range(len(child))]))

    if all(None not in c for c in child):
        queue += child


if not isFound:
    print(-1)