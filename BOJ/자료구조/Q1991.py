import sys

# 1991번 문제. 트리 순회
'''
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .

'''

import heapq


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder_tree(param):
    global preorder
    if param not in nav.keys():
        return
    node = tree[nav[param]]
    preorder += node.data
    preorder_tree(node.left)
    preorder_tree(node.right)


def inorder_tree(param):
    global inorder
    if param not in nav.keys():
        return
    node = tree[nav[param]]
    inorder_tree(node.left)
    inorder += node.data
    inorder_tree(node.right)


def postorder_tree(param):
    global postorder
    if param not in nav.keys():
        return
    node = tree[nav[param]]
    postorder_tree(node.left)
    postorder_tree(node.right)
    postorder += node.data


if __name__ == "__main__":
    n = int(input())
    tree = []
    nav = dict()
    for _ in range(n):
        p, l, r = input().split()
        tree.append([p, l, r])
    root = tree[0][0]
    for i in range(n):
        p, l, r = tree[i]
        nav[p] = i
        new_node = Node(p)
        if l != '.':
            new_node.left = l
        if r != '.':
            new_node.right = r
        tree[i] = new_node

    preorder = ""
    inorder = ""
    postorder = ""
    preorder_tree(root)
    inorder_tree(root)
    postorder_tree(root)

    print(preorder)
    print(inorder)
    print(postorder)
