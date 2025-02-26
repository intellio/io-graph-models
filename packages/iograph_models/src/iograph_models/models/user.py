from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class User(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deletedDateTime: Optional[datetime] = Field(default=None,alias="deletedDateTime",)
	aboutMe: Optional[str] = Field(default=None,alias="aboutMe",)
	accountEnabled: Optional[bool] = Field(default=None,alias="accountEnabled",)
	ageGroup: Optional[str] = Field(default=None,alias="ageGroup",)
	assignedLicenses: list[AssignedLicense] = Field(alias="assignedLicenses",)
	assignedPlans: list[AssignedPlan] = Field(alias="assignedPlans",)
	authorizationInfo: Optional[AuthorizationInfo] = Field(default=None,alias="authorizationInfo",)
	birthday: Optional[datetime] = Field(default=None,alias="birthday",)
	businessPhones: list[str] = Field(alias="businessPhones",)
	city: Optional[str] = Field(default=None,alias="city",)
	companyName: Optional[str] = Field(default=None,alias="companyName",)
	consentProvidedForMinor: Optional[str] = Field(default=None,alias="consentProvidedForMinor",)
	country: Optional[str] = Field(default=None,alias="country",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	creationType: Optional[str] = Field(default=None,alias="creationType",)
	customSecurityAttributes: Optional[CustomSecurityAttributeValue] = Field(default=None,alias="customSecurityAttributes",)
	department: Optional[str] = Field(default=None,alias="department",)
	deviceEnrollmentLimit: Optional[int] = Field(default=None,alias="deviceEnrollmentLimit",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	employeeHireDate: Optional[datetime] = Field(default=None,alias="employeeHireDate",)
	employeeId: Optional[str] = Field(default=None,alias="employeeId",)
	employeeLeaveDateTime: Optional[datetime] = Field(default=None,alias="employeeLeaveDateTime",)
	employeeOrgData: Optional[EmployeeOrgData] = Field(default=None,alias="employeeOrgData",)
	employeeType: Optional[str] = Field(default=None,alias="employeeType",)
	externalUserState: Optional[str] = Field(default=None,alias="externalUserState",)
	externalUserStateChangeDateTime: Optional[datetime] = Field(default=None,alias="externalUserStateChangeDateTime",)
	faxNumber: Optional[str] = Field(default=None,alias="faxNumber",)
	givenName: Optional[str] = Field(default=None,alias="givenName",)
	hireDate: Optional[datetime] = Field(default=None,alias="hireDate",)
	identities: list[ObjectIdentity] = Field(alias="identities",)
	imAddresses: list[Optional[str]] = Field(alias="imAddresses",)
	interests: list[Optional[str]] = Field(alias="interests",)
	isManagementRestricted: Optional[bool] = Field(default=None,alias="isManagementRestricted",)
	isResourceAccount: Optional[bool] = Field(default=None,alias="isResourceAccount",)
	jobTitle: Optional[str] = Field(default=None,alias="jobTitle",)
	lastPasswordChangeDateTime: Optional[datetime] = Field(default=None,alias="lastPasswordChangeDateTime",)
	legalAgeGroupClassification: Optional[str] = Field(default=None,alias="legalAgeGroupClassification",)
	licenseAssignmentStates: list[LicenseAssignmentState] = Field(alias="licenseAssignmentStates",)
	mail: Optional[str] = Field(default=None,alias="mail",)
	mailboxSettings: Optional[MailboxSettings] = Field(default=None,alias="mailboxSettings",)
	mailNickname: Optional[str] = Field(default=None,alias="mailNickname",)
	mobilePhone: Optional[str] = Field(default=None,alias="mobilePhone",)
	mySite: Optional[str] = Field(default=None,alias="mySite",)
	officeLocation: Optional[str] = Field(default=None,alias="officeLocation",)
	onPremisesDistinguishedName: Optional[str] = Field(default=None,alias="onPremisesDistinguishedName",)
	onPremisesDomainName: Optional[str] = Field(default=None,alias="onPremisesDomainName",)
	onPremisesExtensionAttributes: Optional[OnPremisesExtensionAttributes] = Field(default=None,alias="onPremisesExtensionAttributes",)
	onPremisesImmutableId: Optional[str] = Field(default=None,alias="onPremisesImmutableId",)
	onPremisesLastSyncDateTime: Optional[datetime] = Field(default=None,alias="onPremisesLastSyncDateTime",)
	onPremisesProvisioningErrors: list[OnPremisesProvisioningError] = Field(alias="onPremisesProvisioningErrors",)
	onPremisesSamAccountName: Optional[str] = Field(default=None,alias="onPremisesSamAccountName",)
	onPremisesSecurityIdentifier: Optional[str] = Field(default=None,alias="onPremisesSecurityIdentifier",)
	onPremisesSyncEnabled: Optional[bool] = Field(default=None,alias="onPremisesSyncEnabled",)
	onPremisesUserPrincipalName: Optional[str] = Field(default=None,alias="onPremisesUserPrincipalName",)
	otherMails: list[str] = Field(alias="otherMails",)
	passwordPolicies: Optional[str] = Field(default=None,alias="passwordPolicies",)
	passwordProfile: Optional[PasswordProfile] = Field(default=None,alias="passwordProfile",)
	pastProjects: list[Optional[str]] = Field(alias="pastProjects",)
	postalCode: Optional[str] = Field(default=None,alias="postalCode",)
	preferredDataLocation: Optional[str] = Field(default=None,alias="preferredDataLocation",)
	preferredLanguage: Optional[str] = Field(default=None,alias="preferredLanguage",)
	preferredName: Optional[str] = Field(default=None,alias="preferredName",)
	print: Optional[UserPrint] = Field(default=None,alias="print",)
	provisionedPlans: list[ProvisionedPlan] = Field(alias="provisionedPlans",)
	proxyAddresses: list[str] = Field(alias="proxyAddresses",)
	responsibilities: list[Optional[str]] = Field(alias="responsibilities",)
	schools: list[Optional[str]] = Field(alias="schools",)
	securityIdentifier: Optional[str] = Field(default=None,alias="securityIdentifier",)
	serviceProvisioningErrors: list[ServiceProvisioningError] = Field(alias="serviceProvisioningErrors",)
	showInAddressList: Optional[bool] = Field(default=None,alias="showInAddressList",)
	signInActivity: Optional[SignInActivity] = Field(default=None,alias="signInActivity",)
	signInSessionsValidFromDateTime: Optional[datetime] = Field(default=None,alias="signInSessionsValidFromDateTime",)
	skills: list[Optional[str]] = Field(alias="skills",)
	state: Optional[str] = Field(default=None,alias="state",)
	streetAddress: Optional[str] = Field(default=None,alias="streetAddress",)
	surname: Optional[str] = Field(default=None,alias="surname",)
	usageLocation: Optional[str] = Field(default=None,alias="usageLocation",)
	userPrincipalName: Optional[str] = Field(default=None,alias="userPrincipalName",)
	userType: Optional[str] = Field(default=None,alias="userType",)
	activities: list[UserActivity] = Field(alias="activities",)
	agreementAcceptances: list[AgreementAcceptance] = Field(alias="agreementAcceptances",)
	appRoleAssignments: list[AppRoleAssignment] = Field(alias="appRoleAssignments",)
	authentication: Optional[Authentication] = Field(default=None,alias="authentication",)
	calendar: Optional[Calendar] = Field(default=None,alias="calendar",)
	calendarGroups: list[CalendarGroup] = Field(alias="calendarGroups",)
	calendars: list[Calendar] = Field(alias="calendars",)
	calendarView: list[Event] = Field(alias="calendarView",)
	chats: list[Chat] = Field(alias="chats",)
	cloudClipboard: Optional[CloudClipboardRoot] = Field(default=None,alias="cloudClipboard",)
	contactFolders: list[ContactFolder] = Field(alias="contactFolders",)
	contacts: list[Contact] = Field(alias="contacts",)
	createdObjects: list[DirectoryObject] = Field(alias="createdObjects",)
	deviceManagementTroubleshootingEvents: list[DeviceManagementTroubleshootingEvent] = Field(alias="deviceManagementTroubleshootingEvents",)
	directReports: list[DirectoryObject] = Field(alias="directReports",)
	drive: Optional[Drive] = Field(default=None,alias="drive",)
	drives: list[Drive] = Field(alias="drives",)
	employeeExperience: Optional[EmployeeExperienceUser] = Field(default=None,alias="employeeExperience",)
	events: list[Event] = Field(alias="events",)
	extensions: list[Extension] = Field(alias="extensions",)
	followedSites: list[Site] = Field(alias="followedSites",)
	inferenceClassification: Optional[InferenceClassification] = Field(default=None,alias="inferenceClassification",)
	insights: Optional[ItemInsights] = Field(default=None,alias="insights",)
	joinedTeams: list[Team] = Field(alias="joinedTeams",)
	licenseDetails: list[LicenseDetails] = Field(alias="licenseDetails",)
	mailFolders: list[MailFolder] = Field(alias="mailFolders",)
	managedAppRegistrations: list[ManagedAppRegistration] = Field(alias="managedAppRegistrations",)
	managedDevices: list[ManagedDevice] = Field(alias="managedDevices",)
	manager: Optional[DirectoryObject] = Field(default=None,alias="manager",)
	memberOf: list[DirectoryObject] = Field(alias="memberOf",)
	messages: list[Message] = Field(alias="messages",)
	oauth2PermissionGrants: list[OAuth2PermissionGrant] = Field(alias="oauth2PermissionGrants",)
	onenote: Optional[Onenote] = Field(default=None,alias="onenote",)
	onlineMeetings: list[OnlineMeeting] = Field(alias="onlineMeetings",)
	outlook: Optional[OutlookUser] = Field(default=None,alias="outlook",)
	ownedDevices: list[DirectoryObject] = Field(alias="ownedDevices",)
	ownedObjects: list[DirectoryObject] = Field(alias="ownedObjects",)
	people: list[Person] = Field(alias="people",)
	permissionGrants: list[ResourceSpecificPermissionGrant] = Field(alias="permissionGrants",)
	photo: Optional[ProfilePhoto] = Field(default=None,alias="photo",)
	photos: list[ProfilePhoto] = Field(alias="photos",)
	planner: Optional[PlannerUser] = Field(default=None,alias="planner",)
	presence: Optional[Presence] = Field(default=None,alias="presence",)
	registeredDevices: list[DirectoryObject] = Field(alias="registeredDevices",)
	scopedRoleMemberOf: list[ScopedRoleMembership] = Field(alias="scopedRoleMemberOf",)
	settings: Optional[UserSettings] = Field(default=None,alias="settings",)
	solutions: Optional[UserSolutionRoot] = Field(default=None,alias="solutions",)
	sponsors: list[DirectoryObject] = Field(alias="sponsors",)
	teamwork: Optional[UserTeamwork] = Field(default=None,alias="teamwork",)
	todo: Optional[Todo] = Field(default=None,alias="todo",)
	transitiveMemberOf: list[DirectoryObject] = Field(alias="transitiveMemberOf",)

from .assigned_license import AssignedLicense
from .assigned_plan import AssignedPlan
from .authorization_info import AuthorizationInfo
from .custom_security_attribute_value import CustomSecurityAttributeValue
from .employee_org_data import EmployeeOrgData
from .object_identity import ObjectIdentity
from .license_assignment_state import LicenseAssignmentState
from .mailbox_settings import MailboxSettings
from .on_premises_extension_attributes import OnPremisesExtensionAttributes
from .on_premises_provisioning_error import OnPremisesProvisioningError
from .password_profile import PasswordProfile
from .user_print import UserPrint
from .provisioned_plan import ProvisionedPlan
from .service_provisioning_error import ServiceProvisioningError
from .sign_in_activity import SignInActivity
from .user_activity import UserActivity
from .agreement_acceptance import AgreementAcceptance
from .app_role_assignment import AppRoleAssignment
from .authentication import Authentication
from .calendar import Calendar
from .calendar_group import CalendarGroup
from .calendar import Calendar
from .event import Event
from .chat import Chat
from .cloud_clipboard_root import CloudClipboardRoot
from .contact_folder import ContactFolder
from .contact import Contact
from .directory_object import DirectoryObject
from .device_management_troubleshooting_event import DeviceManagementTroubleshootingEvent
from .directory_object import DirectoryObject
from .drive import Drive
from .drive import Drive
from .employee_experience_user import EmployeeExperienceUser
from .event import Event
from .extension import Extension
from .site import Site
from .inference_classification import InferenceClassification
from .item_insights import ItemInsights
from .team import Team
from .license_details import LicenseDetails
from .mail_folder import MailFolder
from .managed_app_registration import ManagedAppRegistration
from .managed_device import ManagedDevice
from .directory_object import DirectoryObject
from .directory_object import DirectoryObject
from .message import Message
from .o_auth2_permission_grant import OAuth2PermissionGrant
from .onenote import Onenote
from .online_meeting import OnlineMeeting
from .outlook_user import OutlookUser
from .directory_object import DirectoryObject
from .directory_object import DirectoryObject
from .person import Person
from .resource_specific_permission_grant import ResourceSpecificPermissionGrant
from .profile_photo import ProfilePhoto
from .profile_photo import ProfilePhoto
from .planner_user import PlannerUser
from .presence import Presence
from .directory_object import DirectoryObject
from .scoped_role_membership import ScopedRoleMembership
from .user_settings import UserSettings
from .user_solution_root import UserSolutionRoot
from .directory_object import DirectoryObject
from .user_teamwork import UserTeamwork
from .todo import Todo
from .directory_object import DirectoryObject

