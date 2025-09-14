from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        :type height: List[int]
        :rtype: int
        """
        maximo=0
        inicio=0
        fin=len(height)-1
        actual=0
        #print("comenzando")
        while(fin<len(height) and inicio<fin):
            if (height[inicio]>height[fin]):
                actual = (fin-inicio) * height[fin]
            else:
                actual = (fin-inicio) * height[inicio]
            #print(f"Inicio: {inicio}, Fin: {fin}, Actual: {actual}, Maximo: {maximo}")
            # Actualizar el máximo si el área actual es mayor
            if actual > maximo:
                maximo = actual
            # Mover el puntero del lado más bajo
            if height[inicio] < height[fin]:
                inicio += 1
            else:
                fin -= 1
            #print(f"Nuevo Inicio: {inicio}, Nuevo Fin: {fin}, Maximo: {maximo}")

        return maximo
    

if __name__ == "__main__":
    sol = Solution()
    print(f"Máxima area: {sol.maxArea([1,8,6,2,5,6,4,8,3,7])}")