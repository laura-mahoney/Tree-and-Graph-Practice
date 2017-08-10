class Node(object):#helper class

     def __init__(self, data, leftchild=None, rightchild=None): #constructor method 
          self.data = data
          self.leftchild = leftchild
          self.rightchild = rightchild


     def insert(self, new_data):

          if self.data: 
               if new_data < self.data:
                    if self.leftchild is None: 
                         self.leftchild = Node(new_data)
                    else:
                         self.leftchild.insert(new_data)

               elif new_data > self.data:
                    if self.rightchild is None: 
                         self.rightchild = Node(new_data)
                    else: 
                         self.rightchild.insert(new_data)
          else: 
               self.data = new_data


     def find(self, value):

          if(self.data==value):
               return True

          elif self.data > value:
               if self.leftchild:
                    return self.leftchild.find(value)

               else:
                    return False

          else: 
               if self.rightchild:
                    return self.rightchild.find(value)
               else:
                    return False

     def find_leaves(self):
          #depth first to find all of the leaf nodes s
          to_visit = [self]
          leaves = []

          while to_visit:

               current = to_visit.pop()

               if current.leftchild is None and current.rightchild is None:
                    leaves.append(current.data)

               if current.leftchild:
                    to_visit.extend([current.leftchild])

               if current.rightchild:
                    to_visit.extend([current.rightchild])

          return leaves
          #use breadth or depth first and when we come to a node where there's
          #no data add it to a list of leaves

#there are several ways to check if a Binary Tree is a valid Binary Search Tree
#one method is an inorder traversal making sure that current node is always smaller
#than previous node
#other method is to use recursion
     def is_valid(self):

          def _ok(n, lt, gt):
               """ check this node and recurse to children"""
               if n is None:
               #base case: this is not a node 
                    return True

               if lt is not None and n.data > lt:
                #base case: left node is greater than current node
                    return False

               if gt is not None and n.data < gt:
                #base base: right node is less than current node
                    return False 

               if not _ok(n.leftchild, n.data, gt):
                #passing the left node in as the new node, recursively checking all lefts
                #all data on the left has to be less than n.data and greater than successive nodes
                    return False 

               if not _ok(n.rightchild, lt, n.data):
                #pass the right node in as the new node, recursively checking all rights
                #all data on the left has to be less than n.data
                    return False



               return True 

          return _ok(self, None, None)


#this is the tree class
class Binary_Search_Tree(object):#main user interface

     def __init__(self, root=None):
          self.root = root #define root 


     def add_value(self, value):
          #add values to bst, one by one without using helper class, or recursion
          if self.root == None:
               self.root = Node(value)

          else:
               current = self.root

               while True:
                    if value < current.data:
                         if current.leftchild:
                              current = current.leftchild
                         else:
                              current.leftchild = Node(value)
                              break

                    elif value > current.data:
                         if current.rightchild:
                              current = current.rightchild
                         else:
                              current.rightchild = Node(value)
                              break

                    else: 
                         break

     def insert(self, data):
     #this insert method calls the insert method from the node class
          if self.root:
               return self.root.insert(data)

          else:
               self.root = Node(data)
               return True



     def find(self, value):
     #this find method calls the find method from the node class

          if self.root:
               return self.root.find(value)

          else:
               return False 


     def find_leaves(self):

          if self.root:
               print self.root
               return self.root.find_leaves()
          else:
               return False


#these are the tree traversals outside of objects
#including the iterative versions as well
def preorder(root):

     if root is not None:
          print root.data,
          preorder(root=root.leftchild)
          preorder(root=root.rightchild)

#check the left children first, then p
def postorder(root):

     if root is not None:
          postorder(root.leftchild)
          postorder(root.rightchild)
          print root.data,

#this uses two stacks, one to iterate over values added to it
#the other 
def postorder_iterative(root):

     to_visit = [root]
     seen = []

     while to_visit:

          curret = to_visit[-1]
          if current in seen:
               print current.data
               to_visit.pop()
          else:
               if currnt.rightchild:
                    to_visit.append(rightchild)
                    seen.append(current.rightchild)
               if current.leftchild:
                    to_visit.append(leftchild)
                    seen.append(current.leftchild)

          if current.leftchild is None and root.righthchild is None:
               print current.data
               to_visit.pop()


def inorder(root):

     if root is not None:
          inorder(root.leftchild)
          print root.data,
          inorder(root.rightchild)


def inorder_iterative(root):

#get height of binary search tree          
def height(root):
    
    if root is None:
        return -1
    
    return max(height(root.leftchild), height(root.rightchild)) + 1


def depth(root):

     if root is None:
        return 0
    
     return max(depth(root.leftchild), depth(root.rightchild)) + 1

  


def breadth_first_traversal(root):
#breadth or level order search using a queue class
     
     to_visit = [root]

     while to_visit:
          current = to_visit.pop(0) 

          if current.leftchild:
               to_visit.append(current.leftchild)
          if current.rightchild:
               to_visit.append(current.rightchild)
          
          print current.data,



def depth_first_traversal(root):
#depth first search using a stack, i.e. popping from list
     to_visit = [root]

     while to_visit:
          current = to_visit.pop() 

          if current.leftchild:
               to_visit.append(current.leftchild)
          if current.rightchild:
               to_visit.append(current.rightchild)
          
          print current.data,



