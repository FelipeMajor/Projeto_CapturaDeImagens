# Projeto_CapturaDeImagens: PARTE 1

> **Responda: por que a janela aberta não mostra a imagem colorida?** <br>
**$** ao ler a imagem em img = cv.imread('messi5.jpg',0), a leitura considera 0 como a nova profundidade da imagem, tornando-a na escala grey; para ajustar basta editar a linha 4 de L__1_img.py como: <br>
  img = cv.imread('messi5.jpg',0) <br>

> **Altere: modifique o programa para que as imagens sejam exibidas mais rápidamente e depois
para que sejam exibidas mais lentamente. Responda: qual a explicação de alteração de
velocidade de exibição, e apresente suas soluções detalhadamente** <br>
**$** para alterar a velocidade de reprodução devemos ajustar a quantidade de frames por segundo da funcao time.sleep(segundo/frame). quanto maior o numero de frames, maior a velocidade de reprodução, basta editar a linha 15 de L__2_video.py como 80 frames por exemplo: <br>
  time.sleep(1/80.0) <br>

> **Altere: modifique o programa para que uma imagem da câmera seja salva num arquivo
“foto1.png” no momento em que for clicada a tecla ‘x’ no teclado. Apresente o resultado e sua
solução detalhadamente.** <br>
**$** para alcancar o objetivo, devemos ajusar a key para funcionar para o mesmo comando e criar uma condicional dentro do loop while True em L__3_webcam.py que reonheca x e use a funcao imwrite para salvar o frame como: <br>
    cv.imshow('frame', frame) <br>
    key = cv.waitKey(1) <br>
    if key == ord('q'): <br>
        break <br>
    if key == ord('x'): <br>
        cv.imwrite('foto.jpg',frame) <br>

> **Altere: modifique o programa para que as imagens gravadas estejam “normais” no arquivo de
video salvo, e apresentem uma velocidade de exibição adequada. Apresente o resultado e sua
solução detalhadamente.** <br>
**$** para as imagens gravadas estarem normais, devemos alterar o codigo L__4_webcap.py para retirar a linha 21 que usa o comando cv.flip e para processar o video gravado em uma velocidade normal, ajustamos a velocidade de frames para a desejada, como abaixo: <br>
    fps =20.0 <br>


> **Responda: se for necessário alterar a imagem, ou seja realizando alguma operação de procesamento nela, em que
ponto dos quatro programas estudados isso deve ser realizado?** <br>
**$** O processamento da imagem deve vir apos a gravacao da mesma, pois com execcao de alguns ajustes como posicao de gravacao ou velocidade, o processamento de imagem como mornalizacao, filtragem de ruido, etc se dá de formas complexas que o programa de geração de imagem não deve se encarregar.
