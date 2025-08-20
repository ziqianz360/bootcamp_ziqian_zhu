### Problem Statement
- A grocery chain struggles with frequent stockouts and overstocking of perishable goods, leading to lost sales and waste. Current ordering relies heavily on manager intuition. Accurate demand forecasts for key SKUs could reduce waste and improve availability.

### Stakeholder & User
- Decision-makers: Supply Chain Director, Category Managers
- Primary users: Store managers, replenishment planners
- Workflow context: Forecasts generated overnight and integrated into the store ordering system by 6 AM daily. Forecast horizon: 1–14 days.

### Useful Answer
- Time-series forecast for daily demand per SKU/store. Decision: quantity to order. Metric: forecast MAPE, waste reduction %, sales uplift.

### Assumptions & Constraints
- Historical sales, promotions, and weather data available
- Latency: overnight batch acceptable
- Perishability means forecast horizon <14 days

### Known Unknowns / Risks
- Unpredictable spikes from local events
- Supplier delivery constraints
- New product introductions with no sales history

### Lifecycle Mapping
- Goal A: Reduce waste & stockouts → Problem Framing & Scoping (Stage 01) → Problem definition document (this)
- Goal B: Build forecasting prototype → Data Exploration & Model Development (Stage 02) → MVP forecast model tested on historical data
- Goal C: Integrate into ordering workflow → Deployment & Monitoring (Stage 03) → Productionized forecasting pipeline with dashboard monitoring

## 📂 Data Storage

This project uses a clear folder structure to separate **raw** input data from **processed** datasets:


### File Formats
- **Raw data**: stored as `.csv` in `data/raw/`  
  - Example: `sample_YYYYMMDD-HHMMSS.csv`  
  - Human-readable, easy to inspect manually.  
- **Processed data**: stored as `.parquet` in `data/processed/`  
  - Example: `sample_YYYYMMDD-HHMMSS.parquet`  
  - Efficient columnar format for analytics and downstream workflows.  

At least one raw file (CSV or Parquet) should exist in `data/raw/` to validate the pipeline.  

---

### How the Code Reads Data
Code modules expect to load data using the paths defined in environment variables. For example:

```python
import os
import pandas as pd

# Load base data directory from environment
DATA_DIR = os.getenv("DATA_DIR", "./data")   # defaults to ./data if not set

RAW_DIR = os.path.join(DATA_DIR, "raw")
PROC_DIR = os.path.join(DATA_DIR, "processed")

# Example: read the latest raw file
df = pd.read_csv(os.path.join(RAW_DIR, "sample_20250818-141530.csv"))

## Data Cleaning

The data cleaning process ensures that missing values and inconsistent
scales are handled before analysis or modeling. Our approach includes:

-   **Filling Missing Values**\
    Missing values in numeric columns are replaced with the column
    median. This preserves the overall distribution while minimizing the
    influence of outliers.

-   **Dropping Excessive Missing Data**\
    Rows or columns are removed if the proportion of missing values
    exceeds a specified threshold (default 50%). This helps eliminate
    sparse data that could bias results.

-   **Normalizing Numeric Data**\
    Selected numeric columns are normalized to improve comparability
    across features. Two methods are supported:

    -   *Min--Max Scaling*: rescales values to the range \[0, 1\].\
    -   *Z-Score Standardization*: centers values to mean 0 with unit
        variance.

Non-numeric and identifier fields (e.g., `zipcode`, `city`) are left
unchanged during cleaning.
