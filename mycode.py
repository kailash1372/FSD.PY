class MyNode:
     
      def __init__(self,key):
       self.left=None
       self.right=None
       self.value=key
      
      
def insert(root,key):
      if root is None:
        return MyNode(key)
      else:
        if root.value==key:
              return root
        elif root.value < key:
              root.right=insert(root.right,key)
        else:
              root.left=insert(root.left,key)
      return root
  
  
def traverseTheGraph(root):
  
   if root:
         traverseTheGraph(root.left)
         print(root.value)
         traverseTheGraph(root.right)
         
returnVal=MyNode(50)
 
returnVal=insert(returnVal,20)
returnVal=insert(returnVal,15)
returnVal=insert(returnVal,30)
 
traverseTheGraph(returnVal)    
      
