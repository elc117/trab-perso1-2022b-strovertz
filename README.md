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

# Desenvolvimento: Trabalho 1 - Marchine Learning; Resultado - Falha 

Utilizando de técnicas de convolução, tentei desenvolver uma IA a partir da biblioteca tensorflow, que é voltada para o aprendizado de máquina e comptuação numerica. O protótipo inicial se baseou na construção de uma aplicação que recebesse uma fonte biblioteca de dados cifar10 e cifar100 (https://www.cs.toronto.edu/~kriz/cifar.html), que utiliza de Superclasses e classes para o treinamento da IA.<br>
<sub>Exemplo de biblioteca de Imagens Cifar</sub>
<br>
![image](https://user-images.githubusercontent.com/74078237/208254793-988d4b74-755e-4da1-8408-5b2a617a6883.png)<br>
<sub> Fonte: https://www.cs.toronto.edu/~kriz/cifar.html </sub><br>

## Função Main( ):

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
O código carrega datasets da biblioteca citada e plota a imagem como 32x32, e divide por 255 para converter as cores RGB (265 cores, numero de valores inteiros interpretados), para uma escala de 0 a 1, para facilitar. Então exemplos de imagens que serão forncidas são exibidas na tela. <br>
![image](https://user-images.githubusercontent.com/74078237/208256500-8c8bc297-1ade-4936-ae54-6acd533c9485.png)<br>
Repare que ao colocarmos o mouse sobre alguma das imagens, temos o aplicativo exibe no canto inferior direito algumas informações sobre as camadas de cores e posição do pixel sobreposto pelo mouse relativa a uma escala 32x32. <br>
![image](https://user-images.githubusercontent.com/74078237/208256587-62ce8df6-0577-4fba-bf04-32b917c473bb.png)


Em seguida fornecemos um conjunto de imagens para o nosso computador treinar a inteligência artificial, porém devido aos limites de capacidade computacional do meu computdor, independente do numero de imagens que eu definir que devem ser analisadas ele limita a alguns lotes de 625 imagens, como o processo de treinamento é um pouco demorado, armazenamos o modelo de aprendizagem em uma pasta do nosso computador. Então realizamos uma validação que verifica se no atual diretório existe uma pasta que armazena nosso modelo. <br>


```Python
 #Verifica se a IA já foi treinada para poupar poder computacional
    if os.path.isdir("image_classifier.model"):
        run_model(class_names)
    else:
        create_model(training_images, training_labels, testing_images, testing_labels)
        run_model(class_names)
```
Caso a pasta não exista, a aplicação puxa uma função responsável por criar um modelo de aprendizagem.

## Função create_model( )
```Python
def create_model(training_images, training_labels, testing_images, testing_labels):   
    
    model = models.Sequential()
    #Especifica o tamanho e a quantidade de canais
    model.add(layers.Conv2D(32, (3,3), activation='relu', input_shape=(32,32,3)))
    # Rsponsavel por diminuir o poder computacional necessario para processar nossos "dados"
    model.add(layers.MaxPooling2D((2,2)))
    model.add(layers.Conv2D(64, (3,3), activation='relu'))
    model.add(layers.MaxPooling2D((2,2)))
    model.add(layers.Conv2D(64, (3,3), activation='relu'))
    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(100, activation='softmax'))

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    model.fit(training_images, training_labels, epochs=20, validation_data=(testing_images, testing_labels))

    loss, accuracy = model.evaluate(testing_images, testing_labels)
    print(f"Loss: {loss}")
    print(f"Accuracy: {accuracy}")

    model.save('image_classifier.model')
```
Esta função é responsável por receber as imagens e labels para treinamento e teste. As imagens são processadas numa qualidade 32x32 (Aspect 1:1), em camadas RGB separadas, utilizando modelo de convolução e específicações para otimizar o a computação necessária para o processamento. Para não alongar tanto o README, uma explicação didática de como funciona o aprendizado por convolução pode ser encontrando na referência 5. <br>
Após o processamento das camadas de imagem, a aplicação imprime a perca nas imagens (% de pixels que não contribuiram com o aprendizado) e a precisão que nesse caso define que a cada 100 fotos distintas, X% serão rotuladas corretamente. Em seguida o modelo de aprendizagem é exportado para a pasta definida.

## Função run_model( )

```Python
def run_model(class_names):
    
    model = models.load_model('image_classifier.model')
    #Observações: A foto precisa ter resolução 32x32 |
    # 1:1 Aspect Ratio pois as imagens fornecidas para a IA 
    # treinar pelo dataset estão nessa qualidade
    img = cv.imread('img/pers.jpg')
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    plt.imshow(img, cmap=plt.cm.binary)
    prediction = model.predict(np.array([img]) / 255)

    index = np.argmax(prediction)
    print(f"Prediction is {class_names[index]}")

    plt.show()
```
A função carrega o modelo de aprendizado construido anteriormente e puxa uma imagem local do computador, com resolução 32x32, exibe a foto converte os pixels da imagem para uma escala entre 0 e 1. Então o algoritmo de utiliza dos das redes neurais para rotular a imagem de acordo com o modelo de aprendizado de máquina.

## O que deu errado?

Desisti de seguir neste trabalho por problemas na execução dos algoritmos que desencadearam algumas motivações pessoais. 

Para que eu possa obter mais precisão ao analisar uma imagem local é preciso fornecer um lote grande de imagens diversas com diferentes bibliotecas, não apenas a cifar100. Porém a capacidade computacional da qual disponho hoje me limita a blocos de aprendizagem com 625 imagens cada, um numero pequeno para exigir que resutlados precisos sejam apresentados. Desse modo, toda vez que tento apresentar uma imagem de uma mulher para o software, ele me retorna "Bird", similar ao apresentar um Cavalo, que a IA identifica como "Deer". Segue exemplo:
![image](https://user-images.githubusercontent.com/74078237/208257465-c82add22-3189-4b37-a309-eb337ac68198.png)<br>
Tentei aumentar o numero de Epochs, porém o resultado não foi tão bem sucedido. O que complicou avançar com o trabalho, pois eu iria entregar resultados imprecisos e a próxima etapa seria executada de maneira errada. O próximo passo da construção do trabalho seria coletar informações mais específicas da imagem e trabalhar com POO e construtores, armazenando dados e criando pessoas/animais com base no que foi identificado pela IA em um grupo de imagens locais. Ex.: Apresento um humano, ela atribui informações geradas de forma randomica utilizando outros arquivos com funções para construir uma pessoa completa, com cpf, email, nome, geolocalização, etc. Caso um animal fosse identificado, ele seria atribuido a algum dos humanos criados. 

Desejo trabalhar com IA de forma mais avançada no futuro, então preferi investir em outro trabalho, para que as frustrações de um modelo de aprendizagem falho resultante de uma falta de tempo para estudar mais a fundo os modelos existentes e outras formas de construção de redes neurais não impactassem negativamente em futuras expriências.

# Mapeamento de infectados com covid-19

## Descrição e Objetivo:

A aplicação tem como objetivo mapear pessoas geradas de forma randomica infectadas ou não com covid 19, e marcar as informações em um mapa HTML interativo utilizando bibliotecas do Python definindo as pessoas a partir de construtores e utilizando JSON para representar os dados estruturados. Ex.:
![image](https://user-images.githubusercontent.com/74078237/208263306-19bff62a-2e9e-473a-8bc9-d094208f1c79.png) <br>


## Algumas Referências:
    
### Python:
    [^1] https://docs.python.org/pt-br/3/library/concurrency.html
    [^2] https://asperbrothers.com/blog/image-recognition-in-python/
    [^3] https://medium.com/diogommartins/concorr%C3%AAncia-e-paralelismo-threads-m%C3%BAltiplos-processos-e-asyncio-parte-2-8e539c59a16a
    [^4] https://insightlab.ufc.br/8-bibliotecas-de-deep-learning-mais-usadas-em-python
    [^5] https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53

## Extras:
Playlist motivacional: https://open.spotify.com/playlist/6wRDAHW2NYw5eB6BCLny6W?si=50114f48c3ce4815
