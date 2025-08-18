
### Formats
- **CSV (`.csv`)**: Used for raw ingested data.  
  - Human-readable, easy to share.  
  - Stored in `data/raw/` with timestamped filenames:  
    ```
    sample_YYYYMMDD-HHMMSS.csv
    ```
- **Parquet (`.parquet`)**: Used for processed datasets.  
  - Compressed, columnar storage, efficient for analytics.  
  - Stored in `data/processed/` with matching timestamped filenames:  
    ```
    sample_YYYYMMDD-HHMMSS.parquet
    ```

### Environment Usage
- A timestamp helper (`ts()`) ensures unique filenames per run.  
- Saving to Parquet requires a parquet engine:
  - Either [`pyarrow`](https://arrow.apache.org/docs/python/) or [`fastparquet`](https://fastparquet.readthedocs.io/).  
  - Install with:
    ```bash
    pip install pyarrow fastparquet
    ```
    or the conda equivalents.

---

## ✅ Validation Checks & Assumptions

### Validation
- DataFrames are checked against **expected column sets** before being stored (e.g., `['date', 'adj_close']`).  
- Missing or misnamed columns trigger validation errors early.  
- Both CSV and Parquet outputs inherit the same validated schema.

### Assumptions
1. **File Paths Exist**: `data/raw/` and `data/processed/` directories exist (created automatically if missing).  
2. **Timestamped Naming**: Each run generates a unique file, preventing overwriting of prior results.  
3. **Engine Availability**: At least one parquet engine (`pyarrow` or `fastparquet`) is installed and compatible with the environment. If not, the CSV version is still always saved.  
4. **Schema Consistency**: Assumes downstream tasks expect the validated column schema.  
5. **Index Handling**: Index is excluded when saving to disk (`index=False`) to keep outputs clean.
