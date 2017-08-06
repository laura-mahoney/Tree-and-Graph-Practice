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





#these are the tree traversals outside of objects
def preorder(root):

     if root is not None:
          print root.data,
          preorder(root=root.leftchild)
          preorder(root=root.rightchild)

def postorder(root):

     if root is not None:
          postorder(root.leftchild)
          postorder(root.rightchild)
          print root.data,

def inorder(root):

     if root is not None:
          inorder(root.leftchild)
          print root.data,
          inorder(root.rightchild)

#get height of binary search tree          
def height(root):
    
    if root is None:
        return -1
    
    return max(height(root.leftchild), height(root.rightchild)) + 1



def breadth_first_traversal(root):
#breadth or level order search using a queue class
     
     to_visit = [root]

     while to_visit:
          current = to_visit.pop(0) 

          if current.leftchild:
               to_visit.extend([current.leftchild])
          if current.rightchild:
               to_visit.extend([current.rightchild])
          
          print current.data,



def depth_first_traversal(root):
#depth first search using a stack, i.e. popping from list
     to_visit = [root]

     while to_visit:
          current = to_visit.pop() 

          if current.leftchild:
               to_visit.extend([current.leftchild])
          if current.rightchild:
               to_visit.extend([current.rightchild])
          
          print current.data,



