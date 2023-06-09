from pathlib import Path

import pandas as pd  # pip install pandas

# Define & create output directory
output_dir = Path(__file__).parent / "output"
output_dir.mkdir(parents=True, exist_ok=True)

# Define Excel file path
excel_file = Path(__file__).parent / "NV.xlsx"

df = pd.read_excel(excel_file)
column_name = "NAME_VILLAGE"
replace_symbols = ['>', '<', ':', '"', '/', '\\\\', '\|', '\?', '\*']
df[column_name] = (
    df[column_name].replace(replace_symbols, '', regex=True).str.strip().str.title()
)
unique_values = df[column_name].unique()

for unique_value in unique_values:
    df_output = df[df[column_name].str.fullmatch(unique_value)]
    output_path = output_dir / f"{unique_value}.xlsx"
    df_output.to_excel(output_path, sheet_name=unique_value[:31], index=False)
