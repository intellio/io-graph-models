from __future__ import annotations
from enum import Enum


class AllowedLobbyAdmitterRoles(Enum):
	organizerAndCoOrganizersAndPresenters = "organizerAndCoOrganizersAndPresenters"
	organizerAndCoOrganizers = "organizerAndCoOrganizers"
	unknownFutureValue = "unknownFutureValue"

