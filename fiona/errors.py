# Errors.


class FionaValueError(ValueError):
    """Fiona-specific value errors"""


class DriverError(FionaValueError):
    """Encapsulates unsupported driver and driver mode errors."""


class SchemaError(FionaValueError):
    """When a schema mapping has no properties or no geometry."""


class CRSError(FionaValueError):
    """When a crs mapping has neither init or proj items."""


class DataIOError(IOError):
    """IO errors involving driver registration or availability."""


class DriverIOError(IOError):
    """A format specific driver error."""


class DatasetDeleteError(IOError):
    """Failure to delete a dataset"""


class FieldNameEncodeError(UnicodeEncodeError):
    """Failure to encode a field name."""


class UnsupportedGeometryTypeError(KeyError):
    """When a OGR geometry type isn't supported by Fiona."""


class GeometryTypeValidationError(FionaValueError):
    """Tried to write a geometry type not specified in the schema"""


class TransactionError(RuntimeError):
    """Failure relating to GDAL transactions"""
