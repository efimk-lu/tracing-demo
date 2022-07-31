from dataclasses import dataclass
from datetime import datetime
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass(frozen=True)
class PingData:
    exact_time: datetime = datetime.now()
