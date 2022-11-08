from blog import app
import io
from os import remove
from blog import db


from blog.database import FileUser

def test_get_pdf_user_correct():
    """obtener el file de un usuario"""

    flask_app =app
    with flask_app.test_client() as test_client:
         data={}
         data['file'] = (io.BytesIO(b"abcdef"), 'imagesScreenshot_10.jpg')
         j = test_client.post('/files/users/1',data=data)
         response = test_client.get('/files/users/1/pdfs')    
         assert response.status_code == 200
        #  assert response.headers['Content-Type']=='application/pdf'
        #  assert response.headers['Content-Disposition']=='inline;filename=output.pdf'

def test_get_img_correct():
    """obtener imagen"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.get('/files/user.png')
        assert response.status_code==200
        assert response.headers['Content-Type'] == 'image/png'


def test_dowload_img():
    """descargar imagen"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.get('/files/downloads/user.png')
        assert response.status_code==200
        assert response.headers['Content-Type'] == 'image/png'

def test_post_img_no_user_no_data():
    """obtener archivos de usuario que no existe sin enviar un archivo"""
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.post('/files/users/0')
        assert response.status_code==400

def test_post_img_no_user():
    """obtener de usuario que no existe """
    data={}
    data['file'] = (io.BytesIO(b"abcdef"), 'imagesScreenshot_10.jpg')
    flask_app =app
    with flask_app.test_client() as test_client:
        response = test_client.post('/files/users/0',data=data)
        assert response.status_code==404
        assert response.json == {"message":"Not found"}

def test_add_user_img(post_body_correct):
    """Actualizar imagen de un usuario"""
    data={}
    data['file'] = (io.BytesIO(b"abcdef"), 'imagesScreenshot_10.jpg')
    flask_app =app
    with flask_app.test_client() as test_client:
        print(post_body_correct)
        response = test_client.post('/files/users/1',data=data)
        assert response.status_code==200
        assert response.json == {"message":"imagen del usuario actualizada con exito"}

def test_put_user_img(post_body_correct_file):
    """Agregar imagen a un usuario"""

    flask_app =app
    with flask_app.test_client() as test_client:
        file=FileUser.query.filter_by(username_id=1).first()
        remove(app.config.get('UPLOAD_FOLDER')+file.name)
        db.session.delete(file)
        db.session.commit()
        response = test_client.post('/files/users/1',data=post_body_correct_file)
        assert response.status_code==201
        assert response.json == {"message":"imagen agregada al usuario con exito"}


def test_get_image_user_incorrect():
    """visualizar imagen  de ususairo que no existe"""

    flask_app =app
    with flask_app.test_client() as test_client:
         response = test_client.get('/files/users/0/imgs')
         assert response.status_code==404
         assert response.json =={"message":"Not Found"}

def test_get_image_user_correct():
    """visualizar imagen de un usuario existente """

    flask_app =app
    with flask_app.test_client() as test_client:
         response = test_client.get('/files/users/1/imgs')
         assert response.status_code==200

def test_get_pdf_user_incorrect():
    """Descargar pdf de usuario que no existe"""

    flask_app =app
    with flask_app.test_client() as test_client:
         response = test_client.get('/files/users/0/pdfs')    
         assert response.status_code==404
         assert response.json == {"message":"Not Found"}
