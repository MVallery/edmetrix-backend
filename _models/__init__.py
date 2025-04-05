import importlib.util
import pathlib

from user.models import *
from auth.models import *
from school.models import *
from students.models import *

from classes.models import *
from metrix.models import *




# package_dir = pathlib.Path(__file__).parent

# for py_file in package_dir.rglob("*.py"):
#     if py_file.name == "__init__.py":
#         continue
#     module_path = py_file.relative_to(package_dir.parent).with_suffix("")
#     module_name = ".".join(module_path.parts)
#     importlib.import_module(module_name)
    
    
    # import pkgutil
# import importlib
# import pathlib

# package_dir = pathlib.Path(__file__).parent

# for _, module_name, _ in pkgutil.walk_packages([str(package_dir)]):
#     full_module = f"models.{module_name}"
#     print("Importing:", full_module)

#     importlib.import_module(full_module)
    
    
    
#     import pkgutil
# import importlib
# import pathlib

# # Automatically import all Python files inside models/ and subfolders
# package_dir = pathlib.Path(__file__).resolve().parent

# for finder, name, ispkg in pkgutil.walk_packages([str(package_dir)], prefix=f"{__name__}."):
#     importlib.import_module(name)

# for _, module_name, _ in pkgutil.walk_packages([str(package_dir)]):
#   importlib.import_module(f"{__name__}.{module_name}")
    
    
#     # from .class_models.class_subject import Class_Subject  # Import all models here
# # from .class_models.subject import Subject
# # from .class_models.class_model import Class_Model


# # from .user.user import User