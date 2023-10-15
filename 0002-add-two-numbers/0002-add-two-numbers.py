'''
Cesar Emilio Castaño Marin
Solution: Add Two Numbers
Github Username: CesarEmilioC
'''
#Node class
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        #We initialize a sum variable and we go through the two lists
        suma = 0
        for lista in [l1,l2]:
            lista_digitos = []
            current_node = lista
            #We analyze the nodes until the last one, and we add the values of the nodes
            while current_node.next != None:
                lista_digitos.append(current_node.val)
                current_node = current_node.next
            lista_digitos.append(current_node.val)
            #We obtain the total sum of the numbers
            for i in range(len(lista_digitos)):
                suma += lista_digitos[i] * 10 ** i
        #We transform the sum into a string in order to be able to loop through it
        suma = str(suma)
        #Reversed the string
        suma = suma[::-1]
        #Generate the new linked list
        l3 = Node(int(suma[0]))
        current_node = l3
        for i in range(1,len(suma)):
            current_node.next = Node(int(suma[i]))
            current_node = current_node.next
        return l3
            
        