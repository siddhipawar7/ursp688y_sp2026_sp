# Exercise04: Ride On Reimagined Transit Equity Project

## Project Question

The full project asks:

> Did Ride On Reimagined produce larger scheduled service gains in higher-transit-need neighborhoods than in lower-transit-need neighborhoods?

Exercise04 starts the project by building the scheduled-service side of the analysis. The notebook asks:

> How did scheduled Ride On service at the stop level change between the pre-implementation January 2025 GTFS feed and the first post-implementation June 2025 GTFS feed?

## Why This Is The Starting Point

The final analysis will combine three pieces:

1. GTFS scheduled service change.
2. ACS-based tract-level transit need indicators.
3. Census tract geography for spatial aggregation.

The notebook in this folder operationalizes the first piece. It creates stop-level service metrics that can later be joined to tract geography and compared with a Transit Need Index.

## Data Status

The project data folder is being prepared as the main data foundation, not just as a small exercise sample.

Ready:

- Official Ride On GTFS snapshots from 2024, 2025, and the published May 2026 feed.
- Processed stop-level service metrics for each GTFS snapshot.
- Processed stop-level service change files for the main comparison periods.
- 2024 Montgomery County Census tract boundaries from TIGER/Line.
- ACS 2024 tract indicators and Transit Need Index outputs.

## Main Comparison Used In Exercise04

The Exercise04 notebook uses:

- Pre feed: `rideon_2025_january.zip`
- Post feed: `rideon_2025_june.zip`

These are useful because the January 2025 feed is the main pre-Phase 1 baseline and the June 2025 feed begins the first post-implementation schedule period.

## Data Sources

Ride On GTFS:

https://www.montgomerycountymd.gov/department-transportation/about-mcdot/divisions/transit-services/current-archived-gtfs-files-transit-services

TIGER/Line tract boundaries:

https://www2.census.gov/geo/tiger/TIGER2024/TRACT/tl_2024_24_tract.zip

ACS API:

https://api.census.gov/data/2024/acs/acs5.html

## Folder Structure

```text
exercises/exercise04/emmanuel
├── ReadMe.md
├── exercise04_emmanuel.ipynb
├── final_project_analysis_emmanuel.ipynb
├── gtfs_service_metrics.py
├── final_project_analysis.py
├── prepare_project_data.py
├── data
│   ├── project_data_catalog.csv
│   ├── raw
│   │   ├── gtfs
│   │   ├── acs
│   │   └── tiger
│   └── processed
│       ├── gtfs
│       ├── acs
│       ├── geography
│       └── final_analysis
└── figures
    └── final_analysis
```