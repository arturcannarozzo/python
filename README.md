# python
scanner.py
python ip scanner
all credits Tcm Security Academy - Python 100 free course
https://academy.tcm-sec.com/p/programming-100-fundamentals
-----------------------------------------------------------------
Order_ingestion.py
This script is a simple “data ingestion pipeline” for an orders CSV file.

At a high level, it:

Sets up a folder structure.
Finds a file whose name contains "orders" in the data/ folder.
Checks whether this file was already ingested (using a log).
Loads the CSV and validates its schema (expected columns).
Saves a cleaned copy into an insights/ folder organized by month.
Moves the original file into an archive/ folder.
Logs what happened (status, row count, timestamp).
