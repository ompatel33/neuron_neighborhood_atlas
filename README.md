# Neuron Neighborhood Atlas
A reusable Python tool to measure the cellular neighborhood around user-selected cell types in brain tissue. This program uses spatial transcriptomics data, which identifies the position and molecular identities of every cell in a given brain section.

## How it works:
1. Loads each cell as a GeoPandas point (coorindates are in μm)
2. Buffers every target cell by a chosen radius and spatially joins the surrounding cells.
3. Comparisons between neighbor compositions are assessed with a permutation test.
4. Region outlines are drawn by dissolving buffered cells, exporting maps, tables, and GeoPackage.

## Usage:
Requires pandas, geopandas, pyarrow, scipy, and matplotlib
python prepare_data.py runs program
python neighborhood.py runs program

User options: `--regions`, `--target-column`, `--target-value`, `--neighbor-level`, `--radius`,
`--sections`, `--permutations`, `--outdir`.
Run `python neighborhood.py -h` for details.

## Data:
Allen Brain Cell Atlas, MERFISH-C57BL6J-638850 (Yao et al., 2023), CC BY-NC 4.0.
Healthy adult mouse tissues describing cellular environments of the brain.
