import caption_generator
from keras.callbacks import ModelCheckpoint

def train_model(weight = None, batch_size=32, epochs = 10):

    cg = caption_generator.CaptionGenerator()
    model = cg.create_model()

    if weight != None:
        model.load_weights(weight)

    counter = 0
    file_name = 'weights-improvement-{epoch:02d}.hdf5'
    checkpoint = ModelCheckpoint(file_name, monitor='loss', verbose=1, save_best_only=True, mode='min')
    callbacks_list = [checkpoint]
    model.fit_generator(cg.data_generator(batch_size=batch_size), steps_per_epoch=cg.total_samples/batch_size, epochs=epochs, verbose=2, callbacks=callbacks_list)
    try:
        model.save('Models/WholeModel.h5', overwrite=True)
        model.save_weights('Models/Weights.h5',overwrite=True)
    except:
        print ("Error in saving model.")
    print ("Training complete...\n")

if __name__ == '__main__':
    import time
    tic = time.clock()

    train_model(epochs=50)

    toc = time.clock()
    print('Time taken to train with 50 epochs is ', toc - tic)