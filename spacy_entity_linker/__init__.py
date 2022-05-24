try:  # Python 3.8
    import importlib.metadata as importlib_metadata
except ImportError:
    import importlib_metadata  # noqa: F401

from .EntityLinker import EntityLinker
try:
    pkg_meta = importlib_metadata.metadata(__name__.split(".")[0])
except:
    pkg_meta = {"version": "1.0.1"}
__version__ = pkg_meta["version"]
__all__ = [EntityLinker]
