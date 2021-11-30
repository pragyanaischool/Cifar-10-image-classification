import tensorflow as tf
from tensorflow import keras

#load the model
model=tf.keras.models.load_model('models/basic_model.h5')

#load the prediction image
def load_image(img_path):
    img=tf.keras.preprocessing.image.load_img(img_path,target_size=(28,28))
    img_tensor=keras.preprocessing.image.img_to_array(img)
    img_tensor=tf.expand_dims(img_tensor,axis=0)
    img_tensor/=255.0
    
    return img_tensor

IMAGE_PATH="data/images/airplane1.jpg"
image=load_image(IMAGE_PATH)

pred=model.predict(image)
print(pred)