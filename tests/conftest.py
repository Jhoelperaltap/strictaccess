import sys, os
# Añade ../src al path para que pytest encuentre el paquete strictaccess
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))