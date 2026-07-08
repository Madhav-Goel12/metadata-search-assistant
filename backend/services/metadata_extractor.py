import pandas as pd


def extract_metadata(file_info):
    """
    Extract metadata from a CSV file.

    Parameters
    ----------
    file_info : dict
        {
            database_name,
            table_name,
            file_path
        }

    Returns
    -------
    list[dict]
    """

    df = pd.read_csv(
    file_info["file_path"],
    low_memory=False
)

    metadata = []

    for column in df.columns:

        series = df[column]

        # Sample values
        samples = (
            series.dropna()
                  .astype(str)
                  .head(5)
                  .tolist()
        )

        # Numeric columns
        is_numeric = pd.api.types.is_numeric_dtype(series)

        # Datetime columns
        is_datetime = pd.api.types.is_datetime64_any_dtype(series)

        # Min / Max
        min_value = None
        max_value = None

        if is_numeric:

            min_value = series.min()

            max_value = series.max()

        metadata.append({

            "database_name": file_info["database_name"],

            "table_name": file_info["table_name"],

            "column_name": column,

            "data_type": str(series.dtype),

            "row_count": len(df),

            "null_count": int(series.isnull().sum()),

            "unique_count": int(series.nunique()),

            "sample_values": ", ".join(samples),

            "min_value": str(min_value),

            "max_value": str(max_value),

            "memory_usage": int(series.memory_usage(deep=True)),

            "is_numeric": is_numeric,

            "is_datetime": is_datetime,

            "file_path": str(file_info["file_path"])

        })

    return metadata