import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import pickle
import os
from config import BASE_DIR, important_features

DATA_PATH = os.path.join(BASE_DIR, 'data', 'data_for_train', 'generated_data.csv')
MODEL_PATH = os.path.join(BASE_DIR, 'data', 'models', 'multi_model.pickle')
SEED = 23

def train_model(classifier, data):
    train_x = data[important_features]
    train_y = data['cls']
    model = classifier.fit(train_x, train_y)
    return model


if __name__ == '__main__':
    df = pd.read_csv(DATA_PATH, index_col='idx')
    classifier = KNeighborsClassifier(n_neighbors=7,
                                      p=1,
                                      weights='distance')
    multi_model = train_model(classifier=classifier,
                              data=df)
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(multi_model, f)
