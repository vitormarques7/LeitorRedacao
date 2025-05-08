import cv2

imagens = ["imgRedacao1.jpg", "imgRedacao2.jpg"]

for nome_imagem in imagens:
    imagem = cv2.imread(nome_imagem)

    if imagem is None:
        print(f"Erro ao carregar a imagem {nome_imagem}.")
        continue

    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    _, binaria = cv2.threshold(cinza, 127, 255, cv2.THRESH_BINARY)

    contornos, _ = cv2.findContours(binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cv2.imshow(f"Imagem Original - {nome_imagem}", imagem.copy())
    cv2.waitKey(0)

    print(f"Contornos encontrados em {nome_imagem}: {len(contornos)}")

    for contorno in contornos:
        x, y, w, h = cv2.boundingRect(contorno)
        if w > 20 and h > 10:
            cv2.rectangle(imagem, (x, y), (x + w, y + h), (0, 255, 0), 10)

    cv2.imshow(f"Texto Detectado - {nome_imagem}", imagem)
    cv2.waitKey(0)

    nome_saida = f"resultado_{nome_imagem}"
    cv2.imwrite(nome_saida, imagem)
    print(f"Resultado salvo como {nome_saida}")

cv2.destroyAllWindows()
