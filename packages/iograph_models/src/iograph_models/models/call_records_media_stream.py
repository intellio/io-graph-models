from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class CallRecordsMediaStream(BaseModel):
	audioCodec: Optional[CallRecordsAudioCodec] = Field(default=None,alias="audioCodec",)
	averageAudioDegradation: Optional[float] | Optional[str] | ReferenceNumeric
	averageAudioNetworkJitter: Optional[str] = Field(default=None,alias="averageAudioNetworkJitter",)
	averageBandwidthEstimate: Optional[int] = Field(default=None,alias="averageBandwidthEstimate",)
	averageFreezeDuration: Optional[str] = Field(default=None,alias="averageFreezeDuration",)
	averageJitter: Optional[str] = Field(default=None,alias="averageJitter",)
	averagePacketLossRate: Optional[float] | Optional[str] | ReferenceNumeric
	averageRatioOfConcealedSamples: Optional[float] | Optional[str] | ReferenceNumeric
	averageReceivedFrameRate: Optional[float] | Optional[str] | ReferenceNumeric
	averageRoundTripTime: Optional[str] = Field(default=None,alias="averageRoundTripTime",)
	averageVideoFrameLossPercentage: Optional[float] | Optional[str] | ReferenceNumeric
	averageVideoFrameRate: Optional[float] | Optional[str] | ReferenceNumeric
	averageVideoPacketLossRate: Optional[float] | Optional[str] | ReferenceNumeric
	endDateTime: Optional[datetime] = Field(default=None,alias="endDateTime",)
	isAudioForwardErrorCorrectionUsed: Optional[bool] = Field(default=None,alias="isAudioForwardErrorCorrectionUsed",)
	lowFrameRateRatio: Optional[float] | Optional[str] | ReferenceNumeric
	lowVideoProcessingCapabilityRatio: Optional[float] | Optional[str] | ReferenceNumeric
	maxAudioNetworkJitter: Optional[str] = Field(default=None,alias="maxAudioNetworkJitter",)
	maxJitter: Optional[str] = Field(default=None,alias="maxJitter",)
	maxPacketLossRate: Optional[float] | Optional[str] | ReferenceNumeric
	maxRatioOfConcealedSamples: Optional[float] | Optional[str] | ReferenceNumeric
	maxRoundTripTime: Optional[str] = Field(default=None,alias="maxRoundTripTime",)
	packetUtilization: Optional[int] = Field(default=None,alias="packetUtilization",)
	postForwardErrorCorrectionPacketLossRate: Optional[float] | Optional[str] | ReferenceNumeric
	rmsFreezeDuration: Optional[str] = Field(default=None,alias="rmsFreezeDuration",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)
	streamDirection: Optional[CallRecordsMediaStreamDirection] = Field(default=None,alias="streamDirection",)
	streamId: Optional[str] = Field(default=None,alias="streamId",)
	videoCodec: Optional[CallRecordsVideoCodec] = Field(default=None,alias="videoCodec",)
	wasMediaBypassed: Optional[bool] = Field(default=None,alias="wasMediaBypassed",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .call_records_audio_codec import CallRecordsAudioCodec
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .call_records_media_stream_direction import CallRecordsMediaStreamDirection
from .call_records_video_codec import CallRecordsVideoCodec

