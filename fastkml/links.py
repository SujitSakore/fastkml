# Copyright (C) 2012-2023 Christian Ledermann
#
# This library is free software; you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation; either version 2.1 of the License, or (at your option)
# any later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this library; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA

from typing import Any
from typing import Dict
from typing import Optional

from fastkml.base import _BaseObject
from fastkml.enums import RefreshMode
from fastkml.enums import Verbosity
from fastkml.enums import ViewRefreshMode
from fastkml.helpers import enum_subelement
from fastkml.helpers import float_subelement
from fastkml.helpers import subelement_enum_kwarg
from fastkml.helpers import subelement_float_kwarg
from fastkml.helpers import subelement_text_kwarg
from fastkml.helpers import text_subelement
from fastkml.types import Element


class Link(_BaseObject):
    """
    Represents a <Link> element.

    A URL can be passed to the constructor, or the href can be set later.
    """

    href: Optional[str]
    refresh_mode: Optional[RefreshMode]
    refresh_interval: Optional[float]
    view_refresh_mode: Optional[ViewRefreshMode]
    view_refresh_time: Optional[float]
    view_bound_scale: Optional[float]
    view_format: Optional[str]
    http_query: Optional[str]

    def __init__(
        self,
        ns: Optional[str] = None,
        name_spaces: Optional[Dict[str, str]] = None,
        id: Optional[str] = None,
        target_id: Optional[str] = None,
        href: Optional[str] = None,
        refresh_mode: Optional[RefreshMode] = None,
        refresh_interval: Optional[float] = None,
        view_refresh_mode: Optional[ViewRefreshMode] = None,
        view_refresh_time: Optional[float] = None,
        view_bound_scale: Optional[float] = None,
        view_format: Optional[str] = None,
        http_query: Optional[str] = None,
    ) -> None:
        """Initialize the KML Icon Object."""
        super().__init__(ns=ns, name_spaces=name_spaces, id=id, target_id=target_id)
        self.href = href
        self.refresh_mode = refresh_mode
        self.refresh_interval = refresh_interval
        self.view_refresh_mode = view_refresh_mode
        self.view_refresh_time = view_refresh_time
        self.view_bound_scale = view_bound_scale
        self.view_format = view_format
        self.http_query = http_query

    def etree_element(
        self,
        precision: Optional[int] = None,
        verbosity: Verbosity = Verbosity.normal,
    ) -> Element:
        element = super().etree_element(precision=precision, verbosity=verbosity)

        text_subelement(
            self,
            element=element,
            attr_name="href",
            node_name="href",
        )
        text_subelement(
            self,
            element=element,
            attr_name="view_format",
            node_name="viewFormat",
        )
        text_subelement(
            self,
            element=element,
            attr_name="http_query",
            node_name="httpQuery",
        )
        enum_subelement(
            self,
            element=element,
            attr_name="refresh_mode",
            node_name="refreshMode",
        )
        enum_subelement(
            self,
            element=element,
            attr_name="view_refresh_mode",
            node_name="viewRefreshMode",
        )
        float_subelement(
            self,
            element=element,
            attr_name="view_refresh_time",
            node_name="viewRefreshTime",
            precision=precision,
        )
        float_subelement(
            self,
            element=element,
            attr_name="refresh_interval",
            node_name="refreshInterval",
            precision=precision,
        )
        float_subelement(
            self,
            element=element,
            attr_name="view_bound_scale",
            node_name="viewBoundScale",
            precision=precision,
        )
        return element

    @classmethod
    def _get_kwargs(
        cls,
        *,
        ns: str,
        name_spaces: Optional[Dict[str, str]] = None,
        element: Element,
        strict: bool,
    ) -> Dict[str, Any]:
        kwargs = super()._get_kwargs(
            ns=ns,
            name_spaces=name_spaces,
            element=element,
            strict=strict,
        )
        kwargs.update(
            subelement_text_kwarg(
                element=element,
                ns=ns,
                node_name="href",
                kwarg="href",
                strict=strict,
            ),
        )
        kwargs.update(
            subelement_text_kwarg(
                element=element,
                ns=ns,
                node_name="viewFormat",
                kwarg="view_format",
                strict=strict,
            ),
        )
        kwargs.update(
            subelement_text_kwarg(
                element=element,
                ns=ns,
                node_name="httpQuery",
                kwarg="http_query",
                strict=strict,
            ),
        )
        kwargs.update(
            subelement_enum_kwarg(
                element=element,
                ns=ns,
                name_spaces=name_spaces,
                node_name="refreshMode",
                kwarg="refresh_mode",
                classes=(RefreshMode,),
                strict=strict,
            ),
        )
        kwargs.update(
            subelement_enum_kwarg(
                element=element,
                ns=ns,
                name_spaces=name_spaces,
                node_name="viewRefreshMode",
                kwarg="view_refresh_mode",
                classes=(ViewRefreshMode,),
                strict=strict,
            ),
        )
        kwargs.update(
            subelement_float_kwarg(
                element=element,
                ns=ns,
                node_name="refreshInterval",
                kwarg="refresh_interval",
                strict=strict,
            ),
        )
        kwargs.update(
            subelement_float_kwarg(
                element=element,
                ns=ns,
                node_name="viewRefreshTime",
                kwarg="view_refresh_time",
                strict=strict,
            ),
        )
        kwargs.update(
            subelement_float_kwarg(
                element=element,
                ns=ns,
                node_name="viewBoundScale",
                kwarg="view_bound_scale",
                strict=strict,
            ),
        )
        return kwargs


class Icon(Link):
    """
    Represents an <Icon> element used in Overlays.

    Defines an image associated with an Icon style or overlay.
    The required <href> child element defines the location
    of the image to be used as the overlay or as the icon for the placemark.
    This location can either be on a local file system or a remote web server.

    Todo:
    ----
    The <gx:x>, <gx:y>, <gx:w>, and <gx:h> elements are used to select one
    icon from an image that contains multiple icons
    (often referred to as an icon palette).
    """
