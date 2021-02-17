
from typing import Dict, List, Optional, Type

from bamboo.endpoint import Endpoint
from bamboo.location import (
    FlexibleLocation, Uri_t, is_flexible_uri, is_duplicated_uri,
)


# Type definition
HTTPMethod_t = str
Uri2Endpoints_t = Dict[Uri_t, Type[Endpoint]]


class DuplicatedUriRegisteredError(Exception):
    """Raised if duplicated URI is registered."""
    pass


class Router:
    """Operator of routing request to `Endpoint` by URI.
    """
    
    def __init__(self) -> None:
        self.uri2endpoint: Uri2Endpoints_t = {}
        self.uris_flexible: List[Uri_t] = []
    
    def register(self, uri: Uri_t, endpoint: Type[Endpoint]) -> None:
        """Register combination of URI and `Endpoint`.

        Parameters
        ----------
        uri : Uri_t
            URI pattern of the `Endpoint`
        endpoint : Type[Endpoint]
            `Endpoint` class to be registered

        Raises
        ------
        DuplicatedUriRegisteredError
            Raised if given URI pattern matches one already registered
        """
        for uri_registered in self.uri2endpoint.keys():
            if is_duplicated_uri(uri_registered, uri):
                raise DuplicatedUriRegisteredError(
                    "Duplicated URIs were detected.")
        
        if is_flexible_uri(uri):
            self.uris_flexible.append(uri)
        self.uri2endpoint[uri] = endpoint
    
    def validate(self, uri: str) -> Optional[Type[Endpoint]]:
        """Validate specified `uri` and retrieved `Endpoint`.

        Parameters
        ----------
        uri : str
            Path of URI

        Returns
        -------
        Optional[Type[Endpoint]]
            `Endpoint` if specified `uri` is valid, else `None`
        """
        uri = tuple(uri[1:].split("/"))
        endpoint = self.uri2endpoint.get(uri)
        if endpoint:
            return endpoint
        
        depth = len(uri)
        for flexible in self.uris_flexible:
            if len(flexible) != depth:
                continue
            
            # Judging each locations
            for loc_req, loc_flex in zip(uri, flexible):
                if loc_req == loc_flex:
                    continue
                if isinstance(loc_flex, FlexibleLocation):
                    if not loc_flex.is_valid(loc_req):
                        break
            else:
                # Correct case
                endpoint = self.uri2endpoint.get(flexible)
                return endpoint
        
        # Could not find it
        return None
    
    def search_uris(self, endpoint: Type[Endpoint]) -> List[Uri_t]:
        """Search URI patterns of specified `endpoint`.

        Parameters
        ----------
        endpoint : Type[Endpoint]
            `Endpoint` whose URI patterns to be retrieved

        Returns
        -------
        List[Uri_t]
            Result of searching
        """
        return [uri for uri, point in self.uri2endpoint.items() 
                if point is endpoint]