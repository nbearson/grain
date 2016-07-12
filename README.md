Grain is a super simple UTC<->TAI conversion package, made specifically for handling pesky leap seconds.

Requires:
 * setuptools
 * updates when new leap second files come out

Example usage:
```python
from grain import Grain
from datetime import datetime
g = Grain()
now = datetime.utcnow()
unix = datetime(1970, 1, 1)
seconds_since_unix_epoch = g.utc2tai(now, unix)
```
