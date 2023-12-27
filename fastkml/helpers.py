# Copyright (C) 2023  Christian Ledermann
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
"""Helper functions for fastkml."""
import logging
from enum import Enum
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Type

from fastkml import config
from fastkml.base import _XMLObject
from fastkml.enums import Verbosity
from fastkml.types import Element

logger = logging.getLogger(__name__)


def text_subelement(
    obj: _XMLObject,
    *,
    element: Element,
    attr_name: str,
    node_name: str,
    precision: Optional[int] = None,
    verbosity: Optional[Verbosity] = None,
) -> None:
    """Set the value of an attribute from a subelement with a text node."""
    if getattr(obj, attr_name, None):
        subelement = config.etree.SubElement(  # type: ignore[attr-defined]
            element,
            f"{obj.ns}{node_name}",
        )
        subelement.text = getattr(obj, attr_name)


def bool_subelement(
    obj: _XMLObject,
    *,
    element: Element,
    attr_name: str,
    node_name: str,
    precision: Optional[int] = None,
    verbosity: Optional[Verbosity] = None,
) -> None:
    """Set the value of an attribute from a subelement with a text node."""
    if getattr(obj, attr_name, None) is not None:
        subelement = config.etree.SubElement(  # type: ignore[attr-defined]
            element,
            f"{obj.ns}{node_name}",
        )
        subelement.text = str(int(getattr(obj, attr_name)))


def int_subelement(
    obj: _XMLObject,
    *,
    element: Element,
    attr_name: str,
    node_name: str,
    precision: Optional[int] = None,
    verbosity: Optional[Verbosity] = None,
) -> None:
    """Set the value of an attribute from a subelement with a text node."""
    if getattr(obj, attr_name, None) is not None:
        subelement = config.etree.SubElement(  # type: ignore[attr-defined]
            element,
            f"{obj.ns}{node_name}",
        )
        subelement.text = str(getattr(obj, attr_name))


def float_subelement(
    obj: _XMLObject,
    *,
    element: Element,
    attr_name: str,
    node_name: str,
    precision: Optional[int],
    verbosity: Optional[Verbosity] = None,
) -> None:
    """Set the value of an attribute from a subelement with a text node."""
    if getattr(obj, attr_name, None) is not None:
        subelement = config.etree.SubElement(  # type: ignore[attr-defined]
            element,
            f"{obj.ns}{node_name}",
        )
        subelement.text = str(getattr(obj, attr_name))


def enum_subelement(
    obj: _XMLObject,
    *,
    element: Element,
    attr_name: str,
    node_name: str,
    precision: Optional[int] = None,
    verbosity: Optional[Verbosity] = None,
) -> None:
    """Set the value of an attribute from a subelement with a text node."""
    if getattr(obj, attr_name, None):
        subelement = config.etree.SubElement(  # type: ignore[attr-defined]
            element,
            f"{obj.ns}{node_name}",
        )
        subelement.text = getattr(obj, attr_name).value


def xml_subelement(
    obj: _XMLObject,
    *,
    element: Element,
    attr_name: str,
    node_name: Optional[str] = None,
    precision: Optional[int],
    verbosity: Verbosity,
) -> None:
    if getattr(obj, attr_name, None):
        element.append(
            getattr(obj, attr_name).etree_element(
                precision=precision,
                verbosity=verbosity,
            ),
        )


def xml_subelement_list(
    obj: _XMLObject,
    *,
    element: Element,
    attr_name: str,
    node_name: Optional[str] = None,
    precision: Optional[int],
    verbosity: Verbosity,
) -> None:
    if getattr(obj, attr_name, None):
        for item in getattr(obj, attr_name):
            element.append(item.etree_element(precision=precision, verbosity=verbosity))


def subelement_text_kwarg(
    *,
    element: Element,
    ns: str,
    name_spaces: Optional[Dict[str, str]] = None,
    node_name: str,
    kwarg: str,
    strict: bool,
) -> Dict[str, str]:
    node = element.find(f"{ns}{node_name}")
    if node is None:
        return {}
    return {kwarg: node.text.strip()} if node.text and node.text.strip() else {}


def subelement_bool_kwarg(
    *,
    element: Element,
    ns: str,
    name_spaces: Optional[Dict[str, str]] = None,
    node_name: str,
    kwarg: str,
    strict: bool,
) -> Dict[str, bool]:
    node = element.find(f"{ns}{node_name}")
    if node is None:
        return {}
    if node.text and node.text.strip():
        if strict:
            return {kwarg: bool(int(node.text.strip()))}
        if node.text.strip().lower() in {"1", "true"}:
            return {kwarg: True}
        if node.text.strip().lower() in {"0", "false"}:
            return {kwarg: False}
        try:
            return {kwarg: bool(int(float(node.text.strip())))}
        except ValueError:
            return {}
    return {}


def subelement_int_kwarg(
    *,
    element: Element,
    ns: str,
    name_spaces: Optional[Dict[str, str]] = None,
    node_name: str,
    kwarg: str,
    strict: bool,
) -> Dict[str, int]:
    node = element.find(f"{ns}{node_name}")
    if node is None:
        return {}
    if node.text and node.text.strip():
        try:
            return {kwarg: int(node.text.strip())}
        except ValueError:
            if strict:
                raise
            return {}
    return {}


def subelement_float_kwarg(
    *,
    element: Element,
    ns: str,
    name_spaces: Optional[Dict[str, str]] = None,
    node_name: str,
    kwarg: str,
    strict: bool,
) -> Dict[str, float]:
    node = element.find(f"{ns}{node_name}")
    if node is None:
        return {}
    if node.text and node.text.strip():
        try:
            return {kwarg: float(node.text.strip())}
        except ValueError:
            if strict:
                raise
            return {}
    return {}


def subelement_enum_kwarg(
    *,
    element: Element,
    ns: str,
    name_spaces: Optional[Dict[str, str]] = None,
    node_name: str,
    kwarg: str,
    enum_class: Type[Enum],
    strict: bool,
) -> Dict[str, Enum]:
    node = element.find(f"{ns}{node_name}")
    if node is None:
        return {}
    if node.text and node.text.strip():
        return {kwarg: enum_class(node.text.strip())}
    return {}


def xml_subelement_kwarg(
    *,
    element: Element,
    ns: str,
    name_spaces: Dict[str, str],
    node_name: Optional[str] = None,
    kwarg: str,
    obj_class: Type[_XMLObject],
    strict: bool,
) -> Dict[str, _XMLObject]:
    subelement = element.find(f"{ns}{obj_class.get_tag_name()}")
    if subelement is None:
        return {}
    return {
        kwarg: obj_class.class_from_element(
            ns=ns,
            name_spaces=name_spaces,
            element=subelement,
            strict=strict,
        ),
    }


def xml_subelement_list_kwarg(
    *,
    element: Element,
    ns: str,
    name_spaces: Dict[str, str],
    kwarg: str,
    obj_classes: Tuple[Type[_XMLObject], ...],
    strict: bool,
) -> Dict[str, List[_XMLObject]]:
    args_list = []
    for obj_class in obj_classes:
        if subelements := element.findall(f"{ns}{obj_class.get_tag_name()}"):
            args_list.extend(
                [
                    obj_class.class_from_element(
                        ns=ns,
                        name_spaces=name_spaces,
                        element=subelement,
                        strict=strict,
                    )
                    for subelement in subelements
                ],
            )
    return {kwarg: args_list}
