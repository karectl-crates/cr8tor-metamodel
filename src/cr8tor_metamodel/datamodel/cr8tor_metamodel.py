# Auto generated from cr8tor_metamodel.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-08-10T16:15:50
# Schema: cr8tor-metamodel
#
# id: https://w3id.org/karectl-crates/cr8tor-metamodel
# description: Cr8tor metamodel project
# license: MIT

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Date, Datetime, Integer, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URI, URIorCURIE, XSDDate, XSDDateTime

metamodel_version = "1.7.0"
version = None

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
CR8TOR_METAMODEL = CurieNamespace('cr8tor_metamodel', 'https://w3id.org/karectl-crates/cr8tor-metamodel/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMAORG = CurieNamespace('schemaorg', 'http://schema.org/')
SCIM = CurieNamespace('scim', 'urn:ietf:params:scim:schemas:core:2.0')
DEFAULT_ = CR8TOR_METAMODEL


# Types

# Class references
class ActionId(extended_str):
    pass


class CreateActionId(ActionId):
    pass


class AssessActionId(ActionId):
    pass


@dataclass(repr=False)
class Cr8tor(YAMLRoot):
    """
    The root container class for the Cr8tor metamodel, aggregating all project data including governance, data
    ingress, and deployment configuration. This class represents the complete state of a Cr8tor project instance.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["Cr8tor"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:Cr8tor"
    class_name: ClassVar[str] = "cr8tor"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.Cr8tor

    governance: Union[dict, "Governance"] = None
    ingress: Union[dict, "Ingress"] = None
    deployment: Union[dict, "Deployment"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.governance):
            self.MissingRequiredField("governance")
        if not isinstance(self.governance, Governance):
            self.governance = Governance(**as_dict(self.governance))

        if self._is_empty(self.ingress):
            self.MissingRequiredField("ingress")
        if not isinstance(self.ingress, Ingress):
            self.ingress = Ingress(**as_dict(self.ingress))

        if self._is_empty(self.deployment):
            self.MissingRequiredField("deployment")
        if not isinstance(self.deployment, Deployment):
            self.deployment = Deployment(**as_dict(self.deployment))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Governance(YAMLRoot):
    """
    Represents the governance structure of a Cr8tor project, encapsulating user access control, project membership,
    and mandatory project metadata. This class manages the relationships between users and the project, ensuring
    proper access and compliance with governance requirements.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["Governance"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:Governance"
    class_name: ClassVar[str] = "Governance"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.Governance

    project: Union[dict, "Project"] = None
    users: Union[Union[dict, "User"], list[Union[dict, "User"]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.project):
            self.MissingRequiredField("project")
        if not isinstance(self.project, Project):
            self.project = Project(**as_dict(self.project))

        if self._is_empty(self.users):
            self.MissingRequiredField("users")
        if not isinstance(self.users, list):
            self.users = [self.users] if self.users is not None else []
        self.users = [v if isinstance(v, User) else User(**as_dict(v)) for v in self.users]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Project(YAMLRoot):
    """
    Defines the core state and identifying properties of a Cr8tor project, including its name, description, and
    reference information. This class models the essential metadata required to uniquely identify and describe a
    project within the Cr8tor ecosystem.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["Project"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:Project"
    class_name: ClassVar[str] = "Project"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.Project

    name: str = None
    description: str = None
    id: Optional[str] = None
    reference: Optional[str] = None
    start_time: Optional[str] = None
    actions: Optional[Union[dict[Union[str, ActionId], Union[dict, "Action"]], list[Union[dict, "Action"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.reference is not None and not isinstance(self.reference, str):
            self.reference = str(self.reference)

        if self.start_time is not None and not isinstance(self.start_time, str):
            self.start_time = str(self.start_time)

        self._normalize_inlined_as_list(slot_name="actions", slot_type=Action, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Action(YAMLRoot):
    """
    Represents an action or activity performed on a Cr8tor project, tracking the lifecycle and state changes of the
    project. Based on schema.org Action and the Provenance Crate Profile specification. Actions track operations like
    create, assess, validate, etc.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["Action"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:Action"
    class_name: ClassVar[str] = "Action"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.Action

    id: Union[str, ActionId] = None
    action_type: str = None
    name: str = None
    start_time: Union[str, XSDDateTime] = None
    end_time: Union[str, XSDDateTime] = None
    action_status: Union[str, "ActionStatusType"] = None
    agent: str = None
    instrument: Optional[str] = None
    result: Optional[Union[str, list[str]]] = empty_list()
    error: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ActionId):
            self.id = ActionId(self.id)

        if self._is_empty(self.action_type):
            self.MissingRequiredField("action_type")
        self.action_type = str(self.class_name)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.start_time):
            self.MissingRequiredField("start_time")
        if not isinstance(self.start_time, XSDDateTime):
            self.start_time = XSDDateTime(self.start_time)

        if self._is_empty(self.end_time):
            self.MissingRequiredField("end_time")
        if not isinstance(self.end_time, XSDDateTime):
            self.end_time = XSDDateTime(self.end_time)

        if self._is_empty(self.action_status):
            self.MissingRequiredField("action_status")
        if not isinstance(self.action_status, ActionStatusType):
            self.action_status = ActionStatusType(self.action_status)

        if self._is_empty(self.agent):
            self.MissingRequiredField("agent")
        if not isinstance(self.agent, str):
            self.agent = str(self.agent)

        if self.instrument is not None and not isinstance(self.instrument, str):
            self.instrument = str(self.instrument)

        if not isinstance(self.result, list):
            self.result = [self.result] if self.result is not None else []
        self.result = [v if isinstance(v, str) else str(v) for v in self.result]

        if self.error is not None and not isinstance(self.error, str):
            self.error = str(self.error)

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "action_type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class CreateAction(Action):
    """
    Represents a create action performed on a Cr8tor project, typically used to track project initialization and
    creation events. Inherits all properties from Action.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["CreateAction"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:CreateAction"
    class_name: ClassVar[str] = "CreateAction"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.CreateAction

    id: Union[str, CreateActionId] = None
    action_type: str = None
    name: str = None
    start_time: Union[str, XSDDateTime] = None
    end_time: Union[str, XSDDateTime] = None
    action_status: Union[str, "ActionStatusType"] = None
    agent: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CreateActionId):
            self.id = CreateActionId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.action_type):
            self.MissingRequiredField("action_type")
        self.action_type = str(self.class_name)


@dataclass(repr=False)
class AssessAction(Action):
    """
    Represents an assessment action performed on a Cr8tor project, used to track validation, disclosure checks, and
    other evaluation activities. Inherits all properties from Action and adds an optional additional_type for
    sub-assessments.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["AssessAction"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:AssessAction"
    class_name: ClassVar[str] = "AssessAction"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.AssessAction

    id: Union[str, AssessActionId] = None
    action_type: str = None
    name: str = None
    start_time: Union[str, XSDDateTime] = None
    end_time: Union[str, XSDDateTime] = None
    action_status: Union[str, "ActionStatusType"] = None
    agent: str = None
    additional_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AssessActionId):
            self.id = AssessActionId(self.id)

        if self.additional_type is not None and not isinstance(self.additional_type, str):
            self.additional_type = str(self.additional_type)

        super().__post_init__(**kwargs)
        if self._is_empty(self.action_type):
            self.MissingRequiredField("action_type")
        self.action_type = str(self.class_name)


@dataclass(repr=False)
class User(YAMLRoot):
    """
    Models an individual user associated with a Cr8tor project, capturing their identity, contact information,
    organizational affiliation, group memberships, and access lifecycle. This class represents the state of a user's
    relationship to the project and their access rights.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["User"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:User"
    class_name: ClassVar[str] = "User"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.User

    username: Union[str, URIorCURIE] = None
    given_name: str = None
    family_name: str = None
    affiliation: str = None
    email: str = None
    id: Optional[str] = None
    groups: Optional[Union[Union[dict, "Group"], list[Union[dict, "Group"]]]] = empty_list()
    start_date: Optional[Union[str, XSDDate]] = None
    expiry_date: Optional[Union[str, XSDDate]] = None
    enabled: Optional[Union[bool, Bool]] = True
    password: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.username):
            self.MissingRequiredField("username")
        if not isinstance(self.username, URIorCURIE):
            self.username = URIorCURIE(self.username)

        if self._is_empty(self.given_name):
            self.MissingRequiredField("given_name")
        if not isinstance(self.given_name, str):
            self.given_name = str(self.given_name)

        if self._is_empty(self.family_name):
            self.MissingRequiredField("family_name")
        if not isinstance(self.family_name, str):
            self.family_name = str(self.family_name)

        if self._is_empty(self.affiliation):
            self.MissingRequiredField("affiliation")
        if not isinstance(self.affiliation, str):
            self.affiliation = str(self.affiliation)

        if self._is_empty(self.email):
            self.MissingRequiredField("email")
        if not isinstance(self.email, str):
            self.email = str(self.email)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if not isinstance(self.groups, list):
            self.groups = [self.groups] if self.groups is not None else []
        self.groups = [v if isinstance(v, Group) else Group(**as_dict(v)) for v in self.groups]

        if self.start_date is not None and not isinstance(self.start_date, XSDDate):
            self.start_date = XSDDate(self.start_date)

        if self.expiry_date is not None and not isinstance(self.expiry_date, XSDDate):
            self.expiry_date = XSDDate(self.expiry_date)

        if self.enabled is not None and not isinstance(self.enabled, Bool):
            self.enabled = Bool(self.enabled)

        if self.password is not None and not isinstance(self.password, str):
            self.password = str(self.password)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Group(YAMLRoot):
    """
    Represents a group or organizational unit within a Cr8tor project, used to organize users, assign roles, and
    manage permissions. This class models the state of group membership and its associated metadata.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["Group"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:Group"
    class_name: ClassVar[str] = "Group"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.Group

    value: Optional[str] = None
    ref: Optional[Union[str, URI]] = None
    display: Optional[str] = None
    type: Optional[Union[str, "GroupMembershipType"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        if self.ref is not None and not isinstance(self.ref, URI):
            self.ref = URI(self.ref)

        if self.display is not None and not isinstance(self.display, str):
            self.display = str(self.display)

        if self.type is not None and not isinstance(self.type, GroupMembershipType):
            self.type = GroupMembershipType(self.type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Ingress(YAMLRoot):
    """
    Represents the data ingress process for a Cr8tor project, modeling the flow of data from sources to destinations,
    and the datasets involved. This class captures the state of data movement and configuration for project data
    pipelines.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["Ingress"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:Ingress"
    class_name: ClassVar[str] = "Ingress"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.Ingress

    source: Union[dict, "Source"] = None
    destination: Union[dict, "Destination"] = None
    datasets: Optional[Union[Union[dict, "Dataset"], list[Union[dict, "Dataset"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, Source):
            self.source = Source(**as_dict(self.source))

        if self._is_empty(self.destination):
            self.MissingRequiredField("destination")
        if not isinstance(self.destination, Destination):
            self.destination = Destination(**as_dict(self.destination))

        if not isinstance(self.datasets, list):
            self.datasets = [self.datasets] if self.datasets is not None else []
        self.datasets = [v if isinstance(v, Dataset) else Dataset(**as_dict(v)) for v in self.datasets]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Source(YAMLRoot):
    """
    Models a data source within a Cr8tor project, representing the origin of data to be ingested. This class defines
    the state and configuration of external or internal data sources.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["Source"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:Source"
    class_name: ClassVar[str] = "Source"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.Source

    name: str = None
    type: Union[str, "SourceType"] = None
    url: str = None
    credentials: Union[dict, "Credential"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, SourceType):
            self.type = SourceType(self.type)

        if self._is_empty(self.url):
            self.MissingRequiredField("url")
        if not isinstance(self.url, str):
            self.url = str(self.url)

        if self._is_empty(self.credentials):
            self.MissingRequiredField("credentials")
        if not isinstance(self.credentials, Credential):
            self.credentials = Credential(**as_dict(self.credentials))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Credential(YAMLRoot):
    """
    Models authentication credentials for accessing a data source, including the provider and references to password
    and username keys stored in a secure credential store.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["Credential"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:Credential"
    class_name: ClassVar[str] = "Credential"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.Credential

    provider: str = None
    password_key: str = None
    username_key: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.provider):
            self.MissingRequiredField("provider")
        if not isinstance(self.provider, str):
            self.provider = str(self.provider)

        if self._is_empty(self.password_key):
            self.MissingRequiredField("password_key")
        if not isinstance(self.password_key, str):
            self.password_key = str(self.password_key)

        if self._is_empty(self.username_key):
            self.MissingRequiredField("username_key")
        if not isinstance(self.username_key, str):
            self.username_key = str(self.username_key)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Destination(YAMLRoot):
    """
    Models a data destination within a Cr8tor project, representing the endpoint where data is delivered or stored
    after ingress. This class defines the state and configuration of data targets.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["Destination"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:Destination"
    class_name: ClassVar[str] = "Destination"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.Destination

    type: Union[str, "DestinationType"] = None
    url: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, DestinationType):
            self.type = DestinationType(self.type)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Dataset(YAMLRoot):
    """
    Represents a dataset to be ingested or managed within a Cr8tor project, including its metadata, schema, tables,
    and data locations. This class models the state and structure of data collections handled by the project.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["Dataset"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.Dataset

    name: str = None
    schema_name: str = None
    tables: Optional[Union[Union[dict, "Table"], list[Union[dict, "Table"]]]] = empty_list()
    locations: Optional[Union[Union[dict, "Location"], list[Union[dict, "Location"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.schema_name):
            self.MissingRequiredField("schema_name")
        if not isinstance(self.schema_name, str):
            self.schema_name = str(self.schema_name)

        if not isinstance(self.tables, list):
            self.tables = [self.tables] if self.tables is not None else []
        self.tables = [v if isinstance(v, Table) else Table(**as_dict(v)) for v in self.tables]

        super().__post_init__(**kwargs)


Location = Any

@dataclass(repr=False)
class Table(YAMLRoot):
    """
    Models a table within a dataset, representing a structured collection of data organized into columns. This class
    defines the state and schema of tabular data in the project.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["Table"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:Table"
    class_name: ClassVar[str] = "Table"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.Table

    name: str = None
    columns: Union[Union[dict, "Column"], list[Union[dict, "Column"]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.columns):
            self.MissingRequiredField("columns")
        if not isinstance(self.columns, list):
            self.columns = [self.columns] if self.columns is not None else []
        self.columns = [v if isinstance(v, Column) else Column(**as_dict(v)) for v in self.columns]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Column(YAMLRoot):
    """
    Models a column within a table, representing a single field of data with a specific datatype. This class defines
    the state and schema of individual data fields in tabular structures.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["Column"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:Column"
    class_name: ClassVar[str] = "Column"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.Column

    name: str = None
    datatype: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.datatype):
            self.MissingRequiredField("datatype")
        if not isinstance(self.datatype, str):
            self.datatype = str(self.datatype)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Deployment(YAMLRoot):
    """
    Models the deployment configuration for a Cr8tor project, specifying the K8TRE resources and applications to be
    provisioned, as well as the target environment. This class represents the state and desired configuration for
    project deployments.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["Deployment"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:Deployment"
    class_name: ClassVar[str] = "Deployment"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.Deployment

    environment: Union[dict, "Environment"] = None
    resources: Optional[Union[Union[dict, "Resource"], list[Union[dict, "Resource"]]]] = empty_list()
    limit_range: Optional[Union[dict, "LimitRangeConfig"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.environment):
            self.MissingRequiredField("environment")
        if not isinstance(self.environment, Environment):
            self.environment = Environment(**as_dict(self.environment))

        if not isinstance(self.resources, list):
            self.resources = [self.resources] if self.resources is not None else []
        self.resources = [v if isinstance(v, Resource) else Resource(**as_dict(v)) for v in self.resources]

        if self.limit_range is not None and not isinstance(self.limit_range, LimitRangeConfig):
            self.limit_range = LimitRangeConfig(**as_dict(self.limit_range))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Resource(YAMLRoot):
    """
    Abstract base class for K8TRE resources (such as applications or services) that can be deployed through a Cr8tor
    project. This class defines the state and configuration of deployable resources.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["Resource"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:Resource"
    class_name: ClassVar[str] = "Resource"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.Resource

    resource_type: str = None
    name: str = None
    url: Union[str, URI] = None
    enabled: Union[bool, Bool] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.resource_type):
            self.MissingRequiredField("resource_type")
        self.resource_type = str(self.class_name)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.url):
            self.MissingRequiredField("url")
        if not isinstance(self.url, URI):
            self.url = URI(self.url)

        if self._is_empty(self.enabled):
            self.MissingRequiredField("enabled")
        if not isinstance(self.enabled, Bool):
            self.enabled = Bool(self.enabled)

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "resource_type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class Jupyter(Resource):
    """
    Specialized resource configuration for deploying Jupyter workspaces within a Cr8tor project. This class extends
    Resource to include Jupyter-specific settings and state.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["Jupyter"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:Jupyter"
    class_name: ClassVar[str] = "Jupyter"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.Jupyter

    resource_type: str = None
    name: str = None
    url: Union[str, URI] = None
    enabled: Union[bool, Bool] = None
    auth: Optional[str] = None
    profiles: Optional[Union[Union[dict, "ProfileConfig"], list[Union[dict, "ProfileConfig"]]]] = empty_list()
    storage: Optional[Union[dict, "ResourceStorage"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.auth is not None and not isinstance(self.auth, str):
            self.auth = str(self.auth)

        if not isinstance(self.profiles, list):
            self.profiles = [self.profiles] if self.profiles is not None else []
        self.profiles = [v if isinstance(v, ProfileConfig) else ProfileConfig(**as_dict(v)) for v in self.profiles]

        if self.storage is not None and not isinstance(self.storage, ResourceStorage):
            self.storage = ResourceStorage(**as_dict(self.storage))

        super().__post_init__(**kwargs)
        if self._is_empty(self.resource_type):
            self.MissingRequiredField("resource_type")
        self.resource_type = str(self.class_name)


@dataclass(repr=False)
class Keycloak(Resource):
    """
    Specialized resource configuration for deploying Keycloak identity and access management services within a Cr8tor
    project. This class extends Resource to include Keycloak-specific settings and state.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["Keycloak"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:Keycloak"
    class_name: ClassVar[str] = "Keycloak"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.Keycloak

    resource_type: str = None
    name: str = None
    url: Union[str, URI] = None
    enabled: Union[bool, Bool] = None
    realm: Optional[str] = None
    clients: Optional[Union[Union[dict, "KeycloakClientConfig"], list[Union[dict, "KeycloakClientConfig"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.realm is not None and not isinstance(self.realm, str):
            self.realm = str(self.realm)

        if not isinstance(self.clients, list):
            self.clients = [self.clients] if self.clients is not None else []
        self.clients = [v if isinstance(v, KeycloakClientConfig) else KeycloakClientConfig(**as_dict(v)) for v in self.clients]

        super().__post_init__(**kwargs)
        if self._is_empty(self.resource_type):
            self.MissingRequiredField("resource_type")
        self.resource_type = str(self.class_name)


@dataclass(repr=False)
class VDI(Resource):
    """
    Virtual Desktop Infrastructure resource for cr8tor project. The operator creates a pod and Service for each VDI
    instance, and manages user access and lifecycle. This class extends Resource to include VDI-specific
    configuration.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["VDI"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:VDI"
    class_name: ClassVar[str] = "VDI"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.VDI

    resource_type: str = None
    name: str = None
    enabled: Union[bool, Bool] = None
    image: Optional[str] = "ghcr.io/karectl/vdi-mate:v1.0.0-light"
    user: Optional[str] = None
    project: Optional[str] = None
    url: Optional[Union[str, URI]] = None
    connection: Optional[Union[str, "ConnectionType"]] = 'rdp'
    env: Optional[Union[Union[dict, "EnvironmentVariable"], list[Union[dict, "EnvironmentVariable"]]]] = empty_list()
    scheduling: Optional[Union[dict, "VdiScheduling"]] = None
    storage: Optional[Union[dict, "ResourceStorage"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.image is not None and not isinstance(self.image, str):
            self.image = str(self.image)

        if self.user is not None and not isinstance(self.user, str):
            self.user = str(self.user)

        if self.project is not None and not isinstance(self.project, str):
            self.project = str(self.project)

        if self.url is not None and not isinstance(self.url, URI):
            self.url = URI(self.url)

        if self.connection is not None and not isinstance(self.connection, ConnectionType):
            self.connection = getattr(ConnectionType, self.connection)

        if not isinstance(self.env, list):
            self.env = [self.env] if self.env is not None else []
        self.env = [v if isinstance(v, EnvironmentVariable) else EnvironmentVariable(**as_dict(v)) for v in self.env]

        if self.scheduling is not None and not isinstance(self.scheduling, VdiScheduling):
            self.scheduling = VdiScheduling(**as_dict(self.scheduling))

        if self.storage is not None and not isinstance(self.storage, ResourceStorage):
            self.storage = ResourceStorage(**as_dict(self.storage))

        super().__post_init__(**kwargs)
        if self._is_empty(self.resource_type):
            self.MissingRequiredField("resource_type")
        self.resource_type = str(self.class_name)


@dataclass(repr=False)
class RStudio(Resource):
    """
    RStudio workspace resource for cr8tor project.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["RStudio"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:RStudio"
    class_name: ClassVar[str] = "RStudio"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.RStudio

    resource_type: str = None
    name: str = None
    url: Union[str, URI] = None
    enabled: Union[bool, Bool] = None

    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        if self._is_empty(self.resource_type):
            self.MissingRequiredField("resource_type")
        self.resource_type = str(self.class_name)


@dataclass(repr=False)
class Gitea(Resource):
    """
    Gitea git repository resource for cr8tor project. The operator provisions a per-project organisation, its teams
    and an optional template repository.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["Gitea"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:Gitea"
    class_name: ClassVar[str] = "Gitea"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.Gitea

    resource_type: str = None
    name: str = None
    url: Union[str, URI] = None
    enabled: Union[bool, Bool] = None
    visibility: Optional[Union[str, "GiteaVisibility"]] = 'private'
    create_template_repo: Optional[Union[bool, Bool]] = True
    default_repo_permission: Optional[Union[str, "GiteaPermission"]] = 'read'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.visibility is not None and not isinstance(self.visibility, GiteaVisibility):
            self.visibility = getattr(GiteaVisibility, self.visibility)

        if self.create_template_repo is not None and not isinstance(self.create_template_repo, Bool):
            self.create_template_repo = Bool(self.create_template_repo)

        if self.default_repo_permission is not None and not isinstance(self.default_repo_permission, GiteaPermission):
            self.default_repo_permission = getattr(GiteaPermission, self.default_repo_permission)

        super().__post_init__(**kwargs)
        if self._is_empty(self.resource_type):
            self.MissingRequiredField("resource_type")
        self.resource_type = str(self.class_name)


@dataclass(repr=False)
class Environment(YAMLRoot):
    """
    Models the configuration of the target trusted research environment (TRE) for a Cr8tor project deployment,
    including environment-specific settings and metadata.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["Environment"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:Environment"
    class_name: ClassVar[str] = "Environment"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.Environment

    name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EgressRule(YAMLRoot):
    """
    FQDN egress rule with one or more allowed TCP ports (defaults to [443]).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["EgressRule"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:EgressRule"
    class_name: ClassVar[str] = "EgressRule"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.EgressRule

    fqdn: str = None
    ports: Optional[Union[int, list[int]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fqdn):
            self.MissingRequiredField("fqdn")
        if not isinstance(self.fqdn, str):
            self.fqdn = str(self.fqdn)

        if not isinstance(self.ports, list):
            self.ports = [self.ports] if self.ports is not None else []
        self.ports = [v if isinstance(v, int) else int(v) for v in self.ports]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProjectSpec(YAMLRoot):
    """
    Operator project specification to define the resources for a research project namespace.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["ProjectSpec"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:ProjectSpec"
    class_name: ClassVar[str] = "ProjectSpec"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.ProjectSpec

    description: str = None
    resources: Optional[Union[Union[dict, Resource], list[Union[dict, Resource]]]] = empty_list()
    resource_quota: Optional[Union[dict, "ResourceQuotaConfig"]] = None
    limit_range: Optional[Union[dict, "LimitRangeConfig"]] = None
    approved_egress_rules: Optional[Union[Union[dict, EgressRule], list[Union[dict, EgressRule]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.resources, list):
            self.resources = [self.resources] if self.resources is not None else []
        self.resources = [v if isinstance(v, Resource) else Resource(**as_dict(v)) for v in self.resources]

        if self.resource_quota is not None and not isinstance(self.resource_quota, ResourceQuotaConfig):
            self.resource_quota = ResourceQuotaConfig(**as_dict(self.resource_quota))

        if self.limit_range is not None and not isinstance(self.limit_range, LimitRangeConfig):
            self.limit_range = LimitRangeConfig(**as_dict(self.limit_range))

        if not isinstance(self.approved_egress_rules, list):
            self.approved_egress_rules = [self.approved_egress_rules] if self.approved_egress_rules is not None else []
        self.approved_egress_rules = [v if isinstance(v, EgressRule) else EgressRule(**as_dict(v)) for v in self.approved_egress_rules]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GroupSpec(YAMLRoot):
    """
    Operator group specification for managing keycloak groups and setting up workspace storage for group members.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["GroupSpec"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:GroupSpec"
    class_name: ClassVar[str] = "GroupSpec"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.GroupSpec

    description: Optional[str] = None
    members: Optional[Union[str, list[str]]] = empty_list()
    projects: Optional[Union[str, list[str]]] = empty_list()
    subgroups: Optional[Union[str, list[str]]] = empty_list()
    gitea: Optional[Union[dict, "GiteaTeamConfig"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.members, list):
            self.members = [self.members] if self.members is not None else []
        self.members = [v if isinstance(v, str) else str(v) for v in self.members]

        if not isinstance(self.projects, list):
            self.projects = [self.projects] if self.projects is not None else []
        self.projects = [v if isinstance(v, str) else str(v) for v in self.projects]

        if not isinstance(self.subgroups, list):
            self.subgroups = [self.subgroups] if self.subgroups is not None else []
        self.subgroups = [v if isinstance(v, str) else str(v) for v in self.subgroups]

        if self.gitea is not None and not isinstance(self.gitea, GiteaTeamConfig):
            self.gitea = GiteaTeamConfig(**as_dict(self.gitea))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class KeycloakClientConfig(YAMLRoot):
    """
    Configuration for a Keycloak OIDC client. The operator creates and manages these in Keycloak for project services.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["KeycloakClientConfig"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:KeycloakClientConfig"
    class_name: ClassVar[str] = "KeycloakClientConfig"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.KeycloakClientConfig

    client_id: str = None
    name: Optional[str] = None
    secret: Optional[str] = None
    secret_ref: Optional[Union[dict, "SecretRef"]] = None
    enabled: Optional[Union[bool, Bool]] = True
    public_client: Optional[Union[bool, Bool]] = False
    redirect_uris: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    web_origins: Optional[Union[str, list[str]]] = empty_list()
    protocol: Optional[str] = "openid-connect"
    default_client_scopes: Optional[Union[str, list[str]]] = empty_list()
    optional_client_scopes: Optional[Union[str, list[str]]] = empty_list()
    protocol_mappers: Optional[Union[Union[dict, "ProtocolMapper"], list[Union[dict, "ProtocolMapper"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.client_id):
            self.MissingRequiredField("client_id")
        if not isinstance(self.client_id, str):
            self.client_id = str(self.client_id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.secret is not None and not isinstance(self.secret, str):
            self.secret = str(self.secret)

        if self.secret_ref is not None and not isinstance(self.secret_ref, SecretRef):
            self.secret_ref = SecretRef(**as_dict(self.secret_ref))

        if self.enabled is not None and not isinstance(self.enabled, Bool):
            self.enabled = Bool(self.enabled)

        if self.public_client is not None and not isinstance(self.public_client, Bool):
            self.public_client = Bool(self.public_client)

        if not isinstance(self.redirect_uris, list):
            self.redirect_uris = [self.redirect_uris] if self.redirect_uris is not None else []
        self.redirect_uris = [v if isinstance(v, URI) else URI(v) for v in self.redirect_uris]

        if not isinstance(self.web_origins, list):
            self.web_origins = [self.web_origins] if self.web_origins is not None else []
        self.web_origins = [v if isinstance(v, str) else str(v) for v in self.web_origins]

        if self.protocol is not None and not isinstance(self.protocol, str):
            self.protocol = str(self.protocol)

        if not isinstance(self.default_client_scopes, list):
            self.default_client_scopes = [self.default_client_scopes] if self.default_client_scopes is not None else []
        self.default_client_scopes = [v if isinstance(v, str) else str(v) for v in self.default_client_scopes]

        if not isinstance(self.optional_client_scopes, list):
            self.optional_client_scopes = [self.optional_client_scopes] if self.optional_client_scopes is not None else []
        self.optional_client_scopes = [v if isinstance(v, str) else str(v) for v in self.optional_client_scopes]

        if not isinstance(self.protocol_mappers, list):
            self.protocol_mappers = [self.protocol_mappers] if self.protocol_mappers is not None else []
        self.protocol_mappers = [v if isinstance(v, ProtocolMapper) else ProtocolMapper(**as_dict(v)) for v in self.protocol_mappers]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SecretRef(YAMLRoot):
    """
    Reference to a k8s Secret.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["SecretRef"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:SecretRef"
    class_name: ClassVar[str] = "SecretRef"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.SecretRef

    name: str = None
    key: Optional[str] = "client-secret"

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.key is not None and not isinstance(self.key, str):
            self.key = str(self.key)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProtocolMapper(YAMLRoot):
    """
    Keycloak OIDC protocol mapper.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["ProtocolMapper"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:ProtocolMapper"
    class_name: ClassVar[str] = "ProtocolMapper"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.ProtocolMapper

    name: str = None
    protocol_mapper: str = None
    consent_required: Optional[Union[bool, Bool]] = False
    config: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.protocol_mapper):
            self.MissingRequiredField("protocol_mapper")
        if not isinstance(self.protocol_mapper, str):
            self.protocol_mapper = str(self.protocol_mapper)

        if self.consent_required is not None and not isinstance(self.consent_required, Bool):
            self.consent_required = Bool(self.consent_required)

        if self.config is not None and not isinstance(self.config, str):
            self.config = str(self.config)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProfileConfig(YAMLRoot):
    """
    JupyterHub workspace profile to select different workspace environments.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["ProfileConfig"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:ProfileConfig"
    class_name: ClassVar[str] = "ProfileConfig"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.ProfileConfig

    display_name: str = None
    slug: str = None
    description: Optional[str] = None
    kubespawner_override: Optional[Union[dict, "KubespawnerOverride"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.display_name):
            self.MissingRequiredField("display_name")
        if not isinstance(self.display_name, str):
            self.display_name = str(self.display_name)

        if self._is_empty(self.slug):
            self.MissingRequiredField("slug")
        if not isinstance(self.slug, str):
            self.slug = str(self.slug)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.kubespawner_override is not None and not isinstance(self.kubespawner_override, KubespawnerOverride):
            self.kubespawner_override = KubespawnerOverride(**as_dict(self.kubespawner_override))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class KubespawnerOverride(YAMLRoot):
    """
    KubeSpawner override settings for a jupyterhub profile.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["KubespawnerOverride"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:KubespawnerOverride"
    class_name: ClassVar[str] = "KubespawnerOverride"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.KubespawnerOverride

    image: Optional[str] = None
    env: Optional[Union[Union[dict, "EnvironmentVariable"], list[Union[dict, "EnvironmentVariable"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.image is not None and not isinstance(self.image, str):
            self.image = str(self.image)

        if not isinstance(self.env, list):
            self.env = [self.env] if self.env is not None else []
        self.env = [v if isinstance(v, EnvironmentVariable) else EnvironmentVariable(**as_dict(v)) for v in self.env]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnvironmentVariable(YAMLRoot):
    """
    A name-value environment variable pair.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["EnvironmentVariable"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:EnvironmentVariable"
    class_name: ClassVar[str] = "EnvironmentVariable"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.EnvironmentVariable

    name: str = None
    value: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GiteaTeamConfig(YAMLRoot):
    """
    Gitea team configuration for a group. The operator maintains a team of this name in each organisation belonging to
    the group's projects.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["GiteaTeamConfig"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:GiteaTeamConfig"
    class_name: ClassVar[str] = "GiteaTeamConfig"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.GiteaTeamConfig

    team_name: Optional[str] = None
    permission: Optional[Union[str, "GiteaPermission"]] = 'write'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.team_name is not None and not isinstance(self.team_name, str):
            self.team_name = str(self.team_name)

        if self.permission is not None and not isinstance(self.permission, GiteaPermission):
            self.permission = getattr(GiteaPermission, self.permission)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ResourceQuotaConfig(YAMLRoot):
    """
    Aggregate resource quota for the project namespace. No defaults are defined: a missing quota means no quota is
    applied.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["ResourceQuotaConfig"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:ResourceQuotaConfig"
    class_name: ClassVar[str] = "ResourceQuotaConfig"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.ResourceQuotaConfig

    requests_cpu: Optional[str] = None
    requests_memory: Optional[str] = None
    limits_cpu: Optional[str] = None
    limits_memory: Optional[str] = None
    pods: Optional[str] = None
    services: Optional[str] = None
    persistentvolumeclaims: Optional[str] = None
    requests_storage: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.requests_cpu is not None and not isinstance(self.requests_cpu, str):
            self.requests_cpu = str(self.requests_cpu)

        if self.requests_memory is not None and not isinstance(self.requests_memory, str):
            self.requests_memory = str(self.requests_memory)

        if self.limits_cpu is not None and not isinstance(self.limits_cpu, str):
            self.limits_cpu = str(self.limits_cpu)

        if self.limits_memory is not None and not isinstance(self.limits_memory, str):
            self.limits_memory = str(self.limits_memory)

        if self.pods is not None and not isinstance(self.pods, str):
            self.pods = str(self.pods)

        if self.services is not None and not isinstance(self.services, str):
            self.services = str(self.services)

        if self.persistentvolumeclaims is not None and not isinstance(self.persistentvolumeclaims, str):
            self.persistentvolumeclaims = str(self.persistentvolumeclaims)

        if self.requests_storage is not None and not isinstance(self.requests_storage, str):
            self.requests_storage = str(self.requests_storage)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LimitRangeConfig(YAMLRoot):
    """
    Default container resource limits for the project namespace.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["LimitRangeConfig"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:LimitRangeConfig"
    class_name: ClassVar[str] = "LimitRangeConfig"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.LimitRangeConfig

    default_memory: Optional[str] = None
    default_cpu: Optional[str] = None
    default_request_memory: Optional[str] = None
    default_request_cpu: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.default_memory is not None and not isinstance(self.default_memory, str):
            self.default_memory = str(self.default_memory)

        if self.default_cpu is not None and not isinstance(self.default_cpu, str):
            self.default_cpu = str(self.default_cpu)

        if self.default_request_memory is not None and not isinstance(self.default_request_memory, str):
            self.default_request_memory = str(self.default_request_memory)

        if self.default_request_cpu is not None and not isinstance(self.default_request_cpu, str):
            self.default_request_cpu = str(self.default_request_cpu)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VdiSchedulingResources(YAMLRoot):
    """
    CPU and memory resource requests/limits for a VDI pod.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["VdiSchedulingResources"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:VdiSchedulingResources"
    class_name: ClassVar[str] = "VdiSchedulingResources"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.VdiSchedulingResources

    requests_cpu: Optional[str] = None
    requests_memory: Optional[str] = None
    limits_cpu: Optional[str] = None
    limits_memory: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.requests_cpu is not None and not isinstance(self.requests_cpu, str):
            self.requests_cpu = str(self.requests_cpu)

        if self.requests_memory is not None and not isinstance(self.requests_memory, str):
            self.requests_memory = str(self.requests_memory)

        if self.limits_cpu is not None and not isinstance(self.limits_cpu, str):
            self.limits_cpu = str(self.limits_cpu)

        if self.limits_memory is not None and not isinstance(self.limits_memory, str):
            self.limits_memory = str(self.limits_memory)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VdiScheduling(YAMLRoot):
    """
    Scheduling configuration for a VDI.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["VdiScheduling"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:VdiScheduling"
    class_name: ClassVar[str] = "VdiScheduling"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.VdiScheduling

    resources: Optional[Union[dict, VdiSchedulingResources]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.resources is not None and not isinstance(self.resources, VdiSchedulingResources):
            self.resources = VdiSchedulingResources(**as_dict(self.resources))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ResourceStorage(YAMLRoot):
    """
    Per-resource storage configuration for workspace persistent volumes.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CR8TOR_METAMODEL["ResourceStorage"]
    class_class_curie: ClassVar[str] = "cr8tor_metamodel:ResourceStorage"
    class_name: ClassVar[str] = "ResourceStorage"
    class_model_uri: ClassVar[URIRef] = CR8TOR_METAMODEL.ResourceStorage

    default_vdi_size: Optional[str] = None
    default_notebook_size: Optional[str] = None
    persist: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.default_vdi_size is not None and not isinstance(self.default_vdi_size, str):
            self.default_vdi_size = str(self.default_vdi_size)

        if self.default_notebook_size is not None and not isinstance(self.default_notebook_size, str):
            self.default_notebook_size = str(self.default_notebook_size)

        if self.persist is not None and not isinstance(self.persist, Bool):
            self.persist = Bool(self.persist)

        super().__post_init__(**kwargs)


# Enumerations
class GroupMembershipType(EnumDefinitionImpl):
    """
    Type of TRE group membership
    """
    Manual = PermissibleValue(
        text="Manual",
        description="Manually assigned group membership")
    Automatic = PermissibleValue(
        text="Automatic",
        description="Automatically assigned group membership")

    _defn = EnumDefinition(
        name="GroupMembershipType",
        description="Type of TRE group membership",
    )

class ActionType(EnumDefinitionImpl):
    """
    Types of actions that can be performed on a Cr8tor project
    """
    Action = PermissibleValue(
        text="Action",
        description="Generic action type")
    CreateAction = PermissibleValue(
        text="CreateAction",
        description="Action to create or initialize a project")
    AssessAction = PermissibleValue(
        text="AssessAction",
        description="Action to assess or evaluate a project (e.g., validation, disclosure check)")
    UpdateAction = PermissibleValue(
        text="UpdateAction",
        description="Action to update project metadata or resources")
    OrchestrationAction = PermissibleValue(
        text="OrchestrationAction",
        description="Action to orchestrate deployment or provisioning")

    _defn = EnumDefinition(
        name="ActionType",
        description="Types of actions that can be performed on a Cr8tor project",
    )

class ActionStatusType(EnumDefinitionImpl):
    """
    Status states for actions, based on schema.org ActionStatusType
    """
    ActiveActionStatus = PermissibleValue(
        text="ActiveActionStatus",
        description="Action is currently in progress")
    CompletedActionStatus = PermissibleValue(
        text="CompletedActionStatus",
        description="Action completed successfully")
    FailedActionStatus = PermissibleValue(
        text="FailedActionStatus",
        description="Action failed with errors")
    PotentialActionStatus = PermissibleValue(
        text="PotentialActionStatus",
        description="Action is potential but not yet started")

    _defn = EnumDefinition(
        name="ActionStatusType",
        description="Status states for actions, based on schema.org ActionStatusType",
    )

class DestinationType(EnumDefinitionImpl):

    filestore = PermissibleValue(
        text="filestore",
        description="Filestore endpoint")
    postgresql = PermissibleValue(
        text="postgresql",
        description="PostgreSQL database endpoint")

    _defn = EnumDefinition(
        name="DestinationType",
    )

class SourceType(EnumDefinitionImpl):

    databricks = PermissibleValue(
        text="databricks",
        description="Databricks endpoint")
    postgresql = PermissibleValue(
        text="postgresql",
        description="PostgreSQL database endpoint")

    _defn = EnumDefinition(
        name="SourceType",
    )

class ConnectionType(EnumDefinitionImpl):
    """
    VDI connection protocols.
    """
    rdp = PermissibleValue(
        text="rdp",
        description="Remote Desktop Protocol.")
    vnc = PermissibleValue(
        text="vnc",
        description="Virtual Network Computing.")

    _defn = EnumDefinition(
        name="ConnectionType",
        description="VDI connection protocols.",
    )

class GiteaVisibility(EnumDefinitionImpl):
    """
    Gitea organisation visibility levels.
    """
    private = PermissibleValue(
        text="private",
        description="Visible only to organisation members.")
    limited = PermissibleValue(
        text="limited",
        description="Visible to signed-in users only.")
    public = PermissibleValue(
        text="public",
        description="Visible to everyone.")

    _defn = EnumDefinition(
        name="GiteaVisibility",
        description="Gitea organisation visibility levels.",
    )

class GiteaPermission(EnumDefinitionImpl):
    """
    Gitea team and repository permission levels.
    """
    read = PermissibleValue(
        text="read",
        description="Read-only access to organisation repositories.")
    write = PermissibleValue(
        text="write",
        description="Read and write access to organisation repositories.")
    admin = PermissibleValue(
        text="admin",
        description="Administrative access to the organisation and its repositories.")

    _defn = EnumDefinition(
        name="GiteaPermission",
        description="Gitea team and repository permission levels.",
    )

# Slots
class slots:
    pass

slots.action_type = Slot(uri=CR8TOR_METAMODEL.action_type, name="action_type", curie=CR8TOR_METAMODEL.curie('action_type'),
                   model_uri=CR8TOR_METAMODEL.action_type, domain=None, range=str)

slots.resource_type = Slot(uri=CR8TOR_METAMODEL.resource_type, name="resource_type", curie=CR8TOR_METAMODEL.curie('resource_type'),
                   model_uri=CR8TOR_METAMODEL.resource_type, domain=None, range=str)

slots.cr8tor__governance = Slot(uri=CR8TOR_METAMODEL.governance, name="cr8tor__governance", curie=CR8TOR_METAMODEL.curie('governance'),
                   model_uri=CR8TOR_METAMODEL.cr8tor__governance, domain=None, range=Union[dict, Governance])

slots.cr8tor__ingress = Slot(uri=CR8TOR_METAMODEL.ingress, name="cr8tor__ingress", curie=CR8TOR_METAMODEL.curie('ingress'),
                   model_uri=CR8TOR_METAMODEL.cr8tor__ingress, domain=None, range=Union[dict, Ingress])

slots.cr8tor__deployment = Slot(uri=CR8TOR_METAMODEL.deployment, name="cr8tor__deployment", curie=CR8TOR_METAMODEL.curie('deployment'),
                   model_uri=CR8TOR_METAMODEL.cr8tor__deployment, domain=None, range=Union[dict, Deployment])

slots.governance__project = Slot(uri=CR8TOR_METAMODEL.project, name="governance__project", curie=CR8TOR_METAMODEL.curie('project'),
                   model_uri=CR8TOR_METAMODEL.governance__project, domain=None, range=Union[dict, Project])

slots.governance__users = Slot(uri=CR8TOR_METAMODEL.users, name="governance__users", curie=CR8TOR_METAMODEL.curie('users'),
                   model_uri=CR8TOR_METAMODEL.governance__users, domain=None, range=Union[Union[dict, User], list[Union[dict, User]]])

slots.project__id = Slot(uri=CR8TOR_METAMODEL.id, name="project__id", curie=CR8TOR_METAMODEL.curie('id'),
                   model_uri=CR8TOR_METAMODEL.project__id, domain=None, range=Optional[str])

slots.project__name = Slot(uri=CR8TOR_METAMODEL.name, name="project__name", curie=CR8TOR_METAMODEL.curie('name'),
                   model_uri=CR8TOR_METAMODEL.project__name, domain=None, range=str)

slots.project__description = Slot(uri=CR8TOR_METAMODEL.description, name="project__description", curie=CR8TOR_METAMODEL.curie('description'),
                   model_uri=CR8TOR_METAMODEL.project__description, domain=None, range=str)

slots.project__reference = Slot(uri=CR8TOR_METAMODEL.reference, name="project__reference", curie=CR8TOR_METAMODEL.curie('reference'),
                   model_uri=CR8TOR_METAMODEL.project__reference, domain=None, range=Optional[str])

slots.project__start_time = Slot(uri=CR8TOR_METAMODEL.start_time, name="project__start_time", curie=CR8TOR_METAMODEL.curie('start_time'),
                   model_uri=CR8TOR_METAMODEL.project__start_time, domain=None, range=Optional[str])

slots.project__actions = Slot(uri=CR8TOR_METAMODEL.actions, name="project__actions", curie=CR8TOR_METAMODEL.curie('actions'),
                   model_uri=CR8TOR_METAMODEL.project__actions, domain=None, range=Optional[Union[dict[Union[str, ActionId], Union[dict, Action]], list[Union[dict, Action]]]])

slots.action__id = Slot(uri=CR8TOR_METAMODEL.id, name="action__id", curie=CR8TOR_METAMODEL.curie('id'),
                   model_uri=CR8TOR_METAMODEL.action__id, domain=None, range=URIRef)

slots.action__name = Slot(uri=CR8TOR_METAMODEL.name, name="action__name", curie=CR8TOR_METAMODEL.curie('name'),
                   model_uri=CR8TOR_METAMODEL.action__name, domain=None, range=str)

slots.action__start_time = Slot(uri=CR8TOR_METAMODEL.start_time, name="action__start_time", curie=CR8TOR_METAMODEL.curie('start_time'),
                   model_uri=CR8TOR_METAMODEL.action__start_time, domain=None, range=Union[str, XSDDateTime])

slots.action__end_time = Slot(uri=CR8TOR_METAMODEL.end_time, name="action__end_time", curie=CR8TOR_METAMODEL.curie('end_time'),
                   model_uri=CR8TOR_METAMODEL.action__end_time, domain=None, range=Union[str, XSDDateTime])

slots.action__action_status = Slot(uri=CR8TOR_METAMODEL.action_status, name="action__action_status", curie=CR8TOR_METAMODEL.curie('action_status'),
                   model_uri=CR8TOR_METAMODEL.action__action_status, domain=None, range=Union[str, "ActionStatusType"])

slots.action__agent = Slot(uri=CR8TOR_METAMODEL.agent, name="action__agent", curie=CR8TOR_METAMODEL.curie('agent'),
                   model_uri=CR8TOR_METAMODEL.action__agent, domain=None, range=str)

slots.action__instrument = Slot(uri=CR8TOR_METAMODEL.instrument, name="action__instrument", curie=CR8TOR_METAMODEL.curie('instrument'),
                   model_uri=CR8TOR_METAMODEL.action__instrument, domain=None, range=Optional[str])

slots.action__result = Slot(uri=CR8TOR_METAMODEL.result, name="action__result", curie=CR8TOR_METAMODEL.curie('result'),
                   model_uri=CR8TOR_METAMODEL.action__result, domain=None, range=Optional[Union[str, list[str]]])

slots.action__error = Slot(uri=CR8TOR_METAMODEL.error, name="action__error", curie=CR8TOR_METAMODEL.curie('error'),
                   model_uri=CR8TOR_METAMODEL.action__error, domain=None, range=Optional[str])

slots.assessAction__additional_type = Slot(uri=CR8TOR_METAMODEL.additional_type, name="assessAction__additional_type", curie=CR8TOR_METAMODEL.curie('additional_type'),
                   model_uri=CR8TOR_METAMODEL.assessAction__additional_type, domain=None, range=Optional[str])

slots.user__id = Slot(uri=SCHEMAORG.identifier, name="user__id", curie=SCHEMAORG.curie('identifier'),
                   model_uri=CR8TOR_METAMODEL.user__id, domain=None, range=Optional[str])

slots.user__username = Slot(uri=SCHEMAORG.identifier, name="user__username", curie=SCHEMAORG.curie('identifier'),
                   model_uri=CR8TOR_METAMODEL.user__username, domain=None, range=Union[str, URIorCURIE])

slots.user__given_name = Slot(uri=SCHEMAORG.name, name="user__given_name", curie=SCHEMAORG.curie('name'),
                   model_uri=CR8TOR_METAMODEL.user__given_name, domain=None, range=str)

slots.user__family_name = Slot(uri=CR8TOR_METAMODEL.family_name, name="user__family_name", curie=CR8TOR_METAMODEL.curie('family_name'),
                   model_uri=CR8TOR_METAMODEL.user__family_name, domain=None, range=str)

slots.user__affiliation = Slot(uri=CR8TOR_METAMODEL.affiliation, name="user__affiliation", curie=CR8TOR_METAMODEL.curie('affiliation'),
                   model_uri=CR8TOR_METAMODEL.user__affiliation, domain=None, range=str)

slots.user__email = Slot(uri=CR8TOR_METAMODEL.email, name="user__email", curie=CR8TOR_METAMODEL.curie('email'),
                   model_uri=CR8TOR_METAMODEL.user__email, domain=None, range=str,
                   pattern=re.compile(r'^\S+@\S+\.\S+$'))

slots.user__groups = Slot(uri=CR8TOR_METAMODEL.groups, name="user__groups", curie=CR8TOR_METAMODEL.curie('groups'),
                   model_uri=CR8TOR_METAMODEL.user__groups, domain=None, range=Optional[Union[Union[dict, Group], list[Union[dict, Group]]]])

slots.user__start_date = Slot(uri=CR8TOR_METAMODEL.start_date, name="user__start_date", curie=CR8TOR_METAMODEL.curie('start_date'),
                   model_uri=CR8TOR_METAMODEL.user__start_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.user__expiry_date = Slot(uri=CR8TOR_METAMODEL.expiry_date, name="user__expiry_date", curie=CR8TOR_METAMODEL.curie('expiry_date'),
                   model_uri=CR8TOR_METAMODEL.user__expiry_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.user__enabled = Slot(uri=CR8TOR_METAMODEL.enabled, name="user__enabled", curie=CR8TOR_METAMODEL.curie('enabled'),
                   model_uri=CR8TOR_METAMODEL.user__enabled, domain=None, range=Optional[Union[bool, Bool]])

slots.user__password = Slot(uri=CR8TOR_METAMODEL.password, name="user__password", curie=CR8TOR_METAMODEL.curie('password'),
                   model_uri=CR8TOR_METAMODEL.user__password, domain=None, range=Optional[str])

slots.group__value = Slot(uri=CR8TOR_METAMODEL.value, name="group__value", curie=CR8TOR_METAMODEL.curie('value'),
                   model_uri=CR8TOR_METAMODEL.group__value, domain=None, range=Optional[str])

slots.group__ref = Slot(uri=CR8TOR_METAMODEL.ref, name="group__ref", curie=CR8TOR_METAMODEL.curie('ref'),
                   model_uri=CR8TOR_METAMODEL.group__ref, domain=None, range=Optional[Union[str, URI]])

slots.group__display = Slot(uri=CR8TOR_METAMODEL.display, name="group__display", curie=CR8TOR_METAMODEL.curie('display'),
                   model_uri=CR8TOR_METAMODEL.group__display, domain=None, range=Optional[str])

slots.group__type = Slot(uri=CR8TOR_METAMODEL.type, name="group__type", curie=CR8TOR_METAMODEL.curie('type'),
                   model_uri=CR8TOR_METAMODEL.group__type, domain=None, range=Optional[Union[str, "GroupMembershipType"]])

slots.ingress__source = Slot(uri=CR8TOR_METAMODEL.source, name="ingress__source", curie=CR8TOR_METAMODEL.curie('source'),
                   model_uri=CR8TOR_METAMODEL.ingress__source, domain=None, range=Union[dict, Source])

slots.ingress__destination = Slot(uri=CR8TOR_METAMODEL.destination, name="ingress__destination", curie=CR8TOR_METAMODEL.curie('destination'),
                   model_uri=CR8TOR_METAMODEL.ingress__destination, domain=None, range=Union[dict, Destination])

slots.ingress__datasets = Slot(uri=CR8TOR_METAMODEL.datasets, name="ingress__datasets", curie=CR8TOR_METAMODEL.curie('datasets'),
                   model_uri=CR8TOR_METAMODEL.ingress__datasets, domain=None, range=Optional[Union[Union[dict, Dataset], list[Union[dict, Dataset]]]])

slots.source__name = Slot(uri=CR8TOR_METAMODEL.name, name="source__name", curie=CR8TOR_METAMODEL.curie('name'),
                   model_uri=CR8TOR_METAMODEL.source__name, domain=None, range=str)

slots.source__type = Slot(uri=CR8TOR_METAMODEL.type, name="source__type", curie=CR8TOR_METAMODEL.curie('type'),
                   model_uri=CR8TOR_METAMODEL.source__type, domain=None, range=Union[str, "SourceType"])

slots.source__url = Slot(uri=CR8TOR_METAMODEL.url, name="source__url", curie=CR8TOR_METAMODEL.curie('url'),
                   model_uri=CR8TOR_METAMODEL.source__url, domain=None, range=str)

slots.source__credentials = Slot(uri=CR8TOR_METAMODEL.credentials, name="source__credentials", curie=CR8TOR_METAMODEL.curie('credentials'),
                   model_uri=CR8TOR_METAMODEL.source__credentials, domain=None, range=Union[dict, Credential])

slots.credential__provider = Slot(uri=CR8TOR_METAMODEL.provider, name="credential__provider", curie=CR8TOR_METAMODEL.curie('provider'),
                   model_uri=CR8TOR_METAMODEL.credential__provider, domain=None, range=str)

slots.credential__password_key = Slot(uri=CR8TOR_METAMODEL.password_key, name="credential__password_key", curie=CR8TOR_METAMODEL.curie('password_key'),
                   model_uri=CR8TOR_METAMODEL.credential__password_key, domain=None, range=str)

slots.credential__username_key = Slot(uri=CR8TOR_METAMODEL.username_key, name="credential__username_key", curie=CR8TOR_METAMODEL.curie('username_key'),
                   model_uri=CR8TOR_METAMODEL.credential__username_key, domain=None, range=str)

slots.destination__type = Slot(uri=CR8TOR_METAMODEL.type, name="destination__type", curie=CR8TOR_METAMODEL.curie('type'),
                   model_uri=CR8TOR_METAMODEL.destination__type, domain=None, range=Union[str, "DestinationType"])

slots.destination__url = Slot(uri=CR8TOR_METAMODEL.url, name="destination__url", curie=CR8TOR_METAMODEL.curie('url'),
                   model_uri=CR8TOR_METAMODEL.destination__url, domain=None, range=Optional[str])

slots.dataset__name = Slot(uri=CR8TOR_METAMODEL.name, name="dataset__name", curie=CR8TOR_METAMODEL.curie('name'),
                   model_uri=CR8TOR_METAMODEL.dataset__name, domain=None, range=str)

slots.dataset__schema_name = Slot(uri=CR8TOR_METAMODEL.schema_name, name="dataset__schema_name", curie=CR8TOR_METAMODEL.curie('schema_name'),
                   model_uri=CR8TOR_METAMODEL.dataset__schema_name, domain=None, range=str)

slots.dataset__tables = Slot(uri=CR8TOR_METAMODEL.tables, name="dataset__tables", curie=CR8TOR_METAMODEL.curie('tables'),
                   model_uri=CR8TOR_METAMODEL.dataset__tables, domain=None, range=Optional[Union[Union[dict, Table], list[Union[dict, Table]]]])

slots.dataset__locations = Slot(uri=CR8TOR_METAMODEL.locations, name="dataset__locations", curie=CR8TOR_METAMODEL.curie('locations'),
                   model_uri=CR8TOR_METAMODEL.dataset__locations, domain=None, range=Optional[Union[Union[dict, Location], list[Union[dict, Location]]]])

slots.table__name = Slot(uri=CR8TOR_METAMODEL.name, name="table__name", curie=CR8TOR_METAMODEL.curie('name'),
                   model_uri=CR8TOR_METAMODEL.table__name, domain=None, range=str)

slots.table__columns = Slot(uri=CR8TOR_METAMODEL.columns, name="table__columns", curie=CR8TOR_METAMODEL.curie('columns'),
                   model_uri=CR8TOR_METAMODEL.table__columns, domain=None, range=Union[Union[dict, Column], list[Union[dict, Column]]])

slots.column__name = Slot(uri=CR8TOR_METAMODEL.name, name="column__name", curie=CR8TOR_METAMODEL.curie('name'),
                   model_uri=CR8TOR_METAMODEL.column__name, domain=None, range=str)

slots.column__datatype = Slot(uri=CR8TOR_METAMODEL.datatype, name="column__datatype", curie=CR8TOR_METAMODEL.curie('datatype'),
                   model_uri=CR8TOR_METAMODEL.column__datatype, domain=None, range=str)

slots.deployment__resources = Slot(uri=CR8TOR_METAMODEL.resources, name="deployment__resources", curie=CR8TOR_METAMODEL.curie('resources'),
                   model_uri=CR8TOR_METAMODEL.deployment__resources, domain=None, range=Optional[Union[Union[dict, Resource], list[Union[dict, Resource]]]])

slots.deployment__environment = Slot(uri=CR8TOR_METAMODEL.environment, name="deployment__environment", curie=CR8TOR_METAMODEL.curie('environment'),
                   model_uri=CR8TOR_METAMODEL.deployment__environment, domain=None, range=Union[dict, Environment])

slots.deployment__limit_range = Slot(uri=CR8TOR_METAMODEL.limit_range, name="deployment__limit_range", curie=CR8TOR_METAMODEL.curie('limit_range'),
                   model_uri=CR8TOR_METAMODEL.deployment__limit_range, domain=None, range=Optional[Union[dict, LimitRangeConfig]])

slots.resource__name = Slot(uri=CR8TOR_METAMODEL.name, name="resource__name", curie=CR8TOR_METAMODEL.curie('name'),
                   model_uri=CR8TOR_METAMODEL.resource__name, domain=None, range=str)

slots.resource__url = Slot(uri=CR8TOR_METAMODEL.url, name="resource__url", curie=CR8TOR_METAMODEL.curie('url'),
                   model_uri=CR8TOR_METAMODEL.resource__url, domain=None, range=Union[str, URI])

slots.resource__enabled = Slot(uri=CR8TOR_METAMODEL.enabled, name="resource__enabled", curie=CR8TOR_METAMODEL.curie('enabled'),
                   model_uri=CR8TOR_METAMODEL.resource__enabled, domain=None, range=Union[bool, Bool])

slots.jupyter__auth = Slot(uri=CR8TOR_METAMODEL.auth, name="jupyter__auth", curie=CR8TOR_METAMODEL.curie('auth'),
                   model_uri=CR8TOR_METAMODEL.jupyter__auth, domain=None, range=Optional[str])

slots.jupyter__profiles = Slot(uri=CR8TOR_METAMODEL.profiles, name="jupyter__profiles", curie=CR8TOR_METAMODEL.curie('profiles'),
                   model_uri=CR8TOR_METAMODEL.jupyter__profiles, domain=None, range=Optional[Union[Union[dict, ProfileConfig], list[Union[dict, ProfileConfig]]]])

slots.jupyter__storage = Slot(uri=CR8TOR_METAMODEL.storage, name="jupyter__storage", curie=CR8TOR_METAMODEL.curie('storage'),
                   model_uri=CR8TOR_METAMODEL.jupyter__storage, domain=None, range=Optional[Union[dict, ResourceStorage]])

slots.keycloak__realm = Slot(uri=CR8TOR_METAMODEL.realm, name="keycloak__realm", curie=CR8TOR_METAMODEL.curie('realm'),
                   model_uri=CR8TOR_METAMODEL.keycloak__realm, domain=None, range=Optional[str])

slots.keycloak__clients = Slot(uri=CR8TOR_METAMODEL.clients, name="keycloak__clients", curie=CR8TOR_METAMODEL.curie('clients'),
                   model_uri=CR8TOR_METAMODEL.keycloak__clients, domain=None, range=Optional[Union[Union[dict, KeycloakClientConfig], list[Union[dict, KeycloakClientConfig]]]])

slots.vDI__image = Slot(uri=CR8TOR_METAMODEL.image, name="vDI__image", curie=CR8TOR_METAMODEL.curie('image'),
                   model_uri=CR8TOR_METAMODEL.vDI__image, domain=None, range=Optional[str])

slots.vDI__user = Slot(uri=CR8TOR_METAMODEL.user, name="vDI__user", curie=CR8TOR_METAMODEL.curie('user'),
                   model_uri=CR8TOR_METAMODEL.vDI__user, domain=None, range=Optional[str])

slots.vDI__project = Slot(uri=CR8TOR_METAMODEL.project, name="vDI__project", curie=CR8TOR_METAMODEL.curie('project'),
                   model_uri=CR8TOR_METAMODEL.vDI__project, domain=None, range=Optional[str])

slots.vDI__url = Slot(uri=CR8TOR_METAMODEL.url, name="vDI__url", curie=CR8TOR_METAMODEL.curie('url'),
                   model_uri=CR8TOR_METAMODEL.vDI__url, domain=None, range=Optional[Union[str, URI]])

slots.vDI__connection = Slot(uri=CR8TOR_METAMODEL.connection, name="vDI__connection", curie=CR8TOR_METAMODEL.curie('connection'),
                   model_uri=CR8TOR_METAMODEL.vDI__connection, domain=None, range=Optional[Union[str, "ConnectionType"]])

slots.vDI__env = Slot(uri=CR8TOR_METAMODEL.env, name="vDI__env", curie=CR8TOR_METAMODEL.curie('env'),
                   model_uri=CR8TOR_METAMODEL.vDI__env, domain=None, range=Optional[Union[Union[dict, EnvironmentVariable], list[Union[dict, EnvironmentVariable]]]])

slots.vDI__scheduling = Slot(uri=CR8TOR_METAMODEL.scheduling, name="vDI__scheduling", curie=CR8TOR_METAMODEL.curie('scheduling'),
                   model_uri=CR8TOR_METAMODEL.vDI__scheduling, domain=None, range=Optional[Union[dict, VdiScheduling]])

slots.vDI__storage = Slot(uri=CR8TOR_METAMODEL.storage, name="vDI__storage", curie=CR8TOR_METAMODEL.curie('storage'),
                   model_uri=CR8TOR_METAMODEL.vDI__storage, domain=None, range=Optional[Union[dict, ResourceStorage]])

slots.gitea__visibility = Slot(uri=CR8TOR_METAMODEL.visibility, name="gitea__visibility", curie=CR8TOR_METAMODEL.curie('visibility'),
                   model_uri=CR8TOR_METAMODEL.gitea__visibility, domain=None, range=Optional[Union[str, "GiteaVisibility"]])

slots.gitea__create_template_repo = Slot(uri=CR8TOR_METAMODEL.create_template_repo, name="gitea__create_template_repo", curie=CR8TOR_METAMODEL.curie('create_template_repo'),
                   model_uri=CR8TOR_METAMODEL.gitea__create_template_repo, domain=None, range=Optional[Union[bool, Bool]])

slots.gitea__default_repo_permission = Slot(uri=CR8TOR_METAMODEL.default_repo_permission, name="gitea__default_repo_permission", curie=CR8TOR_METAMODEL.curie('default_repo_permission'),
                   model_uri=CR8TOR_METAMODEL.gitea__default_repo_permission, domain=None, range=Optional[Union[str, "GiteaPermission"]])

slots.environment__name = Slot(uri=CR8TOR_METAMODEL.name, name="environment__name", curie=CR8TOR_METAMODEL.curie('name'),
                   model_uri=CR8TOR_METAMODEL.environment__name, domain=None, range=str)

slots.egressRule__fqdn = Slot(uri=CR8TOR_METAMODEL.fqdn, name="egressRule__fqdn", curie=CR8TOR_METAMODEL.curie('fqdn'),
                   model_uri=CR8TOR_METAMODEL.egressRule__fqdn, domain=None, range=str)

slots.egressRule__ports = Slot(uri=CR8TOR_METAMODEL.ports, name="egressRule__ports", curie=CR8TOR_METAMODEL.curie('ports'),
                   model_uri=CR8TOR_METAMODEL.egressRule__ports, domain=None, range=Optional[Union[int, list[int]]])

slots.projectSpec__description = Slot(uri=CR8TOR_METAMODEL.description, name="projectSpec__description", curie=CR8TOR_METAMODEL.curie('description'),
                   model_uri=CR8TOR_METAMODEL.projectSpec__description, domain=None, range=str)

slots.projectSpec__resources = Slot(uri=CR8TOR_METAMODEL.resources, name="projectSpec__resources", curie=CR8TOR_METAMODEL.curie('resources'),
                   model_uri=CR8TOR_METAMODEL.projectSpec__resources, domain=None, range=Optional[Union[Union[dict, Resource], list[Union[dict, Resource]]]])

slots.projectSpec__resource_quota = Slot(uri=CR8TOR_METAMODEL.resource_quota, name="projectSpec__resource_quota", curie=CR8TOR_METAMODEL.curie('resource_quota'),
                   model_uri=CR8TOR_METAMODEL.projectSpec__resource_quota, domain=None, range=Optional[Union[dict, ResourceQuotaConfig]])

slots.projectSpec__limit_range = Slot(uri=CR8TOR_METAMODEL.limit_range, name="projectSpec__limit_range", curie=CR8TOR_METAMODEL.curie('limit_range'),
                   model_uri=CR8TOR_METAMODEL.projectSpec__limit_range, domain=None, range=Optional[Union[dict, LimitRangeConfig]])

slots.projectSpec__approved_egress_rules = Slot(uri=CR8TOR_METAMODEL.approved_egress_rules, name="projectSpec__approved_egress_rules", curie=CR8TOR_METAMODEL.curie('approved_egress_rules'),
                   model_uri=CR8TOR_METAMODEL.projectSpec__approved_egress_rules, domain=None, range=Optional[Union[Union[dict, EgressRule], list[Union[dict, EgressRule]]]])

slots.groupSpec__description = Slot(uri=CR8TOR_METAMODEL.description, name="groupSpec__description", curie=CR8TOR_METAMODEL.curie('description'),
                   model_uri=CR8TOR_METAMODEL.groupSpec__description, domain=None, range=Optional[str])

slots.groupSpec__members = Slot(uri=CR8TOR_METAMODEL.members, name="groupSpec__members", curie=CR8TOR_METAMODEL.curie('members'),
                   model_uri=CR8TOR_METAMODEL.groupSpec__members, domain=None, range=Optional[Union[str, list[str]]])

slots.groupSpec__projects = Slot(uri=CR8TOR_METAMODEL.projects, name="groupSpec__projects", curie=CR8TOR_METAMODEL.curie('projects'),
                   model_uri=CR8TOR_METAMODEL.groupSpec__projects, domain=None, range=Optional[Union[str, list[str]]])

slots.groupSpec__subgroups = Slot(uri=CR8TOR_METAMODEL.subgroups, name="groupSpec__subgroups", curie=CR8TOR_METAMODEL.curie('subgroups'),
                   model_uri=CR8TOR_METAMODEL.groupSpec__subgroups, domain=None, range=Optional[Union[str, list[str]]])

slots.groupSpec__gitea = Slot(uri=CR8TOR_METAMODEL.gitea, name="groupSpec__gitea", curie=CR8TOR_METAMODEL.curie('gitea'),
                   model_uri=CR8TOR_METAMODEL.groupSpec__gitea, domain=None, range=Optional[Union[dict, GiteaTeamConfig]])

slots.keycloakClientConfig__client_id = Slot(uri=CR8TOR_METAMODEL.client_id, name="keycloakClientConfig__client_id", curie=CR8TOR_METAMODEL.curie('client_id'),
                   model_uri=CR8TOR_METAMODEL.keycloakClientConfig__client_id, domain=None, range=str)

slots.keycloakClientConfig__name = Slot(uri=CR8TOR_METAMODEL.name, name="keycloakClientConfig__name", curie=CR8TOR_METAMODEL.curie('name'),
                   model_uri=CR8TOR_METAMODEL.keycloakClientConfig__name, domain=None, range=Optional[str])

slots.keycloakClientConfig__secret = Slot(uri=CR8TOR_METAMODEL.secret, name="keycloakClientConfig__secret", curie=CR8TOR_METAMODEL.curie('secret'),
                   model_uri=CR8TOR_METAMODEL.keycloakClientConfig__secret, domain=None, range=Optional[str])

slots.keycloakClientConfig__secret_ref = Slot(uri=CR8TOR_METAMODEL.secret_ref, name="keycloakClientConfig__secret_ref", curie=CR8TOR_METAMODEL.curie('secret_ref'),
                   model_uri=CR8TOR_METAMODEL.keycloakClientConfig__secret_ref, domain=None, range=Optional[Union[dict, SecretRef]])

slots.keycloakClientConfig__enabled = Slot(uri=CR8TOR_METAMODEL.enabled, name="keycloakClientConfig__enabled", curie=CR8TOR_METAMODEL.curie('enabled'),
                   model_uri=CR8TOR_METAMODEL.keycloakClientConfig__enabled, domain=None, range=Optional[Union[bool, Bool]])

slots.keycloakClientConfig__public_client = Slot(uri=CR8TOR_METAMODEL.public_client, name="keycloakClientConfig__public_client", curie=CR8TOR_METAMODEL.curie('public_client'),
                   model_uri=CR8TOR_METAMODEL.keycloakClientConfig__public_client, domain=None, range=Optional[Union[bool, Bool]])

slots.keycloakClientConfig__redirect_uris = Slot(uri=CR8TOR_METAMODEL.redirect_uris, name="keycloakClientConfig__redirect_uris", curie=CR8TOR_METAMODEL.curie('redirect_uris'),
                   model_uri=CR8TOR_METAMODEL.keycloakClientConfig__redirect_uris, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.keycloakClientConfig__web_origins = Slot(uri=CR8TOR_METAMODEL.web_origins, name="keycloakClientConfig__web_origins", curie=CR8TOR_METAMODEL.curie('web_origins'),
                   model_uri=CR8TOR_METAMODEL.keycloakClientConfig__web_origins, domain=None, range=Optional[Union[str, list[str]]])

slots.keycloakClientConfig__protocol = Slot(uri=CR8TOR_METAMODEL.protocol, name="keycloakClientConfig__protocol", curie=CR8TOR_METAMODEL.curie('protocol'),
                   model_uri=CR8TOR_METAMODEL.keycloakClientConfig__protocol, domain=None, range=Optional[str])

slots.keycloakClientConfig__default_client_scopes = Slot(uri=CR8TOR_METAMODEL.default_client_scopes, name="keycloakClientConfig__default_client_scopes", curie=CR8TOR_METAMODEL.curie('default_client_scopes'),
                   model_uri=CR8TOR_METAMODEL.keycloakClientConfig__default_client_scopes, domain=None, range=Optional[Union[str, list[str]]])

slots.keycloakClientConfig__optional_client_scopes = Slot(uri=CR8TOR_METAMODEL.optional_client_scopes, name="keycloakClientConfig__optional_client_scopes", curie=CR8TOR_METAMODEL.curie('optional_client_scopes'),
                   model_uri=CR8TOR_METAMODEL.keycloakClientConfig__optional_client_scopes, domain=None, range=Optional[Union[str, list[str]]])

slots.keycloakClientConfig__protocol_mappers = Slot(uri=CR8TOR_METAMODEL.protocol_mappers, name="keycloakClientConfig__protocol_mappers", curie=CR8TOR_METAMODEL.curie('protocol_mappers'),
                   model_uri=CR8TOR_METAMODEL.keycloakClientConfig__protocol_mappers, domain=None, range=Optional[Union[Union[dict, ProtocolMapper], list[Union[dict, ProtocolMapper]]]])

slots.secretRef__name = Slot(uri=CR8TOR_METAMODEL.name, name="secretRef__name", curie=CR8TOR_METAMODEL.curie('name'),
                   model_uri=CR8TOR_METAMODEL.secretRef__name, domain=None, range=str)

slots.secretRef__key = Slot(uri=CR8TOR_METAMODEL.key, name="secretRef__key", curie=CR8TOR_METAMODEL.curie('key'),
                   model_uri=CR8TOR_METAMODEL.secretRef__key, domain=None, range=Optional[str])

slots.protocolMapper__name = Slot(uri=CR8TOR_METAMODEL.name, name="protocolMapper__name", curie=CR8TOR_METAMODEL.curie('name'),
                   model_uri=CR8TOR_METAMODEL.protocolMapper__name, domain=None, range=str)

slots.protocolMapper__protocol_mapper = Slot(uri=CR8TOR_METAMODEL.protocol_mapper, name="protocolMapper__protocol_mapper", curie=CR8TOR_METAMODEL.curie('protocol_mapper'),
                   model_uri=CR8TOR_METAMODEL.protocolMapper__protocol_mapper, domain=None, range=str)

slots.protocolMapper__consent_required = Slot(uri=CR8TOR_METAMODEL.consent_required, name="protocolMapper__consent_required", curie=CR8TOR_METAMODEL.curie('consent_required'),
                   model_uri=CR8TOR_METAMODEL.protocolMapper__consent_required, domain=None, range=Optional[Union[bool, Bool]])

slots.protocolMapper__config = Slot(uri=CR8TOR_METAMODEL.config, name="protocolMapper__config", curie=CR8TOR_METAMODEL.curie('config'),
                   model_uri=CR8TOR_METAMODEL.protocolMapper__config, domain=None, range=Optional[str])

slots.profileConfig__display_name = Slot(uri=CR8TOR_METAMODEL.display_name, name="profileConfig__display_name", curie=CR8TOR_METAMODEL.curie('display_name'),
                   model_uri=CR8TOR_METAMODEL.profileConfig__display_name, domain=None, range=str)

slots.profileConfig__description = Slot(uri=CR8TOR_METAMODEL.description, name="profileConfig__description", curie=CR8TOR_METAMODEL.curie('description'),
                   model_uri=CR8TOR_METAMODEL.profileConfig__description, domain=None, range=Optional[str])

slots.profileConfig__slug = Slot(uri=CR8TOR_METAMODEL.slug, name="profileConfig__slug", curie=CR8TOR_METAMODEL.curie('slug'),
                   model_uri=CR8TOR_METAMODEL.profileConfig__slug, domain=None, range=str)

slots.profileConfig__kubespawner_override = Slot(uri=CR8TOR_METAMODEL.kubespawner_override, name="profileConfig__kubespawner_override", curie=CR8TOR_METAMODEL.curie('kubespawner_override'),
                   model_uri=CR8TOR_METAMODEL.profileConfig__kubespawner_override, domain=None, range=Optional[Union[dict, KubespawnerOverride]])

slots.kubespawnerOverride__image = Slot(uri=CR8TOR_METAMODEL.image, name="kubespawnerOverride__image", curie=CR8TOR_METAMODEL.curie('image'),
                   model_uri=CR8TOR_METAMODEL.kubespawnerOverride__image, domain=None, range=Optional[str])

slots.kubespawnerOverride__env = Slot(uri=CR8TOR_METAMODEL.env, name="kubespawnerOverride__env", curie=CR8TOR_METAMODEL.curie('env'),
                   model_uri=CR8TOR_METAMODEL.kubespawnerOverride__env, domain=None, range=Optional[Union[Union[dict, EnvironmentVariable], list[Union[dict, EnvironmentVariable]]]])

slots.environmentVariable__name = Slot(uri=CR8TOR_METAMODEL.name, name="environmentVariable__name", curie=CR8TOR_METAMODEL.curie('name'),
                   model_uri=CR8TOR_METAMODEL.environmentVariable__name, domain=None, range=str)

slots.environmentVariable__value = Slot(uri=CR8TOR_METAMODEL.value, name="environmentVariable__value", curie=CR8TOR_METAMODEL.curie('value'),
                   model_uri=CR8TOR_METAMODEL.environmentVariable__value, domain=None, range=str)

slots.giteaTeamConfig__team_name = Slot(uri=CR8TOR_METAMODEL.team_name, name="giteaTeamConfig__team_name", curie=CR8TOR_METAMODEL.curie('team_name'),
                   model_uri=CR8TOR_METAMODEL.giteaTeamConfig__team_name, domain=None, range=Optional[str])

slots.giteaTeamConfig__permission = Slot(uri=CR8TOR_METAMODEL.permission, name="giteaTeamConfig__permission", curie=CR8TOR_METAMODEL.curie('permission'),
                   model_uri=CR8TOR_METAMODEL.giteaTeamConfig__permission, domain=None, range=Optional[Union[str, "GiteaPermission"]])

slots.resourceQuotaConfig__requests_cpu = Slot(uri=CR8TOR_METAMODEL.requests_cpu, name="resourceQuotaConfig__requests_cpu", curie=CR8TOR_METAMODEL.curie('requests_cpu'),
                   model_uri=CR8TOR_METAMODEL.resourceQuotaConfig__requests_cpu, domain=None, range=Optional[str])

slots.resourceQuotaConfig__requests_memory = Slot(uri=CR8TOR_METAMODEL.requests_memory, name="resourceQuotaConfig__requests_memory", curie=CR8TOR_METAMODEL.curie('requests_memory'),
                   model_uri=CR8TOR_METAMODEL.resourceQuotaConfig__requests_memory, domain=None, range=Optional[str])

slots.resourceQuotaConfig__limits_cpu = Slot(uri=CR8TOR_METAMODEL.limits_cpu, name="resourceQuotaConfig__limits_cpu", curie=CR8TOR_METAMODEL.curie('limits_cpu'),
                   model_uri=CR8TOR_METAMODEL.resourceQuotaConfig__limits_cpu, domain=None, range=Optional[str])

slots.resourceQuotaConfig__limits_memory = Slot(uri=CR8TOR_METAMODEL.limits_memory, name="resourceQuotaConfig__limits_memory", curie=CR8TOR_METAMODEL.curie('limits_memory'),
                   model_uri=CR8TOR_METAMODEL.resourceQuotaConfig__limits_memory, domain=None, range=Optional[str])

slots.resourceQuotaConfig__pods = Slot(uri=CR8TOR_METAMODEL.pods, name="resourceQuotaConfig__pods", curie=CR8TOR_METAMODEL.curie('pods'),
                   model_uri=CR8TOR_METAMODEL.resourceQuotaConfig__pods, domain=None, range=Optional[str])

slots.resourceQuotaConfig__services = Slot(uri=CR8TOR_METAMODEL.services, name="resourceQuotaConfig__services", curie=CR8TOR_METAMODEL.curie('services'),
                   model_uri=CR8TOR_METAMODEL.resourceQuotaConfig__services, domain=None, range=Optional[str])

slots.resourceQuotaConfig__persistentvolumeclaims = Slot(uri=CR8TOR_METAMODEL.persistentvolumeclaims, name="resourceQuotaConfig__persistentvolumeclaims", curie=CR8TOR_METAMODEL.curie('persistentvolumeclaims'),
                   model_uri=CR8TOR_METAMODEL.resourceQuotaConfig__persistentvolumeclaims, domain=None, range=Optional[str])

slots.resourceQuotaConfig__requests_storage = Slot(uri=CR8TOR_METAMODEL.requests_storage, name="resourceQuotaConfig__requests_storage", curie=CR8TOR_METAMODEL.curie('requests_storage'),
                   model_uri=CR8TOR_METAMODEL.resourceQuotaConfig__requests_storage, domain=None, range=Optional[str])

slots.limitRangeConfig__default_memory = Slot(uri=CR8TOR_METAMODEL.default_memory, name="limitRangeConfig__default_memory", curie=CR8TOR_METAMODEL.curie('default_memory'),
                   model_uri=CR8TOR_METAMODEL.limitRangeConfig__default_memory, domain=None, range=Optional[str])

slots.limitRangeConfig__default_cpu = Slot(uri=CR8TOR_METAMODEL.default_cpu, name="limitRangeConfig__default_cpu", curie=CR8TOR_METAMODEL.curie('default_cpu'),
                   model_uri=CR8TOR_METAMODEL.limitRangeConfig__default_cpu, domain=None, range=Optional[str])

slots.limitRangeConfig__default_request_memory = Slot(uri=CR8TOR_METAMODEL.default_request_memory, name="limitRangeConfig__default_request_memory", curie=CR8TOR_METAMODEL.curie('default_request_memory'),
                   model_uri=CR8TOR_METAMODEL.limitRangeConfig__default_request_memory, domain=None, range=Optional[str])

slots.limitRangeConfig__default_request_cpu = Slot(uri=CR8TOR_METAMODEL.default_request_cpu, name="limitRangeConfig__default_request_cpu", curie=CR8TOR_METAMODEL.curie('default_request_cpu'),
                   model_uri=CR8TOR_METAMODEL.limitRangeConfig__default_request_cpu, domain=None, range=Optional[str])

slots.vdiSchedulingResources__requests_cpu = Slot(uri=CR8TOR_METAMODEL.requests_cpu, name="vdiSchedulingResources__requests_cpu", curie=CR8TOR_METAMODEL.curie('requests_cpu'),
                   model_uri=CR8TOR_METAMODEL.vdiSchedulingResources__requests_cpu, domain=None, range=Optional[str])

slots.vdiSchedulingResources__requests_memory = Slot(uri=CR8TOR_METAMODEL.requests_memory, name="vdiSchedulingResources__requests_memory", curie=CR8TOR_METAMODEL.curie('requests_memory'),
                   model_uri=CR8TOR_METAMODEL.vdiSchedulingResources__requests_memory, domain=None, range=Optional[str])

slots.vdiSchedulingResources__limits_cpu = Slot(uri=CR8TOR_METAMODEL.limits_cpu, name="vdiSchedulingResources__limits_cpu", curie=CR8TOR_METAMODEL.curie('limits_cpu'),
                   model_uri=CR8TOR_METAMODEL.vdiSchedulingResources__limits_cpu, domain=None, range=Optional[str])

slots.vdiSchedulingResources__limits_memory = Slot(uri=CR8TOR_METAMODEL.limits_memory, name="vdiSchedulingResources__limits_memory", curie=CR8TOR_METAMODEL.curie('limits_memory'),
                   model_uri=CR8TOR_METAMODEL.vdiSchedulingResources__limits_memory, domain=None, range=Optional[str])

slots.vdiScheduling__resources = Slot(uri=CR8TOR_METAMODEL.resources, name="vdiScheduling__resources", curie=CR8TOR_METAMODEL.curie('resources'),
                   model_uri=CR8TOR_METAMODEL.vdiScheduling__resources, domain=None, range=Optional[Union[dict, VdiSchedulingResources]])

slots.resourceStorage__default_vdi_size = Slot(uri=CR8TOR_METAMODEL.default_vdi_size, name="resourceStorage__default_vdi_size", curie=CR8TOR_METAMODEL.curie('default_vdi_size'),
                   model_uri=CR8TOR_METAMODEL.resourceStorage__default_vdi_size, domain=None, range=Optional[str])

slots.resourceStorage__default_notebook_size = Slot(uri=CR8TOR_METAMODEL.default_notebook_size, name="resourceStorage__default_notebook_size", curie=CR8TOR_METAMODEL.curie('default_notebook_size'),
                   model_uri=CR8TOR_METAMODEL.resourceStorage__default_notebook_size, domain=None, range=Optional[str])

slots.resourceStorage__persist = Slot(uri=CR8TOR_METAMODEL.persist, name="resourceStorage__persist", curie=CR8TOR_METAMODEL.curie('persist'),
                   model_uri=CR8TOR_METAMODEL.resourceStorage__persist, domain=None, range=Optional[Union[bool, Bool]])
