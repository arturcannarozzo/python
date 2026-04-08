Summary
This cleaning script turns raw ingested orders into a high‑quality dataset by:

Dropping rows with missing required data.

Dropping rows with invalid dates.

Validating numeric fields (IDs and quantities) and dropping invalids.

Removing duplicate orders.

Enforcing that all orders reference valid customers and products.

Saving:

orders_clean.csv – cleaned orders.

orders_dropped.csv – all orders that were removed, for traceability.

Together with the ingestion script, this forms a small but realistic data pipeline: ingest → validate schema → clean → enrich/analyze.
