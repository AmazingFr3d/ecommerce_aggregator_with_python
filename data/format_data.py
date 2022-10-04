from functions import run
import pandas as pd

import json


def format_data(keyword):
    data = run.main(keyword)
    site1 = data[0]
    site2 = data[1]
    combined = pd.concat([site1, site2], ignore_index=True)
    sorted_data = combined.sort_values(by='price')
    sorted_data = sorted_data[:30]

    return sorted_data


keyword = "Raspberry Pi 4"

sorted_data = format_data(keyword)

file = keyword.replace(" ", "_")
fname = f"{file}_data.json"

sorted_data.to_json(fname, orient='split', index=False)
