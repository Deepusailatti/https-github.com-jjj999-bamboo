
import sys


if "__python_version" not in globals():
    python_version = sys.version_info
    __python_version = float(f"{python_version.major}.{python_version.minor}")
    

from bamboo.util.version import VersionState as _VersionState
from bamboo.util.version import resolve_version as _resolve_version


__version__ = _resolve_version(0, 2, 1, _VersionState.alpha)

from bamboo.api import (
    ApiData, ValidationFailedError, BinaryApiData, InvalidAnnotationError,
    JsonApiData, XWWWFormUrlEncodedData,
)

from bamboo.app import (
    App, ParcelConfig, ATTR_PARCEL, VersionConfig, ATTR_VERSION,
)

from bamboo.base import (
    ContentType, ContentTypeHolder, MediaTypes, HTTPMethods, HTTPStatus,
)

from bamboo.endpoint import (
    StatusCodeAlreadySetError, Endpoint, ATTR_DATA_FORMAT, DataFormatInfo,
    get_data_format_info, data_format, ATTR_HEADERS_REQUIRED, 
    RequiredHeaderInfo, get_required_header_info, has_header_of,
    ATTR_CLIENT_RESTRICTED, get_restricted_ip_info, restricts_client,
    ATTR_ERRORS, get_errors_info, may_occur, _get_bamboo_attr,
)

from bamboo.error import (
    ErrInfoBase, ApiErrInfo, DEFAULT_NOT_FOUND_ERROR, 
    DEFUALT_INCORRECT_DATA_FORMAT_ERROR, DEFAULT_HEADER_NOT_FOUND_ERROR,
    DEFAULT_NOT_APPLICABLE_IP_ERROR,
)

from bamboo.location import (
    FlexibleLocation, is_flexible_uri, is_duplicated_uri,
    AsciiDigitLocation, AnyStringLocation,
)

from bamboo.router import DuplicatedUriRegisteredError, Router

from bamboo.test import ServerForm, TestExecutor
