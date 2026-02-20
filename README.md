# Projeto_CapturaDeImagens

Responda: por que a janela aberta não mostra a imagem colorida?
$ ao ler a imagem em img = cv.imread('messi5.jpg',0), a leitura considera 0 como a nova profundidade da imagem, tornando-a na escala grey; para ajustar basta editar a linha 4 de L__1_img.py como:
  img = cv.imread('messi5.jpg',0)

Altere: modifique o programa para que as imagens sejam exibidas mais rápidamente e depois
para que sejam exibidas mais lentamente. Responda: qual a explicação de alteração de
velocidade de exibição, e apresente suas soluções detalhadamente
$ para alterar a velocidade de reprodução devemos ajustar a quantidade de fremes por segundo da funcao time.sleep(segundo/frame). quanto maior o numero de frames, maior a velocidade de reprodução, basta editar a linha 15 de L__2_video.py como 80 frames por exemplo:
  time.sleep(1/80.0)

Altere: modifique o programa para que uma imagem da câmera seja salva num arquivo
“foto1.png” no momento em que for clicada a tecla ‘x’ no teclado. Apresente o resultado e sua
solução detalhadamente.
$ para alcancar o objetivo, devemos ajusar a key para funcionar para o mesmo comando e criar uma condicional dentro do loop while True em L__3_webcam.py que reonheca x e use a funcao imwrite para salvar o frame como:
    cv.imshow('frame', frame)
    key = cv.waitKey(1)
    if key == ord('q'):
        break
    if key == ord('x'):
        cv.imwrite('foto.jpg',frame)

Altere: modifique o programa para que as imagens gravadas estejam “normais” no arquivo de
video salvo, e apresentem uma velocidade de exibição adequada. Apresente o resultado e sua
solução detalhadamente.
$ para as imagens gravadas estarem normais, devemos alterar o codigo L__4_webcap.py para retirar a linha 21 que usa o comando cv.flip e adicionar o codigo de L__2_video.py para processar o video gravado, ajustando a velocidade de frames para a ddesejada, como abaixo:
    # frame = cv.flip(frame, 0)
    # write the flipped frame
    out.write(frame)
    cv.imshow('Imagem Normal', frame)
    if cv.waitKey(1) == ord('q'):
        break
