from __future__ import absolute_import, unicode_literals

from .manager import serialize  # NOQA

# TODO(dcramer): we cant seem to use import_submodules here as something is
# wrong w/ the code that causes it to mess up the default_manager instance
from . import app  # NOQA
from . import task  # NOQA
