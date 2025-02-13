import sys
import os
import json
import bcrypt

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.bus as bus
from db.usuarios import create_usuario, get_usuario, get_usuarios, get_usuario_by_rut, delete_usuario, update_usuario, login_usuario, register_usuario

def handle_create_user(data):
    required_fields = ['rut', 'tipo_usuario', 'correo', 'fono', 'nombre', 'apellido_paterno', 'apellido_materno', 'estado_cuenta', 'contrasena']
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return json.dumps({'error': 'Missing required fields', 'missing_fields': missing_fields})
    
    usuario = create_usuario(
        rut=data['rut'],
        tipo_usuario=data['tipo_usuario'],
        correo=data['correo'],
        fono=data['fono'],
        nombre=data['nombre'],
        apellido_paterno=data['apellido_paterno'],
        apellido_materno=data['apellido_materno'],
        estado_cuenta=data['estado_cuenta'],
        contrasena=data['contrasena']
    )
    return json.dumps(usuario.to_dict_private())

def handle_get_user(data):
    required_fields = ['id_usuario']
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return json.dumps({'error': 'Missing required fields', 'missing_fields': missing_fields})
    
    usuario = get_usuario(data['id_usuario'])
    return json.dumps(usuario.to_dict())

def handle_get_all_users(data):
    usuarios = get_usuarios()
    return json.dumps([usuario.to_dict() for usuario in usuarios])

def handle_update_user(data):
    required_fields = ['id_usuario', 'rut', 'tipo_usuario', 'correo', 'fono', 'nombre', 'apellido_paterno', 'apellido_materno', 'estado_cuenta']
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return json.dumps({'error': 'Missing required fields', 'missing_fields': missing_fields})
    
    usuario = update_usuario(
        id_usuario=data['id_usuario'],
        rut=data['rut'],
        tipo_usuario=data['tipo_usuario'],
        correo=data['correo'],
        fono=data['fono'],
        nombre=data['nombre'],
        apellido_paterno=data['apellido_paterno'],
        apellido_materno=data['apellido_materno'],
        estado_cuenta=data['estado_cuenta']
    )
    return json.dumps(usuario.to_dict())

def handle_delete_user(data):
    required_fields = ['id_usuario']
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return json.dumps({'error': 'Missing required fields', 'missing_fields': missing_fields})
    
    usuario = delete_usuario(data['id_usuario'])
    return json.dumps(usuario.to_dict())

def handle_login_user(data):
    required_fields = ['rut', 'contrasena']
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return json.dumps({'error': 'Missing required fields', 'missing_fields': missing_fields})
    
    usuario = login_usuario(rut=data['rut'], contrasena=data['contrasena'])
    if usuario:
        return json.dumps(usuario.to_dict_private())
    return json.dumps({'error': 'Invalid credentials'})

def handle_register_user(data):
    required_fields = ['rut', 'tipo_usuario', 'correo', 'fono', 'nombre', 'apellido_paterno', 'apellido_materno', 'estado_cuenta', 'contrasena']
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return json.dumps({'error': 'Missing required fields', 'missing_fields': missing_fields})
    
    usuario = register_usuario(
        rut=data['rut'],
        tipo_usuario=data['tipo_usuario'],
        correo=data['correo'],
        fono=data['fono'],
        nombre=data['nombre'],
        apellido_paterno=data['apellido_paterno'],
        apellido_materno=data['apellido_materno'],
        estado_cuenta=data['estado_cuenta'],
        contrasena=data['contrasena']
    )
    return json.dumps(usuario.to_dict_private())

def process_user_service(data):
    name_function = data['name_function']
    data = data['data']

    if name_function == 'create':
        return handle_create_user(data)
    elif name_function == 'get':
        return handle_get_user(data)
    elif name_function == 'all':
        return handle_get_all_users(data)
    elif name_function == 'update':
        return handle_update_user(data)
    elif name_function == 'delete':
        return handle_delete_user(data)
    elif name_function == 'login':
        return handle_login_user(data)
    elif name_function == 'register':
        return handle_register_user(data)
    else:
        return json.dumps({'error': 'Invalid function name'})


