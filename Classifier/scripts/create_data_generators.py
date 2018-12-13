import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def create_data_generators(data_src_path, shapeY, shapeX, train_batch_size = 5, validation_batch_size = 10, rotation_range = 0, width_shift_range = 0, height_shift_range = 0, shear_range = 0, zoom_range = 0, class_mode = 'binary'):

  # Define our example directories and files
  train_dir = os.path.join(data_src_path, 'Train')
  validation_dir = os.path.join(data_src_path, 'Test')



  # Add our data-augmentation parameters to ImageDataGenerator
  train_datagen = ImageDataGenerator(
      rescale=1./255,
      rotation_range=rotation_range,
      width_shift_range=width_shift_range,
      height_shift_range=height_shift_range,
      shear_range=shear_range,
      zoom_range=zoom_range)#,
      #horizontal_flip=False)

  # Note that the validation data should not be augmented!
  test_datagen = ImageDataGenerator(rescale=1./255)

  train_generator = train_datagen.flow_from_directory(
          train_dir, # This is the source directory for training images
          target_size=(shapeY, shapeX),  # All images will be resized to 150x150
          batch_size=train_batch_size,
          # Since we use binary_crossentropy loss, we need binary labels
          class_mode=class_mode)

  # Flow validation images in batches of 20 using test_datagen generator
  validation_generator = test_datagen.flow_from_directory(
          validation_dir,
          target_size=(shapeY, shapeX),
          batch_size=validation_batch_size,
          class_mode=class_mode)
  
  return train_generator, validation_generator