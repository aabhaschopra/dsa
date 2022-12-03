# Program to demonstrate insert and delete operation in binary search tree

class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None


# Function to do inorder traversal of BST
def inorder(root):
	if root is not None:
		inorder(root.left)
		print(root.key, end=" ")
		inorder(root.right)


# Function to insert a new node with given key in BST
def insert(node, key):
	if node is None:
		return Node(key)

	if key < node.key:
		node.left = insert(node.left, key)

	else:
		node.right = insert(node.right, key)

	return node


def minValueNode(node):
	current = node
	while(current.left is not None):
		current = current.left

	return current


# Function to delete the key and return the new root
def deleteNode(root, key):
	if root is None:
		return root

	if key < root.key:
		root.left = deleteNode(root.left, key)

	elif (key > root.key):
		root.right = deleteNode(root.right, key)

	else:
		if root.left is None:
			temp = root.right
			root = None
			return temp

		elif root.right is None:
			temp = root.left
			root = None
			return temp

		temp = minValueNode(root.right)
		root.key = temp.key
		root.right = deleteNode(root.right, temp.key)

	return root


n = int(input("Number of elements to be inserted: "))
root = None

print("Enter the elements: ")
for i in range(0, n):
    ele = int(input())
    root = insert(root, ele)

print("Inorder traversal of the tree: ")
inorder(root)

n = int(input("\nNumber of elements to be deleted: "))
print("Enter the elements: ")
for i in range(0, n):
    ele = int(input())
    root = deleteNode(root, ele)
    print("Inorder traversal of the modified tree: ")
    inorder(root)
    print()
