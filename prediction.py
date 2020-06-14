from keras.preprocessing import image
from keras.models  import load_model
import cv2
import tensorflow as tf
from keras import backend as k
import numpy as np


class Predict:

    def prediction(self,file):
        labels = {0: 'Trash', 1: 'Bottles', 2: 'Cardboard', 3: 'Metal', 4: 'Paper', 5: 'Glass'}

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
        if(predicted_class == 'Trash'):
            trashContainer = 'Green Container Trash'
        elif(predicted_class == 'Cardboard' or predicted_class == 'Papper'):
            trashContainer = 'Gray Container Trash'
        elif(predicted_class == 'Glass' or predicted_class == 'Bottles' or predicted_class == 'Metal'):
            trashContainer = 'Blue Container Trash'


        TotalPrediction = [max(prob),predicted_class,trashContainer]

        return TotalPrediction


    def sliceVideo(self,nameOfVideo):

        fps = cv2.VideoCapture(f'./images/{nameOfVideo}')

        i = 0
        while(fps.isOpened()):
            if(i < 1):
                ret, frame = fps.read()
                if(ret == False):
                    break
                cv2.imwrite('./images/ang'+str(i)+'.jpg',frame)
        fps.release()
        cv2.destroyAllWindows()
        return self.prediction('images/ang0.jpg')



    def typeOfFile(self,nameOfFile,file):
        nameOfFileSlice = nameOfFile.split('.')
        if(nameOfFileSlice[1] == 'mp4'):
            return self.sliceVideo(nameOfFile)
        elif(nameOfFileSlice[1] == 'jpg'):
            return self.prediction(file)



if __name__ == '__main__':
    objeto = Preddict()
    objeto.prediction('Dataset/carton/cartonprueba (1).jpg')