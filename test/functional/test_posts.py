import json
from blog import app

def test_get_all_post():
    """obtener todos los post existentes"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.get('/posts')
        assert response.status_code == 200
        assert str(type(response.json['post'])) =="<class 'list'>"


def test_create_post_empty(post_user_bad):
    """obtener todos los post existentes pero de un usuario que  no existe"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.post('/posts',json=post_user_bad)
        assert response.status_code == 404
        assert response.json=={"message": "Usuario no existe"}

def test_create_post_body_bad(post_boby_bad_write):
    """obtener todos los post existentes pero con un json defectuoso"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.post('/posts',json=post_boby_bad_write)
        assert response.status_code == 422

def test_create_post_empty_field():
    """crear post pero con json vacio"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.post('/posts',json={})
        assert response.status_code == 400  
        assert response.json=={"message":"bad request"}


def test_create_post_correct(post_correct):
    """crear  post """
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.post('/posts',json=post_correct)
        assert response.status_code == 201  
        assert str(type(response.json['post_id']))=="<class 'int'>"


def test_deleate_param_incorrect():
    """borrar post con parametro mal escrito"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.delete('/posts',query_string={"i":-1})
        assert response.status_code == 422
   

def test_deleate_not_found():
    """Borrar post que no existe"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.delete('/posts',query_string={"id":3})
        assert response.status_code == 404
        assert response.json=={"message":"Not found"}

def test_deleate_correct(delete_post):
    """Borrar post"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.delete('/posts',query_string={"id":delete_post})
        assert response.status_code == 204

def test_put_no_post(modificated_post):
    """Borrar un usuario que no existe"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.put('/posts',json=modificated_post)
        assert response.status_code == 404
        assert response.json == {"message":"Not Found"}

def test_put_no_body(post_no_body):
    """Borrar un usuario que no existe"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.put('/posts',json=post_no_body)
        assert response.status_code == 422

def test_put_no_field():
    """Actualizar post  que le falta un parametro"""
    flask_app=app
    with flask_app.test_client() as test_client:
        response = test_client.put('/posts',json= {"id":2,"title":"body"})
        assert response.status_code == 400
        assert response.json=={"message":"bad request"}

def test_put_correct(post_body_correct):
    """Actualiar post"""
    flask_app=app
    with flask_app.test_client() as test_client:
        response = test_client.put('/posts',json= post_body_correct)
        assert response.status_code == 200
        assert response.json=={"message":"Post actualizado correctamente"}

def test_get_post_user_no_existing():
    """Post de usuario que no existe"""
    flask_app=app
    with flask_app.test_client() as test_client:
        response = test_client.get('/posts/user/0/posts')
        assert response.status_code == 404
        assert response.json=={"message":"Not Found"}

def test_get_post_user():
    """post de un usuario en especifico"""
    flask_app=app
    with flask_app.test_client() as test_client:
        response = test_client.get('/posts/user/1/posts')
        assert response.status_code == 200
        assert str(type(response.json['post'])) =="<class 'list'>"

def test_get_post_individual_no_existing():
    """Post individual que no existe"""
    flask_app=app
    with flask_app.test_client() as test_client:
        response = test_client.get('/posts/0')
        assert response.status_code == 404
        assert response.json == {"message":"Not Found"}

def test_get_post_individual():
    """Posts individual"""
    flask_app=app
    with flask_app.test_client() as test_client:
        response = test_client.get('/posts/2')
        assert response.status_code == 200
