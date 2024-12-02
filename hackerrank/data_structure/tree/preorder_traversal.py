def preOrder(root):
    print(root, end=" ")
    if root.left is not None:
        preOrder(root.left)
    
    if root.right is not None:
        preOrder(root.right)