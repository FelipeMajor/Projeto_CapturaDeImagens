# Projeto Captura de Imagens e Vídeos 📷

Este repositório reúne os códigos e documentações do **Laboratório 3 – Captura de Imagem e Vídeo** realizado em fevereiro de 2026 por um grupo de estudantes de computação. O objetivo principal é demonstrar o uso básico da biblioteca OpenCV para leitura, exibição, captura e gravação de imagens e vídeos, além de algumas adaptações em um notebook Jupyter para geração de avatares e montagem de quadros.

---

## 👥 Autores

- Fabricio da Costa Fernandes (RA: 11202321635)
- Felipe de Lima Major (RA: 11202230321)
- Lilian Gimenez Teixeira (RA: 11202332321)


## 🗂 Estrutura do projeto

```
main.ipynb              # Notebook com relatório e experimentos
README.md               # Este arquivo de documentação
static/                 # Pasta para imagens e vídeos gerados
    fotos/              # Fotos capturadas pela webcam
    videos/             # Vídeos gravados
webcam-functions/       # Scripts auxiliares utilizados nos experimentos
    (ALTERADO)L__1_img.py
    (ALTERADO)L__2_video.py
    (ALTERADO)L__3_webcam.py
    (ALTERADO)L__4_webcap.py
```

Os arquivos dentro de `webcam-functions` são versões modificadas dos exercícios propostos no laboratório, com ajustes de velocidade, salvamento e correções de orientação.

## 🧪 Conteúdo dos experimentos

1. **Leitura de imagens**: carregamento de arquivos estáticos com diferentes flags para controlar cores e profundidade.
2. **Reprodução de vídeo**: leitura de um arquivo `.mp4` e alteração da velocidade de exibição ajustando o intervalo entre frames.
3. **Captura de webcam**: visualização em tempo real e salvamento de uma foto ao pressionar a tecla `x`.
4. **Gravação de vídeo**: captura da câmera e escrita em arquivo `.avi` com codec XVID, ajustando FPS e removendo flips indesejados.
5. **Adaptação para notebook**: os códigos foram incorporados em `main.ipynb`, que também inclui geração de uma foto de equipe, montagem de avatares e vídeos com diferentes velocidades.

O notebook contém explicações, respostas às questões propostas pelo laboratório e as conclusões dos experimentos.

## 🚀 Começando

Para reproduzir os experimentos em sua máquina:

1. **Pré-requisitos**:
   - Python 3.8+ ou similar
   - Bibliotecas: `opencv-python`, `numpy`, `scikit-image` (para a parte 2)
   - ambiente Jupyter (opcional, para abrir `main.ipynb`)
   - Câmera USB ou integrada para captura ao vivo.

2. **Instalação das dependências** (exemplo usando `pip`):

   ```bash
   pip install opencv-python numpy scikit-image jupyter
   ```

3. **Executar os scripts**:
   - Abra o notebook `main.ipynb` e execute as células conforme desejado.
   - Para rodar individualmente, execute os arquivos dentro de `webcam-functions` com Python:
     ```bash
     python "webcam-functions/(ALTERADO)L__1_img.py"
     python "webcam-functions/(ALTERADO)L__2_video.py"
     python "webcam-functions/(ALTERADO)L__3_webcam.py"
     python "webcam-functions/(ALTERADO)L__4_webcap.py"
     ```

   As janelas de vídeo podem ser fechadas pressionando `q` ou as teclas indicadas nos comentários dos códigos.

4. **Resultados**:
   - As imagens e vídeos gerados são salvos em `static/fotos` e `static/videos` respectivamente.
   - O notebook inclui exemplos adicionais de processamento e montagem de avatares.


## 📄 Conclusão

O projeto serve como relatório prático das atividades do laboratório, demonstrando os procedimentos básicos de captura e manipulação de mídias com OpenCV. Ele estabelece uma base para futuros experimentos de processamento de imagem e vídeo.

> Para detalhes metodológicos e explicações das modificações, consulte o próprio `main.ipynb`.

---

## 📚 Referências

- Biblioteca OpenCV: https://opencv.org/
- Documentação do Jupyter Notebook: https://jupyter.org/


---

*Última atualização: 27 de fevereiro de 2026*