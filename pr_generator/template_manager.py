import os

def list_templates():
    templates_dir = os.path.join(os.path.dirname(__file__), 'templates')
    return [f for f in os.listdir(templates_dir) if f.endswith('.md')]

def load_template(template_name):
    templates_dir = os.path.join(os.path.dirname(__file__), 'templates')
    template_path = os.path.join(templates_dir, template_name)
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template '{template_name}' not found.")
    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()