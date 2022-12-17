# Machine Learning for pattern recognition With Python

## Proposito: 

Desenvolver/Implementar um código em Java ou Python, para o reconhecimento de padrões, estudando metodologias de implementação de POO e/ou Concorrência em uma das linguagens selecionadas.

Objetivos específicos: 
 * Fornecer uma imagem complexa e ter como resultado a marcação e identificação de objetos nas imagens.
 * Analise e compreensão de como a curva de aprendizado irá se comportar.
 * Identificar conteúdo de imagens de baixa qualidade 32x32 pixels utilizando de convolução.

 ## Materiais:

 ### Python:

* VsCode + Jupyter NB e Anaconda
* GitHub (Versionamento)
* Talvez AWS (Ferramentas de Machine Learning e ETL e Computação Serverless se o meu pc não aguentar)

#### Bibliotecas:
* Numpy
* Matplotlib
* Tensorflow
* OpenCV
* OS

#Desenvolvimento: Trabalho 1 - Marchine Learning; Resultado - Falha 

Utilizando de técnicas de convolução, tentei desenvolver uma IA a partir da biblioteca tensorflow, que é voltada para o aprendizado de máquina e comptuação numerica. O protótipo inicial se baseou na construção de uma aplicação que recebesse uma fonte biblioteca de dados cifar10 e cifar100 (https://www.cs.toronto.edu/~kriz/cifar.html), que utiliza de Superclasses e classes para o treinamento da IA.<br>
<sub>Exemplo de biblioteca de Imagens Cifar</sub>
<br>
![image](https://user-images.githubusercontent.com/74078237/208254793-988d4b74-755e-4da1-8408-5b2a617a6883.png)<br>
<sub> Fonte: https://www.cs.toronto.edu/~kriz/cifar.html </sub><br>

## Função Main:

```Python
def main():
    #Carrega um dataset com 100 classes, incluindo crianças, gatos, castelos, etc 
    (training_images, training_labels), (testing_images, testing_labels) = datasets.cifar100.load_data()
    training_images, testing_images = training_images / 255, testing_images/ 255
    class_names = get_class()
    
    plt.figure(figsize=(10,10))
    for i in range(0, 20):
        plt.subplot(5,5,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        j = i+0
        data_plot = training_images[j]
        plt.imshow(data_plot)
        plt.xlabel(str(testing_labels[j]))
        
    plt.show()
    #Diminuir o valor pra não matar o computador!!
    training_images = training_images[:20000]
    training_labels = training_labels[:20000]
    testing_images = testing_images[:40000]
    testing_labels = testing_labels[:40000]
```
O código carrega datasets da biblioteca citada e plota a imagem como 32x32, e divide por 255 para converter as cores RGB (265 cores, numero de valores inteiros interpretados), para uma escala de 0 a 1, para facilitar, em seguida fornecemos um conjunto de imagens para o nosso computador treinar a inteligência artificial, porém devido aos limites de capacidade computacional do meu computdor, independente do numero de imagens que eu definir que devem ser analisadas ele limita a alguns lotes de 625 imagens, como o processo de treinamento é um pouco demorado, armazenamos o modelo de aprendizagem em uma pasta do nosso computador. Então realizamos uma validação que verifica se no atual diretório existe uma pasta que armazena nosso modelo. <br>

```Python
 #Verifica se a IA já foi treinada para poupar poder computacional
    if os.path.isdir("image_classifier.model"):
        run_model(class_names)
    else:
        create_model(training_images, training_labels, testing_images, testing_labels)
        run_model(class_names)
```
Caso a pasta não exista, a aplicação puxa uma função responsável por criar um modelo de aprendizagem.

##Função Create Model:





## Algumas Referências:
    
### Python:
    [^1] https://docs.python.org/pt-br/3/library/concurrency.html
    [^2] https://asperbrothers.com/blog/image-recognition-in-python/
    [^3] https://medium.com/diogommartins/concorr%C3%AAncia-e-paralelismo-threads-m%C3%BAltiplos-processos-e-asyncio-parte-2-8e539c59a16a
    [^4] https://insightlab.ufc.br/8-bibliotecas-de-deep-learning-mais-usadas-em-python
    [^5] https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53

## Extras:
Playlist motivacional: https://open.spotify.com/playlist/6wRDAHW2NYw5eB6BCLny6W?si=50114f48c3ce4815
