from blog import app

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
def test_created_new_user(create_new_user):
    """Usuario json no existe"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.post('/auth/user',json=create_new_user)
        assert response.status_code == 201

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
      