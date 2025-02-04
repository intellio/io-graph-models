# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-02-04T01:23:12+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field

from . import KeyValue
from . import Entity


class LocalizedDescription(BaseModel):
    field_odata_type: str
    description: Optional[str] = Field(
        None, description='The description in the localized language.'
    )
    language_tag: Optional[str] = Field(
        None, description='The language tag for the label.'
    )


class LocalizedLabel(BaseModel):
    field_odata_type: str
    is_default: Optional[bool] = Field(
        None, description='Indicates whether the label is the default label.'
    )
    language_tag: Optional[str] = Field(
        None, description='The language tag for the label.'
    )
    name: Optional[str] = Field(None, description='The name of the label.')


class LocalizedName(BaseModel):
    field_odata_type: str
    language_tag: Optional[str] = Field(
        None, description='The language tag for the label.'
    )
    name: Optional[str] = Field(None, description='The name in the localized language.')


class RelationType(Enum):
    pin = 'pin'
    reuse = 'reuse'
    unknown_future_value = 'unknownFutureValue'


class TermGroupScope(Enum):
    global_ = 'global'
    system = 'system'
    site_collection = 'siteCollection'
    unknown_future_value = 'unknownFutureValue'


class Group(Entity):
    field_odata_type: str
    created_date_time: Optional[datetime] = Field(
        None, description='Date and time of the group creation. Read-only.'
    )
    description: Optional[str] = Field(
        None, description='Description that gives details on the term usage.'
    )
    display_name: Optional[str] = Field(None, description='Name of the group.')
    parent_site_id: Optional[str] = Field(
        None, description='ID of the parent site of this group.'
    )
    scope: Optional[Union[TermGroupScope, Dict[str, Any]]] = Field(
        None,
        description='Returns the type of the group. Possible values are: global, system, and siteCollection.',
    )
    sets: Optional[List[Set]] = Field(
        None, description='All sets under the group in a term [store].'
    )


class Relation(Entity):
    field_odata_type: str
    from_term: Optional[Union[Term, Dict[str, Any]]] = Field(
        None,
        description='The from [term] of the relation. The term from which the relationship is defined. A null value would indicate the relation is directly with the [set].',
    )
    relationship: Optional[Union[RelationType, Dict[str, Any]]] = Field(
        None, description='The type of relation. Possible values are: pin, reuse.'
    )
    set: Optional[Union[Set, Dict[str, Any]]] = Field(
        None, description='The [set] in which the relation is relevant.'
    )
    to_term: Optional[Union[Term, Dict[str, Any]]] = Field(
        None,
        description='The to [term] of the relation. The term to which the relationship is defined.',
    )


class Set(Entity):
    field_odata_type: str
    children: Optional[List[Term]] = Field(
        None, description='Children terms of set in term [store].'
    )
    created_date_time: Optional[datetime] = Field(
        None, description='Date and time of set creation. Read-only.'
    )
    description: Optional[str] = Field(
        None, description='Description that gives details on the term usage.'
    )
    localized_names: Optional[List[LocalizedName]] = Field(
        None, description='Name of the set for each languageTag.'
    )
    parent_group: Optional[Group] = None
    properties: Optional[List[KeyValue]] = Field(
        None, description='Custom properties for the set.'
    )
    relations: Optional[List[Relation]] = Field(
        None,
        description='Indicates which terms have been pinned or reused directly under the set.',
    )
    terms: Optional[List[Term]] = Field(
        None, description='All the terms under the set.'
    )


class Store(Entity):
    field_odata_type: str
    default_language_tag: Optional[str] = Field(
        None, description='Default language of the term store.'
    )
    groups: Optional[List[Group]] = Field(
        None, description='Collection of all groups available in the term store.'
    )
    language_tags: Optional[List[str]] = Field(
        None, description='List of languages for the term store.'
    )
    sets: Optional[List[Set]] = Field(
        None,
        description='Collection of all sets available in the term store. This relationship can only be used to load a specific term set.',
    )


class Term(Entity):
    field_odata_type: str
    children: Optional[List[Term]] = Field(
        None, description='Children of current term.'
    )
    created_date_time: Optional[datetime] = Field(
        None, description='Date and time of term creation. Read-only.'
    )
    descriptions: Optional[List[LocalizedDescription]] = Field(
        None, description='Description about term that is dependent on the languageTag.'
    )
    labels: Optional[List[LocalizedLabel]] = Field(
        None, description='Label metadata for a term.'
    )
    last_modified_date_time: Optional[datetime] = Field(
        None, description='Last date and time of term modification. Read-only.'
    )
    properties: Optional[List[KeyValue]] = Field(
        None, description='Collection of properties on the term.'
    )
    relations: Optional[List[Relation]] = Field(
        None,
        description='To indicate which terms are related to the current term as either pinned or reused.',
    )
    set: Optional[Union[Set, Dict[str, Any]]] = Field(
        None, description='The [set] in which the term is created.'
    )

