import json
import pickle

__location =None
__data_columns=None
__model=None


def get_location():
    return __location

def load():
    print("loading saved artifacts...start")
    global __data_columns
    global __location
    #global __model
    
    with open("Server/artifacts/columns.json",'r')as f:
       __data_columns= json.load(f)
       __location = __data_columns[3:] 
       
       
    with open("Server\artifacts\Real_Estate_model.pickle",'rb') as f:
        __model = pickle.load(f)
    print("Data columns loaded successfully.")
    

if __name__ == '__main__':
    print(get_location())