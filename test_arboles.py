from arboles import TreeNode

def main():
   raiz=TreeNode('r', \
                              TreeNode('b',TreeNode('s'),TreeNode('m')),\
                              TreeNode('p',TreeNode(1),TreeNode(2,TreeNode('z'),None)))
   print(raiz.left.left.data)
   print(raiz.right.right.left.data)
   print(raiz.right.left.data)
   raiz.left.right.left=TreeNode(3)
   raiz.right.right.right=TreeNode(4)
   raiz.left.left.left=TreeNode(6)

   aux=raiz
   while aux.right != None:
      aux=aux.right
   print(f"El ultimo a la derecha es:  {aux.data}")
main()
                                   
   
