#!/usr/bin/python3

# Import packages

import os
import pandas as pd
import shutil 
from datetime import datetime

# Define folders and paths 

data_folder = "data"
archive_folder = os.path.join(data_folder, "archive")
insights_folder = "insights"
logs_folder = "logs"
log_path = os.path.join(logs_folder, "ingest_log.csv")

# Create folders if they don't exist
for folder in data [data_folder
