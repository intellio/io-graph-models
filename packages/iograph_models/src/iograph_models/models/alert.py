from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class Alert(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	activityGroupName: Optional[str] = Field(default=None,alias="activityGroupName",)
	alertDetections: list[AlertDetection] = Field(alias="alertDetections",)
	assignedTo: Optional[str] = Field(default=None,alias="assignedTo",)
	azureSubscriptionId: Optional[str] = Field(default=None,alias="azureSubscriptionId",)
	azureTenantId: Optional[str] = Field(default=None,alias="azureTenantId",)
	category: Optional[str] = Field(default=None,alias="category",)
	closedDateTime: Optional[datetime] = Field(default=None,alias="closedDateTime",)
	cloudAppStates: list[CloudAppSecurityState] = Field(alias="cloudAppStates",)
	comments: list[Optional[str]] = Field(alias="comments",)
	confidence: Optional[int] = Field(default=None,alias="confidence",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	detectionIds: list[Optional[str]] = Field(alias="detectionIds",)
	eventDateTime: Optional[datetime] = Field(default=None,alias="eventDateTime",)
	feedback: Optional[AlertFeedback] = Field(default=None,alias="feedback",)
	fileStates: list[FileSecurityState] = Field(alias="fileStates",)
	historyStates: list[AlertHistoryState] = Field(alias="historyStates",)
	hostStates: list[HostSecurityState] = Field(alias="hostStates",)
	incidentIds: list[Optional[str]] = Field(alias="incidentIds",)
	investigationSecurityStates: list[InvestigationSecurityState] = Field(alias="investigationSecurityStates",)
	lastEventDateTime: Optional[datetime] = Field(default=None,alias="lastEventDateTime",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	malwareStates: list[MalwareState] = Field(alias="malwareStates",)
	messageSecurityStates: list[MessageSecurityState] = Field(alias="messageSecurityStates",)
	networkConnections: list[NetworkConnection] = Field(alias="networkConnections",)
	processes: list[Process] = Field(alias="processes",)
	recommendedActions: list[Optional[str]] = Field(alias="recommendedActions",)
	registryKeyStates: list[RegistryKeyState] = Field(alias="registryKeyStates",)
	securityResources: list[SecurityResource] = Field(alias="securityResources",)
	severity: Optional[AlertSeverity] = Field(default=None,alias="severity",)
	sourceMaterials: list[Optional[str]] = Field(alias="sourceMaterials",)
	status: Optional[AlertStatus] = Field(default=None,alias="status",)
	tags: list[Optional[str]] = Field(alias="tags",)
	title: Optional[str] = Field(default=None,alias="title",)
	triggers: list[AlertTrigger] = Field(alias="triggers",)
	uriClickSecurityStates: list[UriClickSecurityState] = Field(alias="uriClickSecurityStates",)
	userStates: list[UserSecurityState] = Field(alias="userStates",)
	vendorInformation: Optional[SecurityVendorInformation] = Field(default=None,alias="vendorInformation",)
	vulnerabilityStates: list[VulnerabilityState] = Field(alias="vulnerabilityStates",)

from .alert_detection import AlertDetection
from .cloud_app_security_state import CloudAppSecurityState
from .alert_feedback import AlertFeedback
from .file_security_state import FileSecurityState
from .alert_history_state import AlertHistoryState
from .host_security_state import HostSecurityState
from .investigation_security_state import InvestigationSecurityState
from .malware_state import MalwareState
from .message_security_state import MessageSecurityState
from .network_connection import NetworkConnection
from .process import Process
from .registry_key_state import RegistryKeyState
from .security_resource import SecurityResource
from .alert_severity import AlertSeverity
from .alert_status import AlertStatus
from .alert_trigger import AlertTrigger
from .uri_click_security_state import UriClickSecurityState
from .user_security_state import UserSecurityState
from .security_vendor_information import SecurityVendorInformation
from .vulnerability_state import VulnerabilityState

