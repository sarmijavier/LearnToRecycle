from keras.preprocessing import image
from keras.models  import load_model
import matplotlib.pyplot as plt
import numpy as np
import cv2
import tensorflow as tf
from keras.callbacks import ModelCheckpoint,EarlyStopping
from keras.layers import Conv2D, Flatten, MaxPooling2D,Dense,Dropout,SpatialDropout2D
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img, array_to_img
import random,os,glob
from keras import backend as k
import gc


class prueba():

    def predecir(self,file,nombre):
        dir_path = './Dataset'

        img_list = glob.glob(os.path.join(dir_path, '*/*.jpg'))

        print(len(img_list))



        # Image Pre Processing
        train=ImageDataGenerator(horizontal_flip=True,
                                 vertical_flip=True,
                                 validation_split=0.1,
                                 rescale=1./255,
                                 shear_range = 0.1,
                                 zoom_range = 0.1,
                                 width_shift_range = 0.1,
                                 height_shift_range = 0.1,)

        test=ImageDataGenerator(rescale=1/255,
                                validation_split=0.1)

        train_generator=train.flow_from_directory(dir_path,
                                                  target_size=(300,300),
                                                  batch_size=32,
                                                  class_mode='categorical',
                                                  subset='training')

        test_generator=test.flow_from_directory(dir_path,
                                                target_size=(300,300),
                                                batch_size=32,
                                                class_mode='categorical',
                                                subset='validation')


        # Image Pre Processing
        train=ImageDataGenerator(horizontal_flip=True,
                                 vertical_flip=True,
                                 validation_split=0.1,
                                 rescale=1./255,
                                 shear_range = 0.1,
                                 zoom_range = 0.1,
                                 width_shift_range = 0.1,
                                 height_shift_range = 0.1,)

        test=ImageDataGenerator(rescale=1/255,
                                validation_split=0.1)

        train_generator=train.flow_from_directory(dir_path,
                                                  target_size=(300,300),
                                                  batch_size=32,
                                                  class_mode='categorical',
                                                  subset='training')

        test_generator=test.flow_from_directory(dir_path,
                                                target_size=(300,300),
                                                batch_size=32,
                                                class_mode='categorical',
                                                subset='validation')

        labels = (train_generator.class_indices)
        print(labels)

        labels = dict((v,k) for k,v in labels.items())
        print(labels)



        for image_batch, label_batch in train_generator:
          break
        image_batch.shape, label_batch.shape


        print (train_generator.class_indices)

        Labels = '\n'.join(sorted(train_generator.class_indices.keys()))

        with open('./WeightsAndLabels/labels.txt', 'w') as f:
          f.write(Labels)



        model=Sequential()
        #Convolution blocks

        model.add(Conv2D(32,(3,3), padding='same',input_shape=(300,300,3),activation='relu'))
        model.add(MaxPooling2D(pool_size=2))
        #model.add(SpatialDropout2D(0.5)) # No accuracy

        model.add(Conv2D(64,(3,3), padding='same',activation='relu'))
        model.add(MaxPooling2D(pool_size=2))
        #model.add(SpatialDropout2D(0.5))

        model.add(Conv2D(32,(3,3), padding='same',activation='relu'))
        model.add(MaxPooling2D(pool_size=2))

        #Classification layers
        model.add(Flatten())

        model.add(Dense(64,activation='relu'))
        #model.add(SpatialDropout2D(0.5))
        model.add(Dropout(0.2))
        model.add(Dense(32,activation='relu'))

        model.add(Dropout(0.2))
        model.add(Dense(6,activation='softmax'))

        filepath="./WeightsAndLabels/trained_model.h5"
        checkpoint1 = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
        callbacks_list = [checkpoint1]

        model.compile(loss='categorical_crossentropy',
                      optimizer='adam',
                      metrics=['acc'])



        #img_path = file
        model = load_model('./WeightsAndLabels/trained_model.h5', compile=False)
        #https://stackoverflow.com/questions/58028976/typeerror-unexpected-keyword-argument-passed-to-optimizer-learning-rate


        img = image.load_img(file, target_size=(300, 300))
        img = image.img_to_array(img, dtype=np.uint8)
        img=np.array(img)/255.0


        p=model.predict(img[np.newaxis, ...])
        predicted_class = labels[np.argmax(p[0], axis=-1)]

        k.clear_session() #eliminar la predicción para hacer otra
        #https://stackoverflow.com/questions/40785224/tensorflow-cannot-interpret-feed-dict-key-as-tensor

        classes = []
        prob = []
        for i, j in enumerate(p[0], 0):
            classes.append(labels[i])
            prob.append(round(j * 100, 2))

        caneca  = None
        if(predicted_class == 'basura'):
            caneca = 'Verde'
        elif(predicted_class == 'carton' or predicted_class == 'papel'):
            caneca = 'Gris'
        elif(predicted_class == 'vidrio' or predicted_class == 'botellas' or predicted_class == 'metal'):
            caneca = 'Azul'


        prediccionTotal = [max(prob),predicted_class,caneca]
        return prediccionTotal


    def recortarVideo(self,nombre):

        objeto = prueba()
        fps = cv2.VideoCapture(f'./imagenes/{nombre}')

        i = 0
        while(fps.isOpened()):
            if(i < 1):
                ret, frame = fps.read()
                if(ret == False):
                    break
                cv2.imwrite('./imagenes/ang'+str(i)+'.jpg',frame)
        fps.release()
        cv2.destroyAllWindows()
        return objeto.predecir('./imagenes/ang0.jpg')



    def archivoCorrecto(self,nombre,file):
        objeto = prueba()
        nombreDelarchivo = nombre.split('.')
        print(nombreDelarchivo[1] != 'mp4')
        if(nombreDelarchivo[1] == 'mp4'):
            return objeto.recortarVideo(nombre)
        elif(nombreDelarchivo[1] == 'jpg'):
            return objeto.predecir(file,nombre)
        else:
            return 'El tipo de archivo no es correcto'







if __name__ == '__main__':
    objeto = prueba()
    objeto.predecir('imagenes/botellaprueba_1.jpg')