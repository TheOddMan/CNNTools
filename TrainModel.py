import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K
from TrainModelConfig import *
from numpy.random import seed
import os
from os import system
seed(1)
from tensorflow import set_random_seed
set_random_seed(2)
import xlsxwriter
import arrow


today = arrow.now().format('YYYY-MM-DD_HH-mm-ss')
workbook = xlsxwriter.Workbook('result_' + today + '.xlsx')
sheet = workbook.add_worksheet('result')
highestTrainingAcc = 0
highestValidationAcc = 0
MChighestTraining = ""
MChighestValidation = ""
for montecarlo in range(config_Monte_Carlo_time):
    system('python RandomImage.py')
    # for x in range(3):
    img_width = config_ImageWidth
    img_height = config_ImageHeight

    train_data_dir = config_TrainingDir
    validation_data_dir = config_ValidationDir


    def countSamples(mydir):
        count = 0
        for path, subdirs, files in os.walk(mydir):
            for name in files:
                count += 1

        return count


    nb_train_samples = countSamples(config_TrainingDir)
    nb_validation_samples = countSamples(config_ValidationDir)

    epochs = config_Epochs
    batch_size = config_Batch_Size

    if K.image_data_format() == 'channels_first':
        input_shape = (3, img_width, img_height)
    else:
        input_shape = (img_width, img_height, 3)

    model = Sequential()
    model.add(Conv2D(config_Con_Layer1_Filters, (config_Con_Layer1_Filters_Size, config_Con_Layer1_Filters_Size),
                     input_shape=input_shape, padding='same'))
    model.add(Activation(config_Con_Layer1_Activation))
    if (config_Con_Layer1_Open_Dropout.lower() == 'on'):
        model.add(Dropout(config_Con_Layer1_Dropout_Value))
    if (config_Con_Layer1_Open_MaxPooling.lower() == 'on'):
        model.add(MaxPooling2D(pool_size=(config_Con_Layer1_MaxPooling_Size, config_Con_Layer1_MaxPooling_Size)))

    model.add(Conv2D(config_Con_Layer2_Filters, (config_Con_Layer2_Filters_Size, config_Con_Layer2_Filters_Size),
                     input_shape=input_shape, padding='same'))
    model.add(Activation(config_Con_Layer2_Activation))
    if (config_Con_Layer2_Open_Dropout.lower() == 'on'):
        model.add(Dropout(config_Con_Layer2_Dropout_Value))
    if (config_Con_Layer2_Open_MaxPooling.lower() == 'on'):
        model.add(MaxPooling2D(pool_size=(config_Con_Layer2_MaxPooling_Size, config_Con_Layer2_MaxPooling_Size)))

    model.add(Conv2D(config_Con_Layer3_Filters, (config_Con_Layer3_Filters_Size, config_Con_Layer3_Filters_Size),
                     input_shape=input_shape, padding='same'))
    model.add(Activation(config_Con_Layer3_Activation))
    if (config_Con_Layer3_Open_Dropout.lower() == 'on'):
        model.add(Dropout(config_Con_Layer3_Dropout_Value))
    if (config_Con_Layer3_Open_MaxPooling.lower() == 'on'):
        model.add(MaxPooling2D(pool_size=(config_Con_Layer3_MaxPooling_Size, config_Con_Layer3_MaxPooling_Size)))

    model.add(Flatten())
    for i in range(config_Dense_Layers_amount):
        model.add(Dense(config_Dense_neurons_amount))
        model.add(Activation(config_Dense_Layers_Activation))
        if (config_Dense_Layers_Open_Dropout.lower() == 'on'):
            model.add(Dropout(config_Dense_Layers_Dropout_Value))

    model.add(Dense(config_Classes_amount))  # 更改處
    model.add(Activation('softmax'))

    opt = keras.optimizers.RMSprop(lr=config_Learning_Rate, rho=0.9, epsilon=None, decay=0.0)

    model.compile(loss='categorical_crossentropy',
                  optimizer=opt,
                  metrics=['accuracy'])

    train_datagen = ImageDataGenerator(
        rescale=1. / 255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

    test_datagen = ImageDataGenerator(rescale=1. / 255)

    train_generator = train_datagen.flow_from_directory(
        train_data_dir,
        target_size=(img_width, img_height),
        batch_size=batch_size,
        class_mode='categorical',
        classes=config_Classes_name
    )

    validation_generator = test_datagen.flow_from_directory(
        validation_data_dir,
        target_size=(img_width, img_height),
        batch_size=batch_size,
        class_mode='categorical')

    history = model.fit_generator(
        train_generator,
        steps_per_epoch=nb_train_samples // batch_size,
        epochs=epochs,
        validation_data=validation_generator,
        validation_steps=nb_validation_samples // batch_size
    )
    print('training accuracy : ', history.history['acc'])
    print('validation accuracy : ', history.history['val_acc'])
    print('training accuracy : ', round(history.history['acc'][-1], 3))
    print('validation accuracy : ', round(history.history['val_acc'][-1], 3))

    sheet.write('B1', 'Training Accuracy')
    sheet.write('C1', 'Validation Accuracy')
    sheet.write('A' + str(montecarlo + 2), '蒙地卡羅第' + str(montecarlo + 1) + '個隨機樣本集結果')
    sheet.write('B' + str(montecarlo + 2), round(history.history['acc'][-1], 3))
    sheet.write('C' + str(montecarlo + 2), round(history.history['val_acc'][-1], 3))

    trainingacc = round(history.history['acc'][-1], 3)
    validationacc =  round(history.history['val_acc'][-1], 3)

    if(trainingacc >highestTrainingAcc):
        highestTrainingAcc = trainingacc
        model.save(config_Save_Model_File_Name + '_highestTrainingAcc.h5')
        MChighestTraining = '蒙地卡羅第' + str(montecarlo + 1) + '個隨機樣本集'

    if(validationacc > highestValidationAcc):
        highestValidationAcc = validationacc
        model.save(config_Save_Model_File_Name + '_highestValidationAcc.h5')
        MChighestValidation = '蒙地卡羅第' + str(montecarlo + 1) + '個隨機樣本集'

workbook.close()
print("Training Acc 最高是"+MChighestTraining)
print("Validation Acc 最高是"+MChighestValidation)




