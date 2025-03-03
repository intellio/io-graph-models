from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class Alert(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	activityGroupName: Optional[str] = Field(default=None,alias="activityGroupName",)
	alertDetections: Optional[list[AlertDetection]] = Field(default=None,alias="alertDetections",)
	assignedTo: Optional[str] = Field(default=None,alias="assignedTo",)
	azureSubscriptionId: Optional[str] = Field(default=None,alias="azureSubscriptionId",)
	azureTenantId: Optional[str] = Field(default=None,alias="azureTenantId",)
	category: Optional[str] = Field(default=None,alias="category",)
	closedDateTime: Optional[datetime] = Field(default=None,alias="closedDateTime",)
	cloudAppStates: Optional[list[CloudAppSecurityState]] = Field(default=None,alias="cloudAppStates",)
	comments: Optional[list[str]] = Field(default=None,alias="comments",)
	confidence: Optional[int] = Field(default=None,alias="confidence",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	detectionIds: Optional[list[str]] = Field(default=None,alias="detectionIds",)
	eventDateTime: Optional[datetime] = Field(default=None,alias="eventDateTime",)
	feedback: Optional[AlertFeedback] = Field(default=None,alias="feedback",)
	fileStates: Optional[list[FileSecurityState]] = Field(default=None,alias="fileStates",)
	historyStates: Optional[list[AlertHistoryState]] = Field(default=None,alias="historyStates",)
	hostStates: Optional[list[HostSecurityState]] = Field(default=None,alias="hostStates",)
	incidentIds: Optional[list[str]] = Field(default=None,alias="incidentIds",)
	investigationSecurityStates: Optional[list[InvestigationSecurityState]] = Field(default=None,alias="investigationSecurityStates",)
	lastEventDateTime: Optional[datetime] = Field(default=None,alias="lastEventDateTime",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	malwareStates: Optional[list[MalwareState]] = Field(default=None,alias="malwareStates",)
	messageSecurityStates: Optional[list[MessageSecurityState]] = Field(default=None,alias="messageSecurityStates",)
	networkConnections: Optional[list[NetworkConnection]] = Field(default=None,alias="networkConnections",)
	processes: Optional[list[Process]] = Field(default=None,alias="processes",)
	recommendedActions: Optional[list[str]] = Field(default=None,alias="recommendedActions",)
	registryKeyStates: Optional[list[RegistryKeyState]] = Field(default=None,alias="registryKeyStates",)
	securityResources: Optional[list[SecurityResource]] = Field(default=None,alias="securityResources",)
	severity: Optional[AlertSeverity] = Field(default=None,alias="severity",)
	sourceMaterials: Optional[list[str]] = Field(default=None,alias="sourceMaterials",)
	status: Optional[AlertStatus] = Field(default=None,alias="status",)
	tags: Optional[list[str]] = Field(default=None,alias="tags",)
	title: Optional[str] = Field(default=None,alias="title",)
	triggers: Optional[list[AlertTrigger]] = Field(default=None,alias="triggers",)
	uriClickSecurityStates: Optional[list[UriClickSecurityState]] = Field(default=None,alias="uriClickSecurityStates",)
	userStates: Optional[list[UserSecurityState]] = Field(default=None,alias="userStates",)
	vendorInformation: Optional[SecurityVendorInformation] = Field(default=None,alias="vendorInformation",)
	vulnerabilityStates: Optional[list[VulnerabilityState]] = Field(default=None,alias="vulnerabilityStates",)

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

