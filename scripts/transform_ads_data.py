import json
import pandas as pd
import os

def transform_ads():
    raw_path = os.path.join("mock_data", "ads_data.json")
    output_path = os.path.join("processed_data", "ads_transformed.csv")

    try:
        # Load raw JSON data
        with open(raw_path, 'r') as f:
            ads_data = json.load(f)

        df = pd.DataFrame(ads_data)

        # Basic transformation: Add CTR and CPC
        df["ctr"] = df["clicks"] / df["impressions"]
        df["cpc"] = df["spend"] / df["clicks"]

        # Optional: Round the new columns
        df["ctr"] = df["ctr"].round(4)
        df["cpc"] = df["cpc"].round(2)

        # Save to CSV
        os.makedirs("processed_data", exist_ok=True)
        df.to_csv(output_path, index=False)
        print(f"✅ Transformed data written to {output_path}")

    except Exception as e:
        print(f"❌ Transformation failed: {e}")

# To allow direct execution for local testing
if __name__ == "__main__":
    transform_ads()