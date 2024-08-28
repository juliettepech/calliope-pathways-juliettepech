from pathlib import Path

import calliope
import calliope_pathways

OUTPUT_PATH = "outputs/"

calliope.set_log_verbosity("INFO")

# Initialise
model = calliope_pathways.models.italy(scenario="scenario_nuclear")

# Build
model.build()

# Solve
model.solve(solver="gurobi")

# Store
output_path = Path(".") / "outputs" / "test"
output_path.mkdir(parents=True, exist_ok=True)

model.to_netcdf(output_path / "data.nc")  # Saves a single file
model.to_csv(
    output_path / "csv_files", allow_overwrite=True
)  # Saves a file for each xarray DataArray
