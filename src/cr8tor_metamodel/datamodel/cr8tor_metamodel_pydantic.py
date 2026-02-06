from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )

    @model_serializer(mode='wrap', when_used='unless-none')
    def treat_empty_lists_as_none(
            self, handler: SerializerFunctionWrapHandler,
            info: SerializationInfo) -> dict[str, Any]:
        if info.exclude_none:
            _instance = self.model_copy()
            for field, field_info in type(_instance).model_fields.items():
                if getattr(_instance, field) == [] and not(
                        field_info.is_required()):
                    setattr(_instance, field, None)
        else:
            _instance = self
        return handler(_instance, info)



class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'cr8tor_metamodel',
     'default_range': 'string',
     'description': 'Cr8tor metamodel project',
     'id': 'https://w3id.org/karectl-crates/cr8tor-metamodel',
     'imports': ['governance_model', 'data_model', 'deployment_model'],
     'license': 'MIT',
     'name': 'cr8tor-metamodel',
     'prefixes': {'PATO': {'prefix_prefix': 'PATO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/PATO_'},
                  'biolink': {'prefix_prefix': 'biolink',
                              'prefix_reference': 'https://w3id.org/biolink/'},
                  'cr8tor_metamodel': {'prefix_prefix': 'cr8tor_metamodel',
                                       'prefix_reference': 'https://w3id.org/karectl-crates/cr8tor-metamodel/'},
                  'example': {'prefix_prefix': 'example',
                              'prefix_reference': 'https://example.org/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'}},
     'see_also': ['https://karectl-crates.github.io/cr8tor-metamodel'],
     'source_file': 'src/cr8tor_metamodel/schema/cr8tor_metamodel.yaml',
     'title': 'cr8tor-metamodel'} )

class GroupMembershipType(str, Enum):
    """
    Type of TRE group membership
    """
    Manual = "Manual"
    """
    Manually assigned group membership
    """
    Automatic = "Automatic"
    """
    Automatically assigned group membership
    """


class DestinationType(str, Enum):
    filestore = "filestore"
    """
    Filestore endpoint
    """
    postgresql = "postgresql"
    """
    PostgreSQL database endpoint
    """



class Governance(ConfiguredBaseModel):
    """
    A Cr8tor project's governance-specific information (e.g. user access and mandatory project details)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/governance-model'})

    users: Optional[list[User]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Governance']} })
    project: Optional[Project] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Governance']} })


class Project(ConfiguredBaseModel):
    """
    Describes the core properties of a cr8tor project
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/governance-model',
         'narrow_mappings': ['schema-org:Project']})

    name: Optional[str] = Field(default=None, description="""Cr8tor project name""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project',
                       'Dataset',
                       'Table',
                       'Column',
                       'Resource',
                       'Environment']} })
    description: Optional[str] = Field(default=None, description="""A brief description of the cr8tor project""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project']} })
    reference: Optional[str] = Field(default=None, description="""Cr8tor project name""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project']} })


class User(ConfiguredBaseModel):
    """
    Represents a user entity associated with a cr8tor project.  
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/governance-model',
         'narrow_mappings': ['schema-org:Person',
                             'schema-org:Organization',
                             'scim:User']})

    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['User'], 'slot_uri': 'schema-org:identifier'} })
    username: Optional[str] = Field(default=None, description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['User'], 'slot_uri': 'schema-org:identifier'} })
    given_name: Optional[str] = Field(default=None, description="""A human-readable name for a things""", json_schema_extra = { "linkml_meta": {'domain_of': ['User'], 'slot_uri': 'schema-org:name'} })
    family_name: Optional[str] = Field(default=None, description="""A human-readable name for a things""", json_schema_extra = { "linkml_meta": {'domain_of': ['User']} })
    affiliation: Optional[str] = Field(default=None, description="""Name of affilitate organisation""", json_schema_extra = { "linkml_meta": {'domain_of': ['User']} })
    email: Optional[str] = Field(default=None, description="""Email address of the user""", json_schema_extra = { "linkml_meta": {'domain_of': ['User']} })
    groups: Optional[list[Group]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['User']} })
    start_date: Optional[datetime ] = Field(default=None, description="""Date and time of when the user's access to the project is active.""", json_schema_extra = { "linkml_meta": {'domain_of': ['User']} })
    expiry_date: Optional[datetime ] = Field(default=None, description="""Date and time of when the user's access to the Cr8tor project expires""", json_schema_extra = { "linkml_meta": {'domain_of': ['User']} })


