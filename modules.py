# Módulos: own modules, thirdy party modules e python modules
# Python Module Index: https://docs.python.org/3/py-modindex.html
# PyPI: https://pypi.org/

# Usando o módulo do Python datetime 
# Basic date and time types: https://docs.python.org/3/library/datetime.html
import datetime

print(datetime.date.today())

# Importar apenas uma função

from datetime import timedelta

print(datetime.timedelta(minutes=70))
print(datetime.timedelta(minutes=100))
