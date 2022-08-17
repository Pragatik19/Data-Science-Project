import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras import layers, models

dataset=tf.keras.preprocessing.image_dataset_from_directory("training/PlantVillage",shuffle=True,image_size=(256,256),batch_size=32)
class_names=dataset.class_names
print(class_names)
print(len(dataset))
for image_batch,label_batch in dataset.take(1):
    plt.imshow(image_batch[0].numpy().astype("uint8"))
    # print(image_batch[0].shape)
    # print(label_batch.numpy())
    