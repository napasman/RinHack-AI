import datetime
from dataclasses import dataclass, field


@dataclass(frozen=True, kw_only=True)
class TrafficDTO:
    id: int | None = field(default=None)
    timestamp: str
    source_ip: str
    destination_ip: str
    protocol: str
    port: str
    packet_size: str
    prediction: str
