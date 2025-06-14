import folium
import numpy as np
import json
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize
from PIL import Image
import os

# -------------------------------------------
# ✅ Step 0: Create a sample NDVI JSON
# -------------------------------------------
sample_ndvi_json = {
    "subset": [
        {
            "date": "2023-08-09",
            "band": "250m_16_days_NDVI",
            "grid": [
                [52, 78, 102],
                [89, 112, 96],
                [70, 82, 105]
            ]
        }
    ]
}

os.makedirs("data", exist_ok=True)
json_path = "data/ndvi_sample.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(sample_ndvi_json, f)

# -------------------------------------------
# ✅ Step 1: Load NDVI data from JSON
# -------------------------------------------
with open(json_path, "r", encoding="utf-8") as f:
    ndvi_data = json.load(f)

ndvi_grid = np.array(ndvi_data["subset"][0]["grid"])

# -------------------------------------------
# ✅ Step 2: Normalize NDVI values (-1 to +1)
# -------------------------------------------
ndvi_normalized = (ndvi_grid - 128) / 128.0  # 0–255 → -1 to +1

# -------------------------------------------
# ✅ Step 3: Apply colormap and save as RGBA PNG
# -------------------------------------------
cmap = cm.get_cmap("YlGn")
norm = Normalize(vmin=-1, vmax=1)
rgba_array = (cmap(norm(ndvi_normalized)) * 255).astype(np.uint8)

os.makedirs("output", exist_ok=True)
overlay_image_path = "output/ndvi_overlay.png"
Image.fromarray(rgba_array, mode="RGBA").save(overlay_image_path)

# -------------------------------------------
# ✅ Step 4: Create a Folium Map with overlay
# -------------------------------------------
latitude = 40.0150
longitude = -105.2705
m = folium.Map(location=[latitude, longitude], zoom_start=15)

folium.raster_layers.ImageOverlay(
    name="NDVI Overlay",
    image=overlay_image_path,
    bounds=[[latitude - 0.005, longitude - 0.005],
            [latitude + 0.005, longitude + 0.005]],
    opacity=0.6,
    interactive=True,
    cross_origin=False
).add_to(m)

folium.LayerControl().add_to(m)

# -------------------------------------------
# ✅ Step 5: Save the final map as HTML
# -------------------------------------------
final_html = "output/ndvi_map_with_overlay.html"
m.save(final_html)
print(f"✅ NDVI map saved to: {final_html}")
