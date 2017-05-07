from init import predict
import os
import numpy as np

root_path = 'violentflows'
save_path = os.path.join(root_path, 'generated')
method = 'mean'

x_train_bow = np.load(os.path.join(save_path, method, 'xtrainbow.npy'))
x_test_bow = np.load(os.path.join(save_path, method, 'xtestbow.npy'))
y_train = np.load(os.path.join(save_path, 'ytrain.npy'))
y_test = np.load(os.path.join(save_path, 'ytest.npy'))

print()
print('Method', method)
predict(x_train_bow, x_test_bow, y_train, y_test)
print()

method = 'max'

x_train_bow = np.load(os.path.join(save_path, method, 'xtrainbow.npy'))
x_test_bow = np.load(os.path.join(save_path, method, 'xtestbow.npy'))
y_train = np.load(os.path.join(save_path, 'ytrain.npy'))
y_test = np.load(os.path.join(save_path, 'ytest.npy'))

print('Method', method)
predict(x_train_bow, x_test_bow, y_train, y_test)
