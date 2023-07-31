try:
    from .settings_production import *
except:
    from .settings_local import *
