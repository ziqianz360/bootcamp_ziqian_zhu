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