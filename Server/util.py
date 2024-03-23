import json
import pickle
import numpy as np


__location =None
__data_columns=None
__model=None


def price(location,total_sqft,bath, balcony, bhk):
    
     loc_index = np.where(X.columns==location)[0][0]

    x = np.zeros(len(X.columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    x[3] =balcony
    if loc_index >= 0:
        x[loc_index] = 1
    
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    return __model.predict([x])
    


def get_location():
    return __location

def load():
    print("loading saved artifacts...start")
    global __data_columns
    global __location
    #global __model
    
    
    
    with open("Server/artifacts/columns.json",'r')as f:
       __data_columns= json.load(f)['data_columns']
       __location = __data_columns[4:] 
       
       
    with open("Server/artifacts/Real_Estate_model.pickle",'rb') as f:
        __model = pickle.load(f)
    print("Data columns loaded successfully.")
    

if __name__ == '__main__':
    load()
    print(get_location())