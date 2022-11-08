def test_new_user(new_user):
    """
    Se verifica su un nuevo usuario cumple con los parametros dados
    """

    assert new_user.username == 'patkennedy79@gmail.com'
    assert new_user.password != "FlaskIsAwesome"

def test_passwor_encode(new_user_two):
    """Se verifica si la funcion __repr()__ funciona adecuadamente"""
    assert new_user_two.__repr__()==f'User: {new_user_two.username}'

def test_new_post(new_post):
    """Se comprueba el modelo de blog"""
    assert new_post.author==1
    assert new_post.title=="El leon de rio de janeiro"
    assert new_post.body=="as"
    assert new_post.__repr__()== f'Post: {new_post.author}'

def test_new_sale(new_sales):
    """Se comprueba el modelo de sale """
    assert new_sales.username_id==1
    assert new_sales.venta==1212
    assert new_sales.ventas_productos==2343
    assert new_sales.__repr__()== f'Sale: {new_sales.venta}'

def test_new_file(new_files):
    """Se comprueba el modelo de file"""
    assert new_files.name=="imagen6.png"
    assert new_files.username_id==30
    assert new_files.url=="http://127.0.0.1:5000/file/imagen6.png"
    assert new_files.__repr__()==f'Name: {new_files.name}'

def test_new_role(new_roles):
    """Se comprueba el modelo de role"""
    assert new_roles.name=="super_user"
    assert new_roles.__repr__()==f'Role: {new_roles.name}'