##################################################
## FileName: ohmypydb.py
##################################################
## Author: RDinmore
## Date: 2020.06.27
## Purpose: database functions
## Libs: pandas
## Path: db/ohmypydb.py
##################################################

import pandas as pd

def get_face_id(face_vector, name_id):
    data = pd.read_csv("face_data.csv")
    face_id = data['face_vector'] == face_vector
    face_id = data[face_id]

    if face_id.shape[0] == 0:
        max_id = data.loc[data['face_id'].idxmax()]
        max_id = max_id['face_id'] + 1
        row = [{'face_id': max_id, 'face_vector': face_vector, 'name_id': name_id}]
        new_df = pd.DataFrame(row)

        with open("face_data.csv", 'a') as f:
            new_df.to_csv(f, header=True)

        return (max_id)

    return face_id['face_id'].to_string(index=False)

def get_name_id(name):
    data = pd.read_csv("name_data.csv")
    name_id = data[data['full_name'] == name]['name_id']

    if name_id.shape[0] == 0:
        max_id = data.loc[data['name_id'].idxmax()]
        max_id = max_id['name_id'] + 1
        row = [{'name_id':max_id,'full_name':name}]
        new_df = pd.DataFrame(row)
        with open("name_data.csv",'a') as f:
            new_df.to_csv(f, header=False)

        return (max_id)

    return name_id.to_string(index=False)


def insert_face(face_vector, name):
    name_id = get_name_id(name)
    get_face_id(face_vector,name_id)

def get_data():
    face_data = pd.read_csv("face_data.csv")
    name_data = pd.read_csv("name_data.csv")
    df = name_data.join(face_data.set_index('name_id'), lsuffix='_other', on='name_id')
    #return_df = df['full_name','face_vector'].copy()

    return df[["full_name","face_vector"]]