
# https://www.saltycrane.com/blog/2009/05/converting-time-zones-datetime-objects-python/

from datetime import datetime
from pytz import timezone

fmt = "%Y-%m-%d %H:%M:%S %Z%z"

# Current time in UTC
now_utc = datetime.utcfromtimestamp(1547314660)    
# now_utc = datetime.now(timezone('UTC'))
print(now_utc.strftime(fmt))

# Convert to US/Pacific time zone
now_pacific = now_utc.astimezone(timezone('US/Pacific'))
print(now_pacific.strftime(fmt))

# Convert to Europe/Berlin time zone
now_berlin = now_pacific.astimezone(timezone('Europe/Berlin'))
print(now_berlin.strftime(fmt))

# Convert to America/Sao Paulo time zone
now_saoPaulo = now_utc.astimezone(timezone('America/Sao_Paulo'))
print(now_saoPaulo)
print(now_saoPaulo.strftime(fmt))