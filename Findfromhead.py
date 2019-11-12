def find_from_tail(self, value):
   nodo_actual = self.__head
   
   while nodo_actual.data != value:
      if nodo_actual.next == None:
         return None
      nodo_actual = nodo_actual.next

      return nodo_actual
   
