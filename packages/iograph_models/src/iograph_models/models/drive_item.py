from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class DriveItem(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdBy: Optional[IdentitySet] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	eTag: Optional[str] = Field(default=None,alias="eTag",)
	lastModifiedBy: Optional[IdentitySet] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	name: Optional[str] = Field(default=None,alias="name",)
	parentReference: Optional[ItemReference] = Field(default=None,alias="parentReference",)
	webUrl: Optional[str] = Field(default=None,alias="webUrl",)
	createdByUser: Optional[User] = Field(default=None,alias="createdByUser",)
	lastModifiedByUser: Optional[User] = Field(default=None,alias="lastModifiedByUser",)
	audio: Optional[Audio] = Field(default=None,alias="audio",)
	bundle: Optional[Bundle] = Field(default=None,alias="bundle",)
	content: Optional[str] = Field(default=None,alias="content",)
	cTag: Optional[str] = Field(default=None,alias="cTag",)
	deleted: Optional[Deleted] = Field(default=None,alias="deleted",)
	file: Optional[File] = Field(default=None,alias="file",)
	fileSystemInfo: Optional[FileSystemInfo] = Field(default=None,alias="fileSystemInfo",)
	folder: Optional[Folder] = Field(default=None,alias="folder",)
	image: Optional[Image] = Field(default=None,alias="image",)
	location: Optional[GeoCoordinates] = Field(default=None,alias="location",)
	malware: Optional[Malware] = Field(default=None,alias="malware",)
	package: Optional[Package] = Field(default=None,alias="package",)
	pendingOperations: Optional[PendingOperations] = Field(default=None,alias="pendingOperations",)
	photo: Optional[Photo] = Field(default=None,alias="photo",)
	publication: Optional[PublicationFacet] = Field(default=None,alias="publication",)
	remoteItem: Optional[RemoteItem] = Field(default=None,alias="remoteItem",)
	root: Optional[Root] = Field(default=None,alias="root",)
	searchResult: Optional[SearchResult] = Field(default=None,alias="searchResult",)
	shared: Optional[Shared] = Field(default=None,alias="shared",)
	sharepointIds: Optional[SharepointIds] = Field(default=None,alias="sharepointIds",)
	size: Optional[int] = Field(default=None,alias="size",)
	specialFolder: Optional[SpecialFolder] = Field(default=None,alias="specialFolder",)
	video: Optional[Video] = Field(default=None,alias="video",)
	webDavUrl: Optional[str] = Field(default=None,alias="webDavUrl",)
	analytics: Optional[ItemAnalytics] = Field(default=None,alias="analytics",)
	children: Optional[list[DriveItem]] = Field(default=None,alias="children",)
	listItem: Optional[ListItem] = Field(default=None,alias="listItem",)
	permissions: Optional[list[Permission]] = Field(default=None,alias="permissions",)
	retentionLabel: Optional[ItemRetentionLabel] = Field(default=None,alias="retentionLabel",)
	subscriptions: Optional[list[Subscription]] = Field(default=None,alias="subscriptions",)
	thumbnails: Optional[list[ThumbnailSet]] = Field(default=None,alias="thumbnails",)
	versions: Optional[list[DriveItemVersion]] = Field(default=None,alias="versions",)
	workbook: Optional[Workbook] = Field(default=None,alias="workbook",)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .item_reference import ItemReference
from .user import User
from .user import User
from .audio import Audio
from .bundle import Bundle
from .deleted import Deleted
from .file import File
from .file_system_info import FileSystemInfo
from .folder import Folder
from .image import Image
from .geo_coordinates import GeoCoordinates
from .malware import Malware
from .package import Package
from .pending_operations import PendingOperations
from .photo import Photo
from .publication_facet import PublicationFacet
from .remote_item import RemoteItem
from .root import Root
from .search_result import SearchResult
from .shared import Shared
from .sharepoint_ids import SharepointIds
from .special_folder import SpecialFolder
from .video import Video
from .item_analytics import ItemAnalytics
from .list_item import ListItem
from .permission import Permission
from .item_retention_label import ItemRetentionLabel
from .subscription import Subscription
from .thumbnail_set import ThumbnailSet
from .drive_item_version import DriveItemVersion
from .workbook import Workbook

