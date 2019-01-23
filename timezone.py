# setting.py
USE_TZ = True

# 避免RuntimeWarning: DateTimeField ModelName.field_name received a naive
# datetime (2012-01-01 00:00:00) while time zone support is active.
# 將USE_TZ = False
# 或用以下方法

from datetime import datetime
from pytz import timezone
TP = timezone('Asia/Taipei')
now = datetime.now(TP)
start_time = datetime(2019,2,20,10,14,0,0,tzinfo=TP)