class Group(ConfiguredBaseModel):
    """
    Represents a KARE group associated with a project
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/governance-model',
         'narrow_mappings': ['scim:Group']})

    value: Optional[str] = Field(default=None, description="""The identifier of the User's group. Typically the group ID.""", json_schema_extra = { "linkml_meta": {'annotations': {'mutability': {'tag': 'mutability', 'value': 'readOnly'}},
         'domain_of': ['Group']} })
    ref: Optional[str] = Field(default=None, description="""The URI of the corresponding Group resource""", json_schema_extra = { "linkml_meta": {'annotations': {'mutability': {'tag': 'mutability', 'value': 'readOnly'},
                         'reference_type': {'tag': 'reference_type', 'value': 'Group'}},
         'domain_of': ['Group']} })
    display: Optional[str] = Field(default=None, description="""A human-readable display name for the group""", json_schema_extra = { "linkml_meta": {'annotations': {'mutability': {'tag': 'mutability', 'value': 'readOnly'}},
         'domain_of': ['Group']} })
    type: Optional[GroupMembershipType] = Field(default=None, description="""A label to convey the type of KARE group membership""", json_schema_extra = { "linkml_meta": {'annotations': {'mutability': {'tag': 'mutability', 'value': 'readOnly'}},
         'domain_of': ['Group', 'Destination', 'Resource']} })


class Ingress(ConfiguredBaseModel):
    """
    Ingress
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/data-model'})

    source: Optional[Source] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Ingress']} })
    destination: Destination = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Ingress']} })
    datasets: Optional[list[Dataset]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Ingress']} })


class Source(ConfiguredBaseModel):
    """
    A source of data in a cr8tor project 
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/data-model'})

    url: Optional[str] = Field(default=None, description="""url""", json_schema_extra = { "linkml_meta": {'domain_of': ['Source', 'Destination', 'Resource']} })


class Destination(ConfiguredBaseModel):
    """
    A destination of data in a cr8tor project 
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/data-model'})

    type: DestinationType = Field(default=..., description="""url""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group', 'Destination', 'Resource']} })
    url: Optional[str] = Field(default=None, description="""url""", json_schema_extra = { "linkml_meta": {'domain_of': ['Source', 'Destination', 'Resource']} })


