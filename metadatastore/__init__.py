from . import conf, commands

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
# for api
import doct as doc
