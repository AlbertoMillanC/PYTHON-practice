import calendar
from pathlib import Path

month = list(calendar.month_name [1:])
day = list['monday','thursday','wednesday','tuesday','friday','saturday','sunday']
for i,month in enumerate(month):
    for day_name in day:
    
     Path(f'2022/{i+1}.{month}/{day_name}').mkdir(parents=True, exist_ok=True)








       