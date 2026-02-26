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
                  'schemaorg': {'prefix_prefix': 'schemaorg',
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


class ActionType(str, Enum):
    """
    Types of actions that can be performed on a Cr8tor project
    """
    Action = "Action"
    """
    Generic action type
    """
    CreateAction = "CreateAction"
    """
    Action to create or initialize a project
    """
    AssessAction = "AssessAction"
    """
    Action to assess or evaluate a project (e.g., validation, disclosure check)
    """
    UpdateAction = "UpdateAction"
    """
    Action to update project metadata or resources
    """
    OrchestrationAction = "OrchestrationAction"
    """
    Action to orchestrate deployment or provisioning
    """


class ActionStatusType(str, Enum):
    """
    Status states for actions, based on schema.org ActionStatusType
    """
    ActiveActionStatus = "ActiveActionStatus"
    """
    Action is currently in progress
    """
    CompletedActionStatus = "CompletedActionStatus"
    """
    Action completed successfully
    """
    FailedActionStatus = "FailedActionStatus"
    """
    Action failed with errors
    """
    PotentialActionStatus = "PotentialActionStatus"
    """
    Action is potential but not yet started
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


class ConnectionType(str, Enum):
    """
    VDI connection protocols.
    """
    rdp = "rdp"
    """
    Remote Desktop Protocol.
    """
    vnc = "vnc"
    """
    Virtual Network Computing.
    """



class Governance(ConfiguredBaseModel):
    """
    Represents the governance structure of a Cr8tor project, encapsulating user access control, project membership, and mandatory project metadata. This class manages the relationships between users and the project, ensuring proper access and compliance with governance requirements.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/governance-model'})

    project: Project = Field(default=..., description="""The project entity governed by this governance model, containing core project metadata and state.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Governance', 'VDI']} })
    users: Optional[list[User]] = Field(default=[], description="""List of users who have access to the project, each with their own roles, permissions, and membership details. Represents the state of project membership and access control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Governance']} })


class Project(ConfiguredBaseModel):
    """
    Defines the core state and identifying properties of a Cr8tor project, including its name, description, and reference information. This class models the essential metadata required to uniquely identify and describe a project within the Cr8tor ecosystem.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/governance-model',
         'narrow_mappings': ['schemaorg:Project']})

    id: Optional[str] = Field(default=None, description="""Unique identifier for the project""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project', 'Action', 'User']} })
    name: str = Field(default=..., description="""The unique name of the Cr8tor project, used for identification and reference within the system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project',
                       'Action',
                       'Source',
                       'Dataset',
                       'Table',
                       'Column',
                       'Resource',
                       'Environment',
                       'KeycloakClientConfig',
                       'SecretRef',
                       'ProtocolMapper',
                       'EnvironmentVariable']} })
    description: str = Field(default=..., description="""A brief summary describing the purpose, scope, or objectives of the Cr8tor project.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project', 'ProjectSpec', 'GroupSpec', 'ProfileConfig']} })
    reference: Optional[str] = Field(default=None, description="""An external or internal reference identifier for the Cr8tor project, used for cross-referencing or linking to related resources.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project']} })
    start_time: Optional[str] = Field(default=None, description="""Timestamp when project was created""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project', 'Action']} })
    actions: Optional[list[Union[Action,CreateAction,AssessAction]]] = Field(default=[], description="""List of actions performed on the cr8tor project""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project']} })


class Action(ConfiguredBaseModel):
    """
    Represents an action or activity performed on a Cr8tor project, tracking the lifecycle  and state changes of the project. Based on schema.org Action and the Provenance Crate Profile  specification. Actions track operations like create, assess, validate, etc.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/governance-model',
         'narrow_mappings': ['schemaorg:Action']})

    action_type: Literal["Action"] = Field(default="Action", description="""The specific type of action being performed (e.g., CreateAction, AssessAction).""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Action']} })
    id: str = Field(default=..., description="""Unique identifier for the action, typically formatted as '{command_type}-{project_id}'.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project', 'Action', 'User']} })
    name: str = Field(default=..., description="""Human-readable name describing the action (e.g., \"CREATE Data Project Action\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project',
                       'Action',
                       'Source',
                       'Dataset',
                       'Table',
                       'Column',
                       'Resource',
                       'Environment',
                       'KeycloakClientConfig',
                       'SecretRef',
                       'ProtocolMapper',
                       'EnvironmentVariable']} })
    start_time: datetime  = Field(default=..., description="""The date and time when the action started execution.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project', 'Action']} })
    end_time: datetime  = Field(default=..., description="""The date and time when the action completed or failed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Action']} })
    action_status: ActionStatusType = Field(default=..., description="""The current status of the action, indicating whether it's active, completed, failed, or potential. Formatted based on schema.org ActionStatus and Provenance Crate Profile specification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Action']} })
    agent: str = Field(default=..., description="""The agent (person, organization, or software) that triggered or performed the action. Can reference a Person, Organization, or SoftwareApplication entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Action']} })
    instrument: Optional[str] = Field(default=None, description="""The tool or service that executed the action (e.g., 'cr8tor CLI', 'GitHub Action',  specific TRE service). Maps to schema.org Action.instrument.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Action']} })
    result: Optional[list[str]] = Field(default=[], description="""List of result items produced by the action, typically ID references to other  data or context entities created or modified by the action.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Action']} })
    error: Optional[str] = Field(default=None, description="""Error message or output if the action failed. Only present when action_status is FailedActionStatus.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Action']} })


class CreateAction(Action):
    """
    Represents a create action performed on a Cr8tor project, typically used to track project initialization and creation events. Inherits all properties from Action.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/governance-model',
         'narrow_mappings': ['schemaorg:CreateAction']})

    action_type: Literal["CreateAction"] = Field(default="CreateAction", description="""The specific type of action being performed (e.g., CreateAction, AssessAction).""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Action']} })
    id: str = Field(default=..., description="""Unique identifier for the action, typically formatted as '{command_type}-{project_id}'.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project', 'Action', 'User']} })
    name: str = Field(default=..., description="""Human-readable name describing the action (e.g., \"CREATE Data Project Action\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project',
                       'Action',
                       'Source',
                       'Dataset',
                       'Table',
                       'Column',
                       'Resource',
                       'Environment',
                       'KeycloakClientConfig',
                       'SecretRef',
                       'ProtocolMapper',
                       'EnvironmentVariable']} })
    start_time: datetime  = Field(default=..., description="""The date and time when the action started execution.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project', 'Action']} })
    end_time: datetime  = Field(default=..., description="""The date and time when the action completed or failed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Action']} })
    action_status: ActionStatusType = Field(default=..., description="""The current status of the action, indicating whether it's active, completed, failed, or potential. Formatted based on schema.org ActionStatus and Provenance Crate Profile specification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Action']} })
    agent: str = Field(default=..., description="""The agent (person, organization, or software) that triggered or performed the action. Can reference a Person, Organization, or SoftwareApplication entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Action']} })
    instrument: Optional[str] = Field(default=None, description="""The tool or service that executed the action (e.g., 'cr8tor CLI', 'GitHub Action',  specific TRE service). Maps to schema.org Action.instrument.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Action']} })
    result: Optional[list[str]] = Field(default=[], description="""List of result items produced by the action, typically ID references to other  data or context entities created or modified by the action.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Action']} })
    error: Optional[str] = Field(default=None, description="""Error message or output if the action failed. Only present when action_status is FailedActionStatus.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Action']} })


class AssessAction(Action):
    """
    Represents an assessment action performed on a Cr8tor project, used to track validation, disclosure checks, and other evaluation activities. Inherits all properties from Action and adds an optional additional_type for sub-assessments.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/governance-model',
         'narrow_mappings': ['schemaorg:AssessAction']})

    additional_type: Optional[str] = Field(default=None, description="""Additional type classification for specialized actions, used to reference sub-actions  or specific assessment types (e.g., 'disclosure check' for AssessAction).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssessAction']} })
    action_type: Literal["AssessAction"] = Field(default="AssessAction", description="""The specific type of action being performed (e.g., CreateAction, AssessAction).""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Action']} })
    id: str = Field(default=..., description="""Unique identifier for the action, typically formatted as '{command_type}-{project_id}'.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project', 'Action', 'User']} })
    name: str = Field(default=..., description="""Human-readable name describing the action (e.g., \"CREATE Data Project Action\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project',
                       'Action',
                       'Source',
                       'Dataset',
                       'Table',
                       'Column',
                       'Resource',
                       'Environment',
                       'KeycloakClientConfig',
                       'SecretRef',
                       'ProtocolMapper',
                       'EnvironmentVariable']} })
    start_time: datetime  = Field(default=..., description="""The date and time when the action started execution.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project', 'Action']} })
    end_time: datetime  = Field(default=..., description="""The date and time when the action completed or failed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Action']} })
    action_status: ActionStatusType = Field(default=..., description="""The current status of the action, indicating whether it's active, completed, failed, or potential. Formatted based on schema.org ActionStatus and Provenance Crate Profile specification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Action']} })
    agent: str = Field(default=..., description="""The agent (person, organization, or software) that triggered or performed the action. Can reference a Person, Organization, or SoftwareApplication entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Action']} })
    instrument: Optional[str] = Field(default=None, description="""The tool or service that executed the action (e.g., 'cr8tor CLI', 'GitHub Action',  specific TRE service). Maps to schema.org Action.instrument.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Action']} })
    result: Optional[list[str]] = Field(default=[], description="""List of result items produced by the action, typically ID references to other  data or context entities created or modified by the action.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Action']} })
    error: Optional[str] = Field(default=None, description="""Error message or output if the action failed. Only present when action_status is FailedActionStatus.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Action']} })


class User(ConfiguredBaseModel):
    """
    Models an individual user associated with a Cr8tor project, capturing their identity, contact information, organizational affiliation, group memberships, and access lifecycle. This class represents the state of a user's relationship to the project and their access rights.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/governance-model',
         'narrow_mappings': ['schemaorg:Person', 'schemaorg:Organization', 'scim:User']})

    id: str = Field(default=..., description="""A globally unique identifier for the user, ensuring unambiguous reference within and across systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project', 'Action', 'User'], 'slot_uri': 'schemaorg:identifier'} })
    username: Optional[str] = Field(default=None, description="""The user's unique login or account name, used for authentication and identification within the project.""", json_schema_extra = { "linkml_meta": {'domain_of': ['User'], 'slot_uri': 'schemaorg:identifier'} })
    given_name: Optional[str] = Field(default=None, description="""The user's first or given name, representing their personal identity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['User'], 'slot_uri': 'schemaorg:name'} })
    family_name: Optional[str] = Field(default=None, description="""The user's last or family name, used for identification and display purposes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['User']} })
    affiliation: Optional[str] = Field(default=None, description="""The name of the organization or institution with which the user is affiliated, representing their organizational context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['User']} })
    email: Optional[str] = Field(default=None, description="""The user's email address, used for communication and notifications related to the project.""", json_schema_extra = { "linkml_meta": {'domain_of': ['User']} })
    groups: Optional[list[Group]] = Field(default=[], description="""List of groups to which the user belongs within the project, representing roles, permissions, or organizational units.""", json_schema_extra = { "linkml_meta": {'domain_of': ['User']} })
    start_date: Optional[datetime ] = Field(default=None, description="""The date and time when the user's access to the project becomes active, representing the start of their membership or role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['User']} })
    expiry_date: Optional[datetime ] = Field(default=None, description="""The date and time when the user's access to the project expires, representing the end of their membership or role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['User']} })
    enabled: Optional[bool] = Field(default=True, description="""Whether the user account is enabled.""", json_schema_extra = { "linkml_meta": {'domain_of': ['User', 'Resource', 'KeycloakClientConfig'], 'ifabsent': 'true'} })
    password: Optional[str] = Field(default=None, description="""Optional initial password. If not set, the operator generates a temporary password.""", json_schema_extra = { "linkml_meta": {'domain_of': ['User']} })


class Group(ConfiguredBaseModel):
    """
    Represents a group or organizational unit within a Cr8tor project, used to organize users, assign roles, and manage permissions. This class models the state of group membership and its associated metadata.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/governance-model',
         'narrow_mappings': ['scim:Group']})

    value: Optional[str] = Field(default=None, description="""The unique identifier of the group, typically used as the group ID for referencing and access control. Read-only.""", json_schema_extra = { "linkml_meta": {'annotations': {'mutability': {'tag': 'mutability', 'value': 'readOnly'}},
         'domain_of': ['Group', 'EnvironmentVariable']} })
    ref: Optional[str] = Field(default=None, description="""The URI reference to the corresponding Group resource, enabling linkage to external or internal group definitions. Read-only.""", json_schema_extra = { "linkml_meta": {'annotations': {'mutability': {'tag': 'mutability', 'value': 'readOnly'},
                         'reference_type': {'tag': 'reference_type', 'value': 'Group'}},
         'domain_of': ['Group']} })
    display: Optional[str] = Field(default=None, description="""A human-readable display name for the group, used for UI and reporting. Read-only.""", json_schema_extra = { "linkml_meta": {'annotations': {'mutability': {'tag': 'mutability', 'value': 'readOnly'}},
         'domain_of': ['Group']} })
    type: Optional[GroupMembershipType] = Field(default=None, description="""The type of group membership, indicating how the user was assigned to the group (e.g., manual or automatic). Read-only.""", json_schema_extra = { "linkml_meta": {'annotations': {'mutability': {'tag': 'mutability', 'value': 'readOnly'}},
         'domain_of': ['Group', 'Source', 'Destination']} })


class Ingress(ConfiguredBaseModel):
    """
    Represents the data ingress process for a Cr8tor project, modeling the flow of data from sources to destinations, and the datasets involved. This class captures the state of data movement and configuration for project data pipelines.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/data-model'})

    source: Optional[Source] = Field(default=None, description="""The origin or source of data for the ingress process, representing where data is extracted from. Optional.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Ingress']} })
    destination: Destination = Field(default=..., description="""The target or endpoint where data is delivered during the ingress process, representing the state of data delivery. Required.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Ingress']} })
    datasets: Optional[list[Dataset]] = Field(default=[], description="""List of datasets involved in the ingress process, each representing a collection of data to be transferred. Optional, can include multiple datasets.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Ingress']} })


class Source(ConfiguredBaseModel):
    """
    Models a data source within a Cr8tor project, representing the origin of data to be ingested. This class defines the state and configuration of external or internal data sources.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/data-model'})

    name: Optional[str] = Field(default=None, description="""The name of the data source, used for identification and reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project',
                       'Action',
                       'Source',
                       'Dataset',
                       'Table',
                       'Column',
                       'Resource',
                       'Environment',
                       'KeycloakClientConfig',
                       'SecretRef',
                       'ProtocolMapper',
                       'EnvironmentVariable']} })
    type: Optional[str] = Field(default=None, description="""The type of data source (e.g., databricks, postgresql, mssql, filestore).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group', 'Source', 'Destination']} })
    url: Optional[str] = Field(default=None, description="""The URL or location of the data source, specifying where data can be accessed or retrieved from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Source', 'Destination', 'Resource', 'VDI']} })
    credentials: Optional[Credential] = Field(default=None, description="""The credentials required to access the data source, including authentication provider and key references.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Source']} })


class Credential(ConfiguredBaseModel):
    """
    Models authentication credentials for accessing a data source, including the provider and references to password and username keys stored in a secure credential store.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/data-model'})

    provider: str = Field(default=..., description="""The credential provider or authentication service (e.g., Azure Key Vault, AWS Secrets Manager, HashiCorp Vault).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Credential']} })
    password_key: str = Field(default=..., description="""The key or identifier used to retrieve the password from the credential provider.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Credential']} })
    username_key: str = Field(default=..., description="""The key or identifier used to retrieve the username from the credential provider.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Credential']} })


class Destination(ConfiguredBaseModel):
    """
    Models a data destination within a Cr8tor project, representing the endpoint where data is delivered or stored after ingress. This class defines the state and configuration of data targets.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/data-model'})

    type: DestinationType = Field(default=..., description="""The type of destination (e.g., filestore, postgresql), specifying the nature of the data endpoint. Required.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group', 'Source', 'Destination']} })
    url: Optional[str] = Field(default=None, description="""The URL or location of the data destination, specifying where data should be delivered. Optional.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Source', 'Destination', 'Resource', 'VDI']} })


class Dataset(ConfiguredBaseModel):
    """
    Represents a dataset to be ingested or managed within a Cr8tor project, including its metadata, schema, tables, and data locations. This class models the state and structure of data collections handled by the project.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/data-model'})

    name: str = Field(default=..., description="""The name of the dataset, used for identification and reference within the project. Required.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project',
                       'Action',
                       'Source',
                       'Dataset',
                       'Table',
                       'Column',
                       'Resource',
                       'Environment',
                       'KeycloakClientConfig',
                       'SecretRef',
                       'ProtocolMapper',
                       'EnvironmentVariable']} })
    schema_name: str = Field(default=..., description="""The name of the schema in the target database where the dataset will reside. Required.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })
    tables: Optional[list[Table]] = Field(default=[], description="""List of tables that make up the dataset, each representing a structured collection of columns and data. Optional, can include multiple tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })
    locations: Optional[list[Any]] = Field(default=[], description="""List of data locations or URIs where the dataset is stored or accessed during the TRE ingestion workflow. Accepts arbitrary data structures including dictionaries. Optional, can include multiple locations.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })


class Table(ConfiguredBaseModel):
    """
    Models a table within a dataset, representing a structured collection of data organized into columns. This class defines the state and schema of tabular data in the project.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/data-model'})

    name: str = Field(default=..., description="""The name of the table, used for identification within the dataset. Required.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project',
                       'Action',
                       'Source',
                       'Dataset',
                       'Table',
                       'Column',
                       'Resource',
                       'Environment',
                       'KeycloakClientConfig',
                       'SecretRef',
                       'ProtocolMapper',
                       'EnvironmentVariable']} })
    columns: list[Column] = Field(default=..., description="""List of columns that define the schema of the table, each representing a data field. Required, can include multiple columns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Table']} })


class Column(ConfiguredBaseModel):
    """
    Models a column within a table, representing a single field of data with a specific datatype. This class defines the state and schema of individual data fields in tabular structures.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/data-model'})

    name: str = Field(default=..., description="""The name of the column, used for identification within the table. Required.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project',
                       'Action',
                       'Source',
                       'Dataset',
                       'Table',
                       'Column',
                       'Resource',
                       'Environment',
                       'KeycloakClientConfig',
                       'SecretRef',
                       'ProtocolMapper',
                       'EnvironmentVariable']} })
    datatype: str = Field(default=..., description="""The datatype of the column, specifying the kind of data stored (e.g., string, integer). Required.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Column']} })


class Deployment(ConfiguredBaseModel):
    """
    Models the deployment configuration for a Cr8tor project, specifying the K8TRE resources and applications to be provisioned, as well as the target environment. This class represents the state and desired configuration for project deployments.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/deployment-model'})

    resources: Optional[list[Union[Resource,Jupyter,Keycloak,VDI,RStudio,Gitea]]] = Field(default=[], description="""List of resource names or identifiers representing the K8TRE applications or services to be deployed as part of the project. Can include multiple resources.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Deployment', 'ProjectSpec', 'VdiScheduling']} })
    environment: Optional[Environment] = Field(default=None, description="""The environment configuration for the deployment, specifying the target trusted research environment (TRE) and its properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Deployment']} })


class Resource(ConfiguredBaseModel):
    """
    Abstract base class for K8TRE resources (such as applications or services) that can be deployed through a Cr8tor project. This class defines the state and configuration of deployable resources.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/deployment-model'})

    resource_type: Literal["Resource"] = Field(default="Resource", description="""The type of resource (e.g., Jupyter, Keycloak, VDI).""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Resource']} })
    name: str = Field(default=..., description="""The requested name of the resource, used for identification and management within the deployment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project',
                       'Action',
                       'Source',
                       'Dataset',
                       'Table',
                       'Column',
                       'Resource',
                       'Environment',
                       'KeycloakClientConfig',
                       'SecretRef',
                       'ProtocolMapper',
                       'EnvironmentVariable']} })
    url: str = Field(default=..., description="""The URL endpoint for accessing the application or resource after deployment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Source', 'Destination', 'Resource', 'VDI']} })
    enabled: bool = Field(default=..., description="""Boolean flag indicating whether the application or resource is enabled and available for use.""", json_schema_extra = { "linkml_meta": {'domain_of': ['User', 'Resource', 'KeycloakClientConfig']} })


class Jupyter(Resource):
    """
    Specialized resource configuration for deploying Jupyter workspaces within a Cr8tor project. This class extends Resource to include Jupyter-specific settings and state.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/deployment-model'})

    auth: Optional[str] = Field(default=None, description="""The type or method of authentication required to access the Jupyter workspace (e.g., OAuth, SSO).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Jupyter']} })
    profiles: Optional[list[ProfileConfig]] = Field(default=[], description="""JupyterHub workspace profiles for this deployment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Jupyter']} })
    storage: Optional[ResourceStorage] = Field(default=None, description="""Storage configuration for notebook workspaces.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Jupyter', 'VDI']} })
    resource_type: Literal["Jupyter"] = Field(default="Jupyter", description="""The type of resource (e.g., Jupyter, Keycloak, VDI).""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Resource']} })
    name: str = Field(default=..., description="""The requested name of the resource, used for identification and management within the deployment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project',
                       'Action',
                       'Source',
                       'Dataset',
                       'Table',
                       'Column',
                       'Resource',
                       'Environment',
                       'KeycloakClientConfig',
                       'SecretRef',
                       'ProtocolMapper',
                       'EnvironmentVariable']} })
    url: str = Field(default=..., description="""The URL endpoint for accessing the application or resource after deployment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Source', 'Destination', 'Resource', 'VDI']} })
    enabled: bool = Field(default=..., description="""Boolean flag indicating whether the application or resource is enabled and available for use.""", json_schema_extra = { "linkml_meta": {'domain_of': ['User', 'Resource', 'KeycloakClientConfig']} })


class Keycloak(Resource):
    """
    Specialized resource configuration for deploying Keycloak identity and access management services within a Cr8tor project. This class extends Resource to include Keycloak-specific settings and state.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/deployment-model'})

    realm: Optional[str] = Field(default=None, description="""The Keycloak realm name for this project deployment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Keycloak']} })
    clients: Optional[list[KeycloakClientConfig]] = Field(default=[], description="""OIDC clients to be managed in this Keycloak deployment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Keycloak']} })
    resource_type: Literal["Keycloak"] = Field(default="Keycloak", description="""The type of resource (e.g., Jupyter, Keycloak, VDI).""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Resource']} })
    name: str = Field(default=..., description="""The requested name of the resource, used for identification and management within the deployment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project',
                       'Action',
                       'Source',
                       'Dataset',
                       'Table',
                       'Column',
                       'Resource',
                       'Environment',
                       'KeycloakClientConfig',
                       'SecretRef',
                       'ProtocolMapper',
                       'EnvironmentVariable']} })
    url: str = Field(default=..., description="""The URL endpoint for accessing the application or resource after deployment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Source', 'Destination', 'Resource', 'VDI']} })
    enabled: bool = Field(default=..., description="""Boolean flag indicating whether the application or resource is enabled and available for use.""", json_schema_extra = { "linkml_meta": {'domain_of': ['User', 'Resource', 'KeycloakClientConfig']} })


class VDI(Resource):
    """
    Virtual Desktop Infrastructure resource for cr8tor project. The operator creates a pod and Service for each VDI instance, and manages user access and lifecycle. This class extends Resource to include VDI-specific configuration.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/deployment-model'})

    image: Optional[str] = Field(default="ghcr.io/karectl/vdi-mate:v1.0.0-light", description="""Container image for the VDI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VDI', 'KubespawnerOverride'],
         'ifabsent': 'string(ghcr.io/karectl/vdi-mate:v1.0.0-light)'} })
    user: Optional[str] = Field(default=None, description="""Username for the VDI session.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VDI']} })
    project: Optional[str] = Field(default=None, description="""Project this VDI belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Governance', 'VDI']} })
    url: Optional[str] = Field(default=None, description="""Not used for VDI; VDI access is managed via the operator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Source', 'Destination', 'Resource', 'VDI']} })
    connection: Optional[ConnectionType] = Field(default=ConnectionType.rdp, description="""Connection protocol""", json_schema_extra = { "linkml_meta": {'domain_of': ['VDI'], 'ifabsent': 'string(rdp)'} })
    env: Optional[list[EnvironmentVariable]] = Field(default=[], description="""Environment variables for the VDI container.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VDI', 'KubespawnerOverride']} })
    scheduling: Optional[VdiScheduling] = Field(default=None, description="""Resource scheduling configuration for VDI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VDI']} })
    storage: Optional[ResourceStorage] = Field(default=None, description="""Storage configuration for VDI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Jupyter', 'VDI']} })
    resource_type: Literal["VDI"] = Field(default="VDI", description="""The type of resource (e.g., Jupyter, Keycloak, VDI).""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Resource']} })
    name: str = Field(default=..., description="""The requested name of the resource, used for identification and management within the deployment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project',
                       'Action',
                       'Source',
                       'Dataset',
                       'Table',
                       'Column',
                       'Resource',
                       'Environment',
                       'KeycloakClientConfig',
                       'SecretRef',
                       'ProtocolMapper',
                       'EnvironmentVariable']} })
    enabled: bool = Field(default=..., description="""Boolean flag indicating whether the application or resource is enabled and available for use.""", json_schema_extra = { "linkml_meta": {'domain_of': ['User', 'Resource', 'KeycloakClientConfig']} })


class RStudio(Resource):
    """
    RStudio workspace resource for cr8tor project.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/deployment-model'})

    resource_type: Literal["RStudio"] = Field(default="RStudio", description="""The type of resource (e.g., Jupyter, Keycloak, VDI).""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Resource']} })
    name: str = Field(default=..., description="""The requested name of the resource, used for identification and management within the deployment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project',
                       'Action',
                       'Source',
                       'Dataset',
                       'Table',
                       'Column',
                       'Resource',
                       'Environment',
                       'KeycloakClientConfig',
                       'SecretRef',
                       'ProtocolMapper',
                       'EnvironmentVariable']} })
    url: str = Field(default=..., description="""The URL endpoint for accessing the application or resource after deployment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Source', 'Destination', 'Resource', 'VDI']} })
    enabled: bool = Field(default=..., description="""Boolean flag indicating whether the application or resource is enabled and available for use.""", json_schema_extra = { "linkml_meta": {'domain_of': ['User', 'Resource', 'KeycloakClientConfig']} })


class Gitea(Resource):
    """
    Gitea git repository resource for cr8tor project.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/deployment-model'})

    resource_type: Literal["Gitea"] = Field(default="Gitea", description="""The type of resource (e.g., Jupyter, Keycloak, VDI).""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Resource']} })
    name: str = Field(default=..., description="""The requested name of the resource, used for identification and management within the deployment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project',
                       'Action',
                       'Source',
                       'Dataset',
                       'Table',
                       'Column',
                       'Resource',
                       'Environment',
                       'KeycloakClientConfig',
                       'SecretRef',
                       'ProtocolMapper',
                       'EnvironmentVariable']} })
    url: str = Field(default=..., description="""The URL endpoint for accessing the application or resource after deployment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Source', 'Destination', 'Resource', 'VDI']} })
    enabled: bool = Field(default=..., description="""Boolean flag indicating whether the application or resource is enabled and available for use.""", json_schema_extra = { "linkml_meta": {'domain_of': ['User', 'Resource', 'KeycloakClientConfig']} })


class Environment(ConfiguredBaseModel):
    """
    Models the configuration of the target trusted research environment (TRE) for a Cr8tor project deployment, including environment-specific settings and metadata.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/deployment-model'})

    name: Optional[str] = Field(default=None, description="""The name of the environment or TRE where the project will be deployed, used for identification and management.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project',
                       'Action',
                       'Source',
                       'Dataset',
                       'Table',
                       'Column',
                       'Resource',
                       'Environment',
                       'KeycloakClientConfig',
                       'SecretRef',
                       'ProtocolMapper',
                       'EnvironmentVariable']} })


class ProjectSpec(ConfiguredBaseModel):
    """
    Operator project specification to define the resources for a research project namespace.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/deployment-model'})

    description: str = Field(default=..., description="""Project description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project', 'ProjectSpec', 'GroupSpec', 'ProfileConfig']} })
    resources: Optional[list[Union[Resource,Jupyter,Keycloak,VDI,RStudio,Gitea]]] = Field(default=[], description="""Resources (applications/services) available in this project.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Deployment', 'ProjectSpec', 'VdiScheduling']} })


class GroupSpec(ConfiguredBaseModel):
    """
    Operator group specification for managing keycloak groups and setting up workspace storage for group members.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/deployment-model'})

    description: Optional[str] = Field(default=None, description="""Descrption of the group and its purpose.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project', 'ProjectSpec', 'GroupSpec', 'ProfileConfig']} })
    members: Optional[list[str]] = Field(default=[], description="""Usernames of group members.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GroupSpec']} })
    projects: Optional[list[str]] = Field(default=[], description="""Project names this group grants access to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GroupSpec']} })
    subgroups: Optional[list[str]] = Field(default=[], description="""Child group names.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GroupSpec']} })


class KeycloakClientConfig(ConfiguredBaseModel):
    """
    Configuration for a Keycloak OIDC client. The operator creates and manages these in Keycloak for project services.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/deployment-model'})

    client_id: str = Field(default=..., description="""Unique Keycloak client identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeycloakClientConfig']} })
    name: Optional[str] = Field(default=None, description="""client name shown in Keycloak admin console.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project',
                       'Action',
                       'Source',
                       'Dataset',
                       'Table',
                       'Column',
                       'Resource',
                       'Environment',
                       'KeycloakClientConfig',
                       'SecretRef',
                       'ProtocolMapper',
                       'EnvironmentVariable']} })
    secret: Optional[str] = Field(default=None, description="""Client secret.""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeycloakClientConfig']} })
    secret_ref: Optional[SecretRef] = Field(default=None, description="""Reference to a k8s Secret containing the client secret.""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeycloakClientConfig']} })
    enabled: Optional[bool] = Field(default=True, description="""Whether the client is enabled.""", json_schema_extra = { "linkml_meta": {'domain_of': ['User', 'Resource', 'KeycloakClientConfig'], 'ifabsent': 'true'} })
    public_client: Optional[bool] = Field(default=False, description="""Whether this is a public client.""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeycloakClientConfig'], 'ifabsent': 'false'} })
    redirect_uris: Optional[list[str]] = Field(default=[], description="""Valid redirect URIs after authentication.""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeycloakClientConfig']} })
    web_origins: Optional[list[str]] = Field(default=[], description="""Allowed web origins for CORS.""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeycloakClientConfig']} })
    protocol: Optional[str] = Field(default="openid-connect", description="""Authentication protocol.""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeycloakClientConfig'], 'ifabsent': 'string(openid-connect)'} })
    default_client_scopes: Optional[list[str]] = Field(default=[], description="""Default client scopes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeycloakClientConfig']} })
    optional_client_scopes: Optional[list[str]] = Field(default=[], description="""Optional client scopes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeycloakClientConfig']} })
    protocol_mappers: Optional[list[ProtocolMapper]] = Field(default=[], description="""OIDC protocol mappers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeycloakClientConfig']} })


class SecretRef(ConfiguredBaseModel):
    """
    Reference to a k8s Secret.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/deployment-model'})

    name: str = Field(default=..., description="""Secret name in the same namespace.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project',
                       'Action',
                       'Source',
                       'Dataset',
                       'Table',
                       'Column',
                       'Resource',
                       'Environment',
                       'KeycloakClientConfig',
                       'SecretRef',
                       'ProtocolMapper',
                       'EnvironmentVariable']} })
    key: Optional[str] = Field(default="client-secret", description="""Key within the Secret.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SecretRef'], 'ifabsent': 'string(client-secret)'} })


class ProtocolMapper(ConfiguredBaseModel):
    """
    Keycloak OIDC protocol mapper.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/deployment-model'})

    name: str = Field(default=..., description="""Mapper name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project',
                       'Action',
                       'Source',
                       'Dataset',
                       'Table',
                       'Column',
                       'Resource',
                       'Environment',
                       'KeycloakClientConfig',
                       'SecretRef',
                       'ProtocolMapper',
                       'EnvironmentVariable']} })
    protocol_mapper: str = Field(default=..., description="""Mapper type or class.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProtocolMapper']} })
    consent_required: Optional[bool] = Field(default=False, json_schema_extra = { "linkml_meta": {'domain_of': ['ProtocolMapper'], 'ifabsent': 'false'} })
    config: Optional[str] = Field(default=None, description="""Mapper configuration as JSON string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProtocolMapper']} })


class ProfileConfig(ConfiguredBaseModel):
    """
    JupyterHub workspace profile to select different workspace environments.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/deployment-model'})

    display_name: str = Field(default=..., description="""Profile name shown in jupyterhub spawner.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProfileConfig']} })
    description: Optional[str] = Field(default=None, description="""Profile description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project', 'ProjectSpec', 'GroupSpec', 'ProfileConfig']} })
    slug: str = Field(default=..., description="""URL-safe profile identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProfileConfig']} })
    kubespawner_override: Optional[KubespawnerOverride] = Field(default=None, description="""KubeSpawner overrides for this profile.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProfileConfig']} })


class KubespawnerOverride(ConfiguredBaseModel):
    """
    KubeSpawner override settings for a jupyterhub profile.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/deployment-model'})

    image: Optional[str] = Field(default=None, description="""Container image for the workspace.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VDI', 'KubespawnerOverride']} })
    env: Optional[list[EnvironmentVariable]] = Field(default=[], description="""Environment variables for the workspace.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VDI', 'KubespawnerOverride']} })


class EnvironmentVariable(ConfiguredBaseModel):
    """
    A name-value environment variable pair.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/deployment-model'})

    name: str = Field(default=..., description="""Variable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Project',
                       'Action',
                       'Source',
                       'Dataset',
                       'Table',
                       'Column',
                       'Resource',
                       'Environment',
                       'KeycloakClientConfig',
                       'SecretRef',
                       'ProtocolMapper',
                       'EnvironmentVariable']} })
    value: str = Field(default=..., description="""Variable value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group', 'EnvironmentVariable']} })


class VdiSchedulingResources(ConfiguredBaseModel):
    """
    CPU and memory resource requests/limits for a VDI pod.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/deployment-model'})

    requests_cpu: Optional[str] = Field(default=None, description="""CPU request""", json_schema_extra = { "linkml_meta": {'domain_of': ['VdiSchedulingResources']} })
    requests_memory: Optional[str] = Field(default=None, description="""Memory requests""", json_schema_extra = { "linkml_meta": {'domain_of': ['VdiSchedulingResources']} })
    limits_cpu: Optional[str] = Field(default=None, description="""CPU limit""", json_schema_extra = { "linkml_meta": {'domain_of': ['VdiSchedulingResources']} })
    limits_memory: Optional[str] = Field(default=None, description="""Memory limit""", json_schema_extra = { "linkml_meta": {'domain_of': ['VdiSchedulingResources']} })


class VdiScheduling(ConfiguredBaseModel):
    """
    Scheduling configuration for a VDI.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/deployment-model'})

    resources: Optional[VdiSchedulingResources] = Field(default=None, description="""CPU and memory resource requests/limits.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Deployment', 'ProjectSpec', 'VdiScheduling']} })


class ResourceStorage(ConfiguredBaseModel):
    """
    Per-resource storage configuration for workspace persistent volumes.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/deployment-model'})

    default_vdi_size: Optional[str] = Field(default=None, description="""Default PVC size for VDI workspaces.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResourceStorage']} })
    default_notebook_size: Optional[str] = Field(default=None, description="""Default PVC size for notebook workspaces.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResourceStorage']} })
    persist: Optional[bool] = Field(default=None, description="""Whether workspace storage should persist across sessions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResourceStorage']} })


class Cr8tor(ConfiguredBaseModel):
    """
    The root container class for the Cr8tor metamodel, aggregating all project data including governance, data ingress, and deployment configuration. This class represents the complete state of a Cr8tor project instance.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/karectl-crates/cr8tor-metamodel',
         'tree_root': True})

    governance: Governance = Field(default=..., description="""The governance configuration for the project, managing user access, membership, and project metadata. Required.""", json_schema_extra = { "linkml_meta": {'domain_of': ['cr8tor']} })
    ingress: Ingress = Field(default=..., description="""The data ingress configuration for the project, specifying data sources, destinations, and datasets involved in data movement. Required.""", json_schema_extra = { "linkml_meta": {'domain_of': ['cr8tor']} })
    deployment: Deployment = Field(default=..., description="""The deployment configuration for the project, detailing the resources and environment to be provisioned. Required.""", json_schema_extra = { "linkml_meta": {'domain_of': ['cr8tor']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Governance.model_rebuild()
Project.model_rebuild()
Action.model_rebuild()
CreateAction.model_rebuild()
AssessAction.model_rebuild()
User.model_rebuild()
Group.model_rebuild()
Ingress.model_rebuild()
Source.model_rebuild()
Credential.model_rebuild()
Destination.model_rebuild()
Dataset.model_rebuild()
Table.model_rebuild()
Column.model_rebuild()
Deployment.model_rebuild()
Resource.model_rebuild()
Jupyter.model_rebuild()
Keycloak.model_rebuild()
VDI.model_rebuild()
RStudio.model_rebuild()
Gitea.model_rebuild()
Environment.model_rebuild()
ProjectSpec.model_rebuild()
GroupSpec.model_rebuild()
KeycloakClientConfig.model_rebuild()
SecretRef.model_rebuild()
ProtocolMapper.model_rebuild()
ProfileConfig.model_rebuild()
KubespawnerOverride.model_rebuild()
EnvironmentVariable.model_rebuild()
VdiSchedulingResources.model_rebuild()
VdiScheduling.model_rebuild()
ResourceStorage.model_rebuild()
Cr8tor.model_rebuild()
