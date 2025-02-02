# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-02-03T05:27:31+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field
from typing_extensions import Annotated




class LocalizedDescription(BaseModel):
    description: Annotated[
        Optional[str], Field(description='The description in the localized language.')
    ] = None
    language_tag: Annotated[
        Optional[str], Field(description='The language tag for the label.')
    ] = None
    field_odata_type: str


class LocalizedLabel(BaseModel):
    is_default: Annotated[
        Optional[bool],
        Field(description='Indicates whether the label is the default label.'),
    ] = None
    language_tag: Annotated[
        Optional[str], Field(description='The language tag for the label.')
    ] = None
    name: Annotated[Optional[str], Field(description='The name of the label.')] = None
    field_odata_type: str


class LocalizedName(BaseModel):
    language_tag: Annotated[
        Optional[str], Field(description='The language tag for the label.')
    ] = None
    name: Annotated[
        Optional[str], Field(description='The name in the localized language.')
    ] = None
    field_odata_type: str


class RelationType(Enum):
    pin = 'pin'
    reuse = 'reuse'
    unknown_future_value = 'unknownFutureValue'


class TermGroupScope(Enum):
    global_ = 'global'
    system = 'system'
    site_collection = 'siteCollection'
    unknown_future_value = 'unknownFutureValue'


class LocalizedNameCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[List[LocalizedName]] = None


class LocalizedDescriptionCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[List[LocalizedDescription]] = None


class LocalizedLabelCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[List[LocalizedLabel]] = None


class Group(Entity):
    created_date_time: Annotated[
        Optional[datetime],
        Field(
            description='Date and time of the group creation. Read-only.',
            pattern='^[0-9]{4,}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]{1,12})?(Z|[+-][0-9][0-9]:[0-9][0-9])$',
        ),
    ] = None
    description: Annotated[
        Optional[str],
        Field(description='Description that gives details on the term usage.'),
    ] = None
    display_name: Annotated[Optional[str], Field(description='Name of the group.')] = (
        None
    )
    parent_site_id: Annotated[
        Optional[str], Field(description='ID of the parent site of this group.')
    ] = None
    scope: Annotated[
        Optional[Union[TermGroupScope, Dict[str, Any]]],
        Field(
            description='Returns the type of the group. Possible values are: global, system, and siteCollection.'
        ),
    ] = None
    sets: Annotated[
        Optional[List[Set]],
        Field(description='All sets under the group in a term [store].'),
    ] = None
    field_odata_type: str


class Relation(Entity):
    relationship: Annotated[
        Optional[Union[RelationType, Dict[str, Any]]],
        Field(description='The type of relation. Possible values are: pin, reuse.'),
    ] = None
    from_term: Annotated[
        Optional[Union[Term, Dict[str, Any]]],
        Field(
            description='The from [term] of the relation. The term from which the relationship is defined. A null value would indicate the relation is directly with the [set].'
        ),
    ] = None
    set: Annotated[
        Optional[Union[Set, Dict[str, Any]]],
        Field(description='The [set] in which the relation is relevant.'),
    ] = None
    to_term: Annotated[
        Optional[Union[Term, Dict[str, Any]]],
        Field(
            description='The to [term] of the relation. The term to which the relationship is defined.'
        ),
    ] = None
    field_odata_type: str


class Set(Entity):
    created_date_time: Annotated[
        Optional[datetime],
        Field(
            description='Date and time of set creation. Read-only.',
            pattern='^[0-9]{4,}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]{1,12})?(Z|[+-][0-9][0-9]:[0-9][0-9])$',
        ),
    ] = None
    description: Annotated[
        Optional[str],
        Field(description='Description that gives details on the term usage.'),
    ] = None
    localized_names: Annotated[
        Optional[List[LocalizedName]],
        Field(description='Name of the set for each languageTag.'),
    ] = None
    properties: Annotated[
        Optional[List[KeyValue]], Field(description='Custom properties for the set.')
    ] = None
    children: Annotated[
        Optional[List[Term]],
        Field(description='Children terms of set in term [store].'),
    ] = None
    parent_group: Optional[Group] = None
    relations: Annotated[
        Optional[List[Relation]],
        Field(
            description='Indicates which terms have been pinned or reused directly under the set.'
        ),
    ] = None
    terms: Annotated[
        Optional[List[Term]], Field(description='All the terms under the set.')
    ] = None
    field_odata_type: str


class Store(Entity):
    default_language_tag: Annotated[
        Optional[str], Field(description='Default language of the term store.')
    ] = None
    language_tags: Annotated[
        Optional[List[str]], Field(description='List of languages for the term store.')
    ] = None
    groups: Annotated[
        Optional[List[Group]],
        Field(description='Collection of all groups available in the term store.'),
    ] = None
    sets: Annotated[
        Optional[List[Set]],
        Field(
            description='Collection of all sets available in the term store. This relationship can only be used to load a specific term set.'
        ),
    ] = None
    field_odata_type: str


class Term(Entity):
    created_date_time: Annotated[
        Optional[datetime],
        Field(
            description='Date and time of term creation. Read-only.',
            pattern='^[0-9]{4,}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]{1,12})?(Z|[+-][0-9][0-9]:[0-9][0-9])$',
        ),
    ] = None
    descriptions: Annotated[
        Optional[List[LocalizedDescription]],
        Field(
            description='Description about term that is dependent on the languageTag.'
        ),
    ] = None
    labels: Annotated[
        Optional[List[LocalizedLabel]], Field(description='Label metadata for a term.')
    ] = None
    last_modified_date_time: Annotated[
        Optional[datetime],
        Field(
            description='Last date and time of term modification. Read-only.',
            pattern='^[0-9]{4,}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]{1,12})?(Z|[+-][0-9][0-9]:[0-9][0-9])$',
        ),
    ] = None
    properties: Annotated[
        Optional[List[KeyValue]],
        Field(description='Collection of properties on the term.'),
    ] = None
    children: Annotated[
        Optional[List[Term]], Field(description='Children of current term.')
    ] = None
    relations: Annotated[
        Optional[List[Relation]],
        Field(
            description='To indicate which terms are related to the current term as either pinned or reused.'
        ),
    ] = None
    set: Annotated[
        Optional[Union[Set, Dict[str, Any]]],
        Field(description='The [set] in which the term is created.'),
    ] = None
    field_odata_type: str


class StoreCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[List[Store]] = None


class SetCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[List[Set]] = None


class TermCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[List[Term]] = None


class RelationCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[List[Relation]] = None


class GroupCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[List[Group]] = None



from . import KeyValue
from . import BaseCollectionPaginationCountResponse
from . import Entity

Group.model_rebuild()
Relation.model_rebuild()
Set.model_rebuild()
