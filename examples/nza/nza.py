from pathlib import Path

import pandas as pd

import pandas_profiling

if __name__ == "__main__":
    df = pd.read_csv(
        "https://www.opendisdata.nl/download/csv/01_DBC.csv", low_memory=False
    )
    df["JAAR"] = pd.to_datetime(df["JAAR"], format="%Y")

    profile = df.profile_report(title="NZa")
    profile.to_file(output_file=Path("./nza_report.html"))
