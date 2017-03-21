from __future__ import print_function, division
import numpy as np
import matplotlib.pyplot as plt
import os # for operating system commands like dealing with paths

DATA_PATH = 'F:/Uni_ETH/0_QBI/Data~' # where are the test.csv and train.csv files located
test_data_path = os.path.join(DATA_PATH, 'test.csv')
train_data_path = os.path.join(DATA_PATH, 'train.csv')

# this takes around 30 seconds so be patient
train_data = np.loadtxt(train_data_path, delimiter = ',', skiprows = 1)
numb_id = train_data[:,0] # just the number id
numb_vec = train_data[:,1:] # the array of the images

print('Input Data:', train_data.shape)
print('Number ID:', numb_id.shape)
print('Number Vector:', numb_vec.shape)

test_vec = np.loadtxt(test_data_path, delimiter = ',', skiprows = 1)
print('Test Vec', test_vec.shape)
test_image = test_vec.reshape(-1, 28, 28)
print('Test Image', test_image.shape)

from sklearn.svm import SVC
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.utils import shuffle
from sklearn.decomposition import PCA
# numb_vec, numb_id, test_vec


rnd_state = np.random.randint(0,128**2)
numb_vecS, numb_idS = shuffle(numb_vec, numb_id, random_state = rnd_state)

scaler = StandardScaler().fit(numb_vecS)
trainData = scaler.transform(numb_vecS)
pca = PCA().fit(trainData)
trainData = pca.transform(trainData)

testData = scaler.transform(test_vec)
testData = pca.transform(testData)

svc = SVC(C = 1, gamma = 1/trainData.shape[1])
svc.fit(trainData, numb_idS)
pred_id = svc.predict(testData)

with open('submission.csv', 'w') as out_file:
    out_file.write('ImageId,Label\n')
    # for img_id, guess_label in enumerate(guess_test_data):
    for img_id, guess_label in enumerate(pred_id):
        out_file.write('%d,%d\n' % (img_id+1, guess_label))