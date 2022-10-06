import json
from blog import app
#1
def test_create_user():
    """Se envio el Json vacio"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.post('/auth/user',json={})
        assert response.status_code == 400
        assert response.json == {"message":"bad request"}

def test_create_user_existing(user_existing):
    """Usuario json ya existe"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.post('/auth/user',json=user_existing)
        assert response.status_code == 400
        assert response.json == {"message":"Usuario ya registrado"}

def test_create_user_existing_bad_key(user_bad_json,response_user_bad_json):
    """json incompleto"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.post('/auth/user',json=user_bad_json)
        assert response.status_code == 422
        assert response.json == response_user_bad_json
        
def test_created_new_user(create_new_user):
    """Usuario json no existe"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.post('/auth/user',json=create_new_user)
        assert response.status_code == 201
#2
def test_deleate_no_data():
    """Borrar un usuario que no existe"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.delete('/auth/user',query_string={})
        assert response.status_code == 400
        assert response.json=={"message":"bad request"}

def test_deleate_no_id():
    """Borrar un usuario que no existe"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.delete('/auth/user',query_string={"id":-1})
        assert response.status_code == 404
        assert response.json=={"message":"archivo no existe"}

def test_deleate_existing_user(user_delete):
    """Borrar un usuario que no existe"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.delete('/auth/user',query_string={"id":user_delete})
        assert response.status_code == 204

def test_close_sesion_login():
    """Cerrar sesión"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.get('/auth/login')
        assert response.status_code == 204

def test_error_login():
    """"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.post('/auth/login',json={})
        assert response.status_code == 400
        assert response.json =={"message":"bad request"},400

def test_error_login_post(user_bad_json,response_user_bad_json):
    """"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.post('/auth/login',json=user_bad_json)
        assert response.status_code == 422
        assert response.json == response_user_bad_json

        # create_new_user
#3
def test_login_post(create_new_user):
    """El usuario no existe"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.post('/auth/login',json=create_new_user)
        assert response.status_code == 404
        assert response.json=={"message":"Usuario no existe"}

def test_login_correct(user_existing):
    """El usuario se loguea"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.post('/auth/login',json=user_existing)
        assert response.status_code == 200

#4

def test_get_all_user():
    """El usuario se loguea"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.get('/auth/user/roles')
        assert response.status_code == 200
        assert str(type(response.json['roles'])) =="<class 'list'>"

def test_post_all_user(user_bad_json,response_user_bad_json):
    """agregar un rol error en las keys"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.post('/auth/user/roles',json=user_bad_json)
        assert response.status_code == 422
        assert response.json == response_user_bad_json

def test_post_json_empty():
    """agregar un rol pero con json vacio"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.post('/auth/user/roles',json={})
        assert response.status_code == 400
        assert response.json =={"message":"bad request"}

def test_post_rol_existeng():
    """agregar un rol existente"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.post('/auth/user/roles',json={"name":"edit"})
        assert response.status_code == 400
        assert response.json =={"message":"Role ya registrado"}

def test_post_rol_no_existing(new_role):
    """agregar un nuevo rol"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.post('/auth/user/roles',json=new_role)
        assert response.status_code == 201

def test_delete_rol(id_role):
    """borrar un nuevo rol"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.delete(f'/auth/user/roles',query_string={"id":id_role})
        assert response.status_code == 204

def test_delete_rol_no_existing():
    """borrar un nuevo rol"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.delete('/auth/user/roles',query_string={"id":-1})
        assert response.status_code == 404

#5
def test_put_role_bad_json(id_role):
    """actualizar role con un json que no existe"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.put(f'/auth/user/roles/{id_role}',json={"ds":"kdj"})
        assert response.status_code==422
        assert response.json=={   "ds": ["Unknown field."]}

def test_put_role_empty_json(id_role):
    """actualizar role con un json vacio"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.put(f'/auth/user/roles/{id_role}',json={})
        assert response.status_code==400
        assert response.json=={"message":"bad request"}

def test_put_not_role():
    """actualizar con id de rol no existente"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.put(f'/auth/user/roles/{0}',json={"name":"jfd"})
        assert response.status_code==404
        assert response.json["message"]=="The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."

def test_put_update(id_new_role,new_role_update):
    """actualizar role"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.put(f'/auth/user/roles/{id_new_role}',json={"name":new_role_update["name"]})
        assert response.status_code==200
        assert response.json=={"message":"rol actualizado"}


def test_put_update_rol_existing(name_new_role):
    """actualizar role con dato ya existente"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.put(f'/auth/user/roles/{1}',json={"name":name_new_role})
        assert response.status_code==400
        assert response.json=={"message":"No puede cambiar el rol a uno ya existente"}

def test_post_role_user_empty_jsons():
    """actualizar role con dato ya existente"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.post(f'/auth/user/roles/1',json={})
        assert response.status_code==400
        assert response.json=={"message":"Bat request"}



def test_post_role_user_no_existing():
    """actualizar role con dato ya existente"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.post(f'/auth/user/roles/1',json={"id_user":0})
        assert response.status_code==404
        assert response.json=={"message":"Not found"}


def test_post_role_user_correct():
    """actualizar role con dato ya existente"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.post(f'/auth/user/roles/1',json={"id_user":1})
        assert response.status_code==201
        