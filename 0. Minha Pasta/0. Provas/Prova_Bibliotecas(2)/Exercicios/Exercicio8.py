import cv2

imagem = cv2.imread("underwater.jpg")

def cor(opcao):
    if opcao == 1:
        return cv2.cvtColor(imagem, cv2.COLOR_BGR2LUV)
    elif opcao == 2: 
        return cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
    elif opcao == 3:
        return cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

# def espelhamento(opcao):
#     if opcao == 1:


print("Escolha o efeito de cor")
print("1 - BGR para LUV\n2 - BGR para HSV\n3 - BGR para RGB")
opcao_cor = int(input("Opção: "))

img_nova = cor(opcao_cor)

cv2.imshow('imagem modificada', img_nova)
cv2.waitKey()
cv2.destroyAllWindows()

# print("Escolha o tipo de espelhamento: ")
# print("1 - Manter original\n2 - Inverter Horizontalmente\n3 - Inverter verticalmente")
# opcao_eplh = int(input("Opção: "))

