# water-intel

A data tool that uses EPA public records to forecast 
which US water utilities are likely to purchase new 
equipment in the next 1-3 years.

## Background
Water utilities replace infrastructure on predictable 
cycles but this information is scattered across 
thousands of public records. This tool centralizes 
that data and turns it into a procurement forecast.

## Data Source
EPA Safe Drinking Water Information System (SDWIS)
Updated quarterly by the US government.
https://echo.epa.gov/tools/data-downloads

## How It Works
- load_data.py  — loads and cleans 50,000+ EPA records
- score.py      — scores each utility on age and size
- Output        — ranked list by procurement likelihood

## Tech Stack
Python, Pandas, EPA Public Data

## Author
Agatsya Patel
Data Analyst 
