import requests
def download_modis_ndvi(lat, lon, date, product="MOD13Q1"):
    """
    Fetch NDVI grid from ORNL Subset API by expanding tile size (3x3 km).
    """
    base_url = "https://modis.ornl.gov/rst/api/v1"
    endpoint = f"{base_url}/{product}/subset"

    params = {
        "latitude": lat,
        "longitude": lon,
        "startDate": date,
        "endDate": date,
        "kmAboveBelow": 1,
        "kmLeftRight": 1
    }

    print(f"🔍 Trying expanded fetch for {lat}, {lon} on {date}...")
    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        output_path = f"data/ndvi_grid_{lat}_{lon}_{date}.json"
        with open(output_path, "w") as f:
            f.write(response.text)
        print(f"✅ Grid NDVI data saved to {output_path}")
        return output_path
    else:
        print(f"❌ Fetch failed: {response.status_code}\n{response.text}")
        return None
