#Purpose: Transforms raw ad data (e.g., calculates CTR) and outputs it as a CSV.

import json
import pandas as pd
import os

def transform_ads_data(input_path='mock_data/ads_sample.json', output_path='mock_data/ads_transformed.csv'):
    # Load raw JSON ad data from the mock input file
    with open(input_path, 'r') as f:
        raw_data = json.load(f)

    # Normalize the JSON structure into a pandas DataFrame
    if isinstance(raw_data, list):
        df = pd.DataFrame(raw_data)
    else:
        df = pd.DataFrame([raw_data])

    # Calculate Click-Through Rate (CTR)
    df['ctr'] = df['clicks'] / df['impressions']

    # Save the transformed data to a CSV file
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Transformed data written to {output_path}")

# Run the transformation if the script is executed directly
if __name__ == '__main__':
    transform_ads_data()