from init import generate_files
from sklearn.svm import LinearSVC
from sklearn.model_selection import  cross_val_score, cross_val_predict

generate_files('violentflows', 'Violence')

