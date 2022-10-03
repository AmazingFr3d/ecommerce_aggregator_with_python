from functions import run
import pandas as pd

import json

keyword = "Arduino Uno"
data = run.main(keyword)

site1 = data[0]
site2 = data[1]
combined = pd.concat([site1, site2], ignore_index=True)

sorted_data = combined.sort_values(by='price')

sorted_data = combined.sort_values(by='price')

file = keyword.replace(" ", "_")
fname = f"{file}_data.json"

sorted_data.to_json(fname, orient='split', index=False)
