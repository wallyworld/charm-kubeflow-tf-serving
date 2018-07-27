from pathlib import Path
from charmhelpers.core import hookenv


def get_model_from_resource():
    filename = hookenv.resource_get('model')
    if not filename:
        return None
    filepath = Path(filename)
    if not filepath.exists():
        return None
    if filepath.stat().st_size == 0:
        return None
    return filename


def get_model_from_config():
    return hookenv.config('model')
