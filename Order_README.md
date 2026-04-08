# python
Order_ingestion.py

Order_ingestion.py - credits KodeKloud

This script is a simple “data ingestion pipeline” for an orders CSV file.
At a high level, it:

Sets up a folder structure.
Finds a file whose name contains "orders" in the data/ folder.
Checks whether this file was already ingested (using a log).
Loads the CSV and validates its schema (expected columns).
Saves a cleaned copy into an insights/ folder organized by month.
Moves the original file into an archive/ folder.
Logs what happened (status, row count, timestamp).

Summary
This script demonstrates a simple but realistic ingestion workflow:

Setup: Create folders and define paths.

Detection: Find the latest orders file.

Safety: Check a log to avoid duplicate processing.

Validation: Confirm the data schema matches expectations.

Processing: Save a clean copy into a structured insights/ folder.

Archiving: Move raw input into archive/.

Auditing: Record what happened in a CSV log.
