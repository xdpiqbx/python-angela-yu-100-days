import json
from pathlib import Path
from datetime import datetime as dt
date = dt.now().strftime("%d.%m.%Y %H:%M:%S")

with open(Path('./save.json'), 'w', encoding='utf-8') as json_file:
    json.dump({"save_date": date}, json_file, indent=4)

