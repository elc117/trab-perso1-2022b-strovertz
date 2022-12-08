import cv2 as cv
import numpy as np
import os
import matplotlib.pyplot as plt
from tensorflow.keras import datasets, layers, models

def get_class():
    class_names = ['Plane', 'Car', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck', 'Human']
    return class_names


def create_model(training_images, training_labels, testing_images, testing_labels):   
    
    model = models.Sequential()
    #Especifica o tamanho e a quantidade de canais
    model.add(layers.Conv2D(32, (3,3), activation='relu', input_shape=(32,32,3)))
    model.add(layers.MaxPooling2D((2,2)))
    model.add(layers.Conv2D(64, (3,3), activation='relu'))
    model.add(layers.MaxPooling2D((2,2)))
    model.add(layers.Conv2D(64, (3,3), activation='relu'))
    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(11, activation='softmax'))

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    model.fit(training_images, training_labels, epochs=11, validation_data=(testing_images, testing_labels))

    loss, accuracy = model.evaluate(testing_images, testing_labels)
    print(f"Loss: {loss}")
    print(f"Accuracy: {accuracy}")

    model.save('image_classifier.model')

def run_model(class_names):
    
    model = models.load_model('image_classifier.model')
    #Observações: A foto precisa ter resolução 32x32 | 1:1 Aspect Ratio pois as imagens fornecidas para a IA treinar pelo dataset estão nessa qualidade
    img = cv.imread('img/person.jpg')
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    plt.imshow(img, cmap=plt.cm.binary)
    prediction = model.predict(np.array([img]) / 255)

    index = np.argmax(prediction)
    print(f"Prediction is {class_names[index]}")

    plt.show()

def main():
    #Carrega um dataset com 100 classes, incluindo crianças, gatos, castelos, etc 
    (training_images, training_labels), (testing_images, testing_labels) = datasets.cifar100.load_data()
    #Os pixels podem variar de 0 a 255, porém fica mais comodo trabalhar com uma escala de 0 a 1, então dividindo por 255 encaixamos os pixels dentro dessa nossa escala
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

    training_images = training_images[:20000]
    training_labels = training_labels[:20000]
    testing_images = testing_images[:40000]
    testing_labels = testing_labels[:40000]

    if os.path.isdir("image_classifier.model"):
        run_model(class_names)
    else:
        create_model(training_images, training_labels, testing_images, testing_labels)
        run_model(class_names)
        
    
if __name__ == "__main__":
    main()