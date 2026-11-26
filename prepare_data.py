"""Download Allen Brain Cell Atlas MERFISH cells for one brain division."""

import argparse
from pathlib import Path
import pandas as pd

URL = ("https://allen-brain-cell-atlas.s3.us-west-2.amazonaws.com/"
       "metadata/MERFISH-C57BL6J-638850-CCF/20231215/views/"
       "cell_metadata_with_parcellation_annotation.csv")

COLUMNS = [
    "cell_label", "brain_section_label", "x_section", "y_section",
    "neurotransmitter", "class", "subclass", "parcellation_division",
    "parcellation_structure",
]

parser = argparse.ArgumentParser(description="Download MERFISH cells for one brain division")
parser.add_argument("--division", default="MB",
                    help="CCF division to keep (default MB = midbrain; e.g. HPF, TH, STR)")
parser.add_argument("--out", default="data/midbrain_cells.parquet", help="Output Parquet path")
args = parser.parse_args()

print(f"Streaming cell table from AWS (~1.6GB, this will take a few minutes.)")
kept=[]
total=0
for chunk in pd.read_csv(URL, usecols=COLUMNS, chunksize=500_000,
                         dtype={"neurotransmitter": "string"}):
    total += len(chunk)
    kept.append(chunk[chunk["parcellation_division"] == args.division])
    print(f"   read {total:,} cells", end="\r")

cells = pd.concat(kept, ignore_index=True)
if cells.empty:
    raise SystemExit(f"no Cells found for division '{args.division}'.")

out = Path(args.out)
out.parent.mkdir(parents=True, exist_ok=True)
cells.to_parquet(out, index=False)
print(f"\nSaved {len(cells):,} {args.division} cells to {out}")

