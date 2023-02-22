import importlib.util

def is_module_installed(module_name):
    try:
        spec = importlib.util.find_spec(module_name)
        return spec is not None
    except Exception as e:
        return False

if is_module_installed("docx"):
    print("El módulo docx está instalado en el sistema")
else:
    print("El módulo docx no está instalado en el sistema")
