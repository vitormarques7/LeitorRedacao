# Detector de texto em imagens de redações

## Requisitos de como executar:

1. Python instalado na máquina. 
2. Biblioteca OpenCV instalada, usando o comando "pip install opencv-python".
3. Colocar as imagens na pasta do projeto com os nomes que serão usados no main.py.
4. No nosso caso foram:
    - imgRedacao1.jpg
    - imgRedacao2.jpg

## O que foi feito:

O projeto implementa um script em Python usando a biblioteca OpenCV para detectar automaticamente 
regiões de texto em imagens de redações escaneadas. O algoritmo (em main.py) realiza as seguintes etapas:

1. Carregamento das imagens.
2. Conversão para escala de cinza.
3. Binarização da imagem.
4. Detecção de contornos.
5. Desenho de retângulos ao redor de áreas com possíveis textos.
6. Salvamento das imagens no mesmo diretório com as marcações feitas.

O resultado são imagens com os trechos de texto destacados com um retângulo em volta.

## Principais dificuldades encontradas.

1. Relembrar a linguagem Python, já que tivemos essa disciplina apenas no primeiro 
período e não estávamos mais familiarizados.
2. Elaboração do código em si.
3. Instalação e configuração do OpenCV.
4. Compreensão do fluxo de processamento de imagem.
