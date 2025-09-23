import json
import pickle
import numpy as np


__location =None
__data_columns=None
__model=None




def price(location,total_sqft,bath,bhk , balcony):
    
     try:
        loc_index = __data_columns.index(location.lower())
     except:
        loc_index = -1
     

     x = np.zeros(len(__data_columns))
     x[0] = total_sqft
     x[1] = bath
     x[2] = bhk
     x[3] =balcony
     if loc_index >= 0:
        x[loc_index] = 1
    
    
    
    
     return round  (__model.predict([x])[0],2)
    


def get_location():
    return __location

def load():
    print("loading saved artifacts...start")
    global __data_columns
    global __location
    global __model
    
    
    
    with open("artifacts/columns.json",'r')as f:
       __data_columns= json.load(f)['data_columns']
       __location = __data_columns[4:] 
       
       
    with open("artifacts/Real_Estate_model.pickle",'rb') as f:
        __model = pickle.load(f)
    print("Data columns loaded successfully.")
    

if __name__ == '__main__':
    load()
    print(get_location())
    print(price('1st Phase JP Nagar',1000, 3, 3,2))
    print(price('1st Phase JP Nagar', 1000, 2, 2,1))
    print(price('Kalhalli', 1000, 2, 2,2)) # other location
    print(price('Ejipura', 1000, 2, 2,1))  # other location