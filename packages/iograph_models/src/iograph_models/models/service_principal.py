from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class ServicePrincipal(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deletedDateTime: Optional[datetime] = Field(default=None,alias="deletedDateTime",)
	accountEnabled: Optional[bool] = Field(default=None,alias="accountEnabled",)
	addIns: Optional[list[AddIn]] = Field(default=None,alias="addIns",)
	alternativeNames: Optional[list[str]] = Field(default=None,alias="alternativeNames",)
	appDescription: Optional[str] = Field(default=None,alias="appDescription",)
	appDisplayName: Optional[str] = Field(default=None,alias="appDisplayName",)
	appId: Optional[str] = Field(default=None,alias="appId",)
	applicationTemplateId: Optional[str] = Field(default=None,alias="applicationTemplateId",)
	appOwnerOrganizationId: Optional[UUID] = Field(default=None,alias="appOwnerOrganizationId",)
	appRoleAssignmentRequired: Optional[bool] = Field(default=None,alias="appRoleAssignmentRequired",)
	appRoles: Optional[list[AppRole]] = Field(default=None,alias="appRoles",)
	customSecurityAttributes: Optional[CustomSecurityAttributeValue] = Field(default=None,alias="customSecurityAttributes",)
	description: Optional[str] = Field(default=None,alias="description",)
	disabledByMicrosoftStatus: Optional[str] = Field(default=None,alias="disabledByMicrosoftStatus",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	homepage: Optional[str] = Field(default=None,alias="homepage",)
	info: Optional[InformationalUrl] = Field(default=None,alias="info",)
	keyCredentials: Optional[list[KeyCredential]] = Field(default=None,alias="keyCredentials",)
	loginUrl: Optional[str] = Field(default=None,alias="loginUrl",)
	logoutUrl: Optional[str] = Field(default=None,alias="logoutUrl",)
	notes: Optional[str] = Field(default=None,alias="notes",)
	notificationEmailAddresses: Optional[list[str]] = Field(default=None,alias="notificationEmailAddresses",)
	oauth2PermissionScopes: Optional[list[PermissionScope]] = Field(default=None,alias="oauth2PermissionScopes",)
	passwordCredentials: Optional[list[PasswordCredential]] = Field(default=None,alias="passwordCredentials",)
	preferredSingleSignOnMode: Optional[str] = Field(default=None,alias="preferredSingleSignOnMode",)
	preferredTokenSigningKeyThumbprint: Optional[str] = Field(default=None,alias="preferredTokenSigningKeyThumbprint",)
	replyUrls: Optional[list[str]] = Field(default=None,alias="replyUrls",)
	resourceSpecificApplicationPermissions: Optional[list[ResourceSpecificPermission]] = Field(default=None,alias="resourceSpecificApplicationPermissions",)
	samlSingleSignOnSettings: Optional[SamlSingleSignOnSettings] = Field(default=None,alias="samlSingleSignOnSettings",)
	servicePrincipalNames: Optional[list[str]] = Field(default=None,alias="servicePrincipalNames",)
	servicePrincipalType: Optional[str] = Field(default=None,alias="servicePrincipalType",)
	signInAudience: Optional[str] = Field(default=None,alias="signInAudience",)
	tags: Optional[list[str]] = Field(default=None,alias="tags",)
	tokenEncryptionKeyId: Optional[UUID] = Field(default=None,alias="tokenEncryptionKeyId",)
	verifiedPublisher: Optional[VerifiedPublisher] = Field(default=None,alias="verifiedPublisher",)
	appManagementPolicies: Optional[list[AppManagementPolicy]] = Field(default=None,alias="appManagementPolicies",)
	appRoleAssignedTo: Optional[list[AppRoleAssignment]] = Field(default=None,alias="appRoleAssignedTo",)
	appRoleAssignments: Optional[list[AppRoleAssignment]] = Field(default=None,alias="appRoleAssignments",)
	claimsMappingPolicies: Optional[list[ClaimsMappingPolicy]] = Field(default=None,alias="claimsMappingPolicies",)
	createdObjects: Optional[list[DirectoryObject]] = Field(default=None,alias="createdObjects",)
	delegatedPermissionClassifications: Optional[list[DelegatedPermissionClassification]] = Field(default=None,alias="delegatedPermissionClassifications",)
	endpoints: Optional[list[Endpoint]] = Field(default=None,alias="endpoints",)
	federatedIdentityCredentials: Optional[list[FederatedIdentityCredential]] = Field(default=None,alias="federatedIdentityCredentials",)
	homeRealmDiscoveryPolicies: Optional[list[HomeRealmDiscoveryPolicy]] = Field(default=None,alias="homeRealmDiscoveryPolicies",)
	memberOf: Optional[list[DirectoryObject]] = Field(default=None,alias="memberOf",)
	oauth2PermissionGrants: Optional[list[OAuth2PermissionGrant]] = Field(default=None,alias="oauth2PermissionGrants",)
	ownedObjects: Optional[list[DirectoryObject]] = Field(default=None,alias="ownedObjects",)
	owners: Optional[list[DirectoryObject]] = Field(default=None,alias="owners",)
	remoteDesktopSecurityConfiguration: Optional[RemoteDesktopSecurityConfiguration] = Field(default=None,alias="remoteDesktopSecurityConfiguration",)
	synchronization: Optional[Synchronization] = Field(default=None,alias="synchronization",)
	tokenIssuancePolicies: Optional[list[TokenIssuancePolicy]] = Field(default=None,alias="tokenIssuancePolicies",)
	tokenLifetimePolicies: Optional[list[TokenLifetimePolicy]] = Field(default=None,alias="tokenLifetimePolicies",)
	transitiveMemberOf: Optional[list[DirectoryObject]] = Field(default=None,alias="transitiveMemberOf",)

from .add_in import AddIn
from .app_role import AppRole
from .custom_security_attribute_value import CustomSecurityAttributeValue
from .informational_url import InformationalUrl
from .key_credential import KeyCredential
from .permission_scope import PermissionScope
from .password_credential import PasswordCredential
from .resource_specific_permission import ResourceSpecificPermission
from .saml_single_sign_on_settings import SamlSingleSignOnSettings
from .verified_publisher import VerifiedPublisher
from .app_management_policy import AppManagementPolicy
from .app_role_assignment import AppRoleAssignment
from .app_role_assignment import AppRoleAssignment
from .claims_mapping_policy import ClaimsMappingPolicy
from .directory_object import DirectoryObject
from .delegated_permission_classification import DelegatedPermissionClassification
from .endpoint import Endpoint
from .federated_identity_credential import FederatedIdentityCredential
from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
from .directory_object import DirectoryObject
from .o_auth2_permission_grant import OAuth2PermissionGrant
from .directory_object import DirectoryObject
from .directory_object import DirectoryObject
from .remote_desktop_security_configuration import RemoteDesktopSecurityConfiguration
from .synchronization import Synchronization
from .token_issuance_policy import TokenIssuancePolicy
from .token_lifetime_policy import TokenLifetimePolicy
from .directory_object import DirectoryObject

