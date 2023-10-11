'''
Cesar Emilio Castaño Marin
Solution: Remove colored pieces if both neighbors are the same color
Github Username: CesarEmilioC
'''
class Solution(object):
    def winnerOfGame(self, colors):
        """
        :type colors: str
        :rtype: bool
        """
        #We define de sum of A's and B's that are going to be removed
        suma_A = 0
        suma_B = 0
        #We define a counter i to check all of the elements of the colors list
        i = 0
        #Cycle for the game
        while i < len(colors) - 1:
            if colors[i] == "A":
                #We create a variable to check the number of consecutives A's in the sector
                suma_sector_A = 1
                #Cycle to check the A's sequence
                for j in colors[i+1:]:
                    if j == "A":
                        suma_sector_A += 1
                        i += 1
                    else:
                        break
                #We add the numbers of A's we can remove
                if suma_sector_A >= 3:
                    suma_A += suma_sector_A - 2
            #We do the same for B
            if colors[i] == "B":
                suma_sector_B = 1
                for j in colors[i+1:]:
                    if j == "B":
                        suma_sector_B += 1
                        i += 1
                    else:
                        break
                if suma_sector_B >= 3:
                    suma_B += suma_sector_B - 2
            i += 1
        #We return who wins
        if suma_A == 0 or suma_A <= suma_B:
            return False
        else:
            return True
            
        