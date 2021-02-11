import os

# User
mock_superuser = {
    'username': 'admin',
    'email': 'admin@admin.com',
    'password': 'admin'
}

# Template
template_name = 'antrag-1.png'
mock_template_path = os.path.join('webserver', 'documents_template', template_name)

mock_template = {
    'file': mock_template_path,
    'description': 'Test template'
}
