from typing import List

class Solucion:
    def maxArea(self, alturas: List[int]) -> int:
        """
        :type alturas: List[int]
        :rtype: int
        """
        maximo=0
        inicio=0
        fin=len(alturas)-1
        actual=0
        while(fin<len(alturas) and inicio<fin):
            if (alturas[inicio]>alturas[fin]):
                actual = (fin-inicio) * alturas[fin]
            else:
                actual = (fin-inicio) * alturas[inicio]
            # Actualizar el máximo si el área actual es mayor
            if actual > maximo:
                maximo = actual
            # Mover el puntero del lado más bajo
            if alturas[inicio] < alturas[fin]:
                inicio += 1
            else:
                fin -= 1

        return maximo
    

if __name__ == "__main__":
    sol = Solucion()
    print(f"Máxima area: {sol.maxArea([1,8,6,2,5,4,8,3,7])}")