import json


def get(table_name, conn):
    if conn is not None:
        table_elements = conn[table_name].find()
        for element in table_elements:
            print(element)


def post(file_path, table_name, conn):
    with open(file_path) as file:
        data_read = file.read()
        json_obj_list = json.loads(data_read)
        if conn is not None:
            for json_obj in json_obj_list:
                conn[table_name].insert_one(json_obj)


def delete(table_name, conn):
    if conn is not None:
        conn[table_name].drop()
