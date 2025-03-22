def quadrado(lado1, lado2, lado3, lado4, angulo):
    if lado1 == lado2 == lado3 == lado4 and angulo==90:
        print(f"O Quadrilátero é um quadrado! \n Valores do quadrilátero = {lado1}, {lado2}, {lado3}, {lado4}, {angulo} ")
    else: 
        print(f"O Quadrilátero não é um quadrado! \n Valores do quadrilátero = {lado1}, {lado2}, {lado3}, {lado4}, {angulo}")
        
resultado = quadrado(2,2,2,2,90)
print(quadrado)