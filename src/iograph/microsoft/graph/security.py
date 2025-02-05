# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-02-04T01:23:12+00:00

from __future__ import annotations

from enum import Enum


class BehaviorDuringRetentionPeriod(Enum):
    do_not_retain = 'doNotRetain'
    retain = 'retain'
    retain_as_record = 'retainAsRecord'
    retain_as_regulatory_record = 'retainAsRegulatoryRecord'
    unknown_future_value = 'unknownFutureValue'