class Dataset(ConfiguredBaseModel):
    """
    Metadata of source dataset to be extracted that can comprise tables and columns
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/data-model'})

    name: str = Field(default=..., description="""name of the dataset metadata description""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project',
                       'Dataset',
                       'Table',
                       'Column',
                       'Resource',
                       'Environment']} })
    schema_name: str = Field(default=..., description="""name of the dataset schema in the target database""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })
    tables: Optional[list[Table]] = Field(default=[], description="""Target tabular data source""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })
    locations: Optional[list[Union[bool, int, str]]] = Field(default=[], description="""List of data locations/URIs of the dataset during TRE ingestion workflow""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'string'}, {'range': 'integer'}, {'range': 'boolean'}],
         'domain_of': ['Dataset']} })


class Table(ConfiguredBaseModel):
    """
    A table within a dataset
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/data-model'})

    name: str = Field(default=..., description="""Name of the table""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project',
                       'Dataset',
                       'Table',
                       'Column',
                       'Resource',
                       'Environment']} })
    columns: list[Column] = Field(default=..., description="""Columns that make up the table""", json_schema_extra = { "linkml_meta": {'domain_of': ['Table']} })


class Column(ConfiguredBaseModel):
    """
    A column within a table
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/data-model'})

    name: str = Field(default=..., description="""Name of the column""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project',
                       'Dataset',
                       'Table',
                       'Column',
                       'Resource',
                       'Environment']} })
    datatype: str = Field(default=..., description="""Datatype of the column""", json_schema_extra = { "linkml_meta": {'domain_of': ['Column']} })


class Deployment(ConfiguredBaseModel):
    """
    Specifies K8TRE resources including applications requested through a cr8tor project
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/deployment-model'})

    resources: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Deployment']} })
    environment: Optional[Environment] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Deployment']} })


class Resource(ConfiguredBaseModel):
    """
    Abstract class representing a K8TRE resource (e.g. K8TRE application) that can be deployed through a cr8tor project
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/deployment-model'})

    name: str = Field(default=..., description="""Requested resource name""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project',
                       'Dataset',
                       'Table',
                       'Column',
                       'Resource',
                       'Environment']} })
    type: str = Field(default=..., description="""Application type (e.g., jupyterhub, vdi)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group', 'Destination', 'Resource']} })
    url: str = Field(default=..., description="""URL endpoint for the application""", json_schema_extra = { "linkml_meta": {'domain_of': ['Source', 'Destination', 'Resource']} })
    enabled: bool = Field(default=..., description="""Indicates if the application is enabled""", json_schema_extra = { "linkml_meta": {'domain_of': ['Resource']} })


class Jupyter(Resource):
    """
    Configuration for deploying Jupyter workspaces accessible to a cr8tor project
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/deployment-model'})

    auth: Optional[str] = Field(default=None, description="""Indicates the type of authentication to use for jupyter""", json_schema_extra = { "linkml_meta": {'domain_of': ['Jupyter']} })
    name: str = Field(default=..., description="""Requested resource name""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project',
                       'Dataset',
                       'Table',
                       'Column',
                       'Resource',
                       'Environment']} })
    type: str = Field(default=..., description="""Application type (e.g., jupyterhub, vdi)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group', 'Destination', 'Resource']} })
    url: str = Field(default=..., description="""URL endpoint for the application""", json_schema_extra = { "linkml_meta": {'domain_of': ['Source', 'Destination', 'Resource']} })
    enabled: bool = Field(default=..., description="""Indicates if the application is enabled""", json_schema_extra = { "linkml_meta": {'domain_of': ['Resource']} })


class Keycloak(Resource):
    """
    Configuration for deploying Keycloak resources available to a cr8tor project
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/deployment-model'})

    somethingspecific: Optional[str] = Field(default=None, description="""a keycloak specific attribute""", json_schema_extra = { "linkml_meta": {'domain_of': ['Keycloak']} })
    name: str = Field(default=..., description="""Requested resource name""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project',
                       'Dataset',
                       'Table',
                       'Column',
                       'Resource',
                       'Environment']} })
    type: str = Field(default=..., description="""Application type (e.g., jupyterhub, vdi)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group', 'Destination', 'Resource']} })
    url: str = Field(default=..., description="""URL endpoint for the application""", json_schema_extra = { "linkml_meta": {'domain_of': ['Source', 'Destination', 'Resource']} })
    enabled: bool = Field(default=..., description="""Indicates if the application is enabled""", json_schema_extra = { "linkml_meta": {'domain_of': ['Resource']} })


class Environment(ConfiguredBaseModel):
    """
    Definition of additional cr8tor project configuration for the target trusted research environment (TRE)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/deployment-model'})

    name: Optional[str] = Field(default=None, description="""Cr8tor project name""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project',
                       'Dataset',
                       'Table',
                       'Column',
                       'Resource',
                       'Environment']} })


class Cr8tor(ConfiguredBaseModel):
    """
    Container for all cr8tor data
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/cr8tor-metamodel',
         'tree_root': True})

    governance: Governance = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['cr8tor']} })
    ingress: Ingress = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['cr8tor']} })
    deployment: Deployment = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['cr8tor']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Governance.model_rebuild()
Project.model_rebuild()
User.model_rebuild()
Group.model_rebuild()
Ingress.model_rebuild()
Source.model_rebuild()
Destination.model_rebuild()
Dataset.model_rebuild()
Table.model_rebuild()
Column.model_rebuild()
Deployment.model_rebuild()
Resource.model_rebuild()
Jupyter.model_rebuild()
Keycloak.model_rebuild()
Environment.model_rebuild()
Cr8tor.model_rebuild()
