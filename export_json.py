import pandas as pd
import json

df = pd.read_csv("retail_sales.csv")
records = df.to_dict(orient="records")

with open("data.js", "w", encoding="utf-8") as f:
    f.write("// Retail Sales Dataset (500 records)\n")
    f.write("const RAW_SALES_DATA = ")
    json.dump(records, f, indent=2)
    f.write(";\n")

print(f"Exported {len(records)} records to data.js")
