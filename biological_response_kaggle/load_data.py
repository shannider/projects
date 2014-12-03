"""
Functions to load the dataset.
"""

import numpy as np
#from sklearn import ensemble

def read_data(file_name):
    """This function is taken from:
    https://github.com/benhamner/BioResponse/blob/master/Benchmarks/csv_io.py
    """
    f = open(file_name,'r')
    #ignore header
    f=f.readlines()
    f=f[1:]	
    samples = []
    target = []
    for l in f:
        sample_ = l.strip().split(',')

	for x in range(len(sample_)):
		if sample_[x]=='':
		       print "#" + str(x)
		       sample_[x]='0'
	if len(sample_)!=1777:
		print "Still Problem"

	sample = [float(x) for x in sample_]
	samples.append(sample)
    return samples

def load():
    """Conveninence function to load all data as numpy arrays.
    """
    print "Loading data..."
    filename_train = 'data/train.csv'
    filename_test = 'data/test.csv'

    train = read_data("train.csv")
    test = read_data("test.csv")
    
    y_train = np.array([x[0] for x in train])
    X_train = np.array([x[1:] for x in train])
   
    print "Train Complete"

    y_test = np.array([x[0] for x in test])
    X_test = np.array([x[1:] for x in test])
    return X_train, y_train, X_test , y_test

if __name__ == '__main__':

    X_train, y_train, X_test ,y_test= load()

