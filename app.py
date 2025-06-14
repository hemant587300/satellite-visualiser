from flask import Flask, render_template, request, send_from_directory
import os
import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize
from PIL import Image
import rasterio
from werkzeug.utils import secure_filename
from datetime import datetime
import re

app = Flask(__name__)
OUTPUT_FOLDER = "output"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = OUTPUT_FOLDER

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    lat = float(request.form.get("latitude"))
    lon = float(request.form.get("longitude"))

    uploaded_files = request.files.getlist("files")
    overlays = []

    for file in uploaded_files:
        if file.filename.endswith(".tif"):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(file_path)

            try:
                with rasterio.open(file_path) as src:
                    ndvi_data = src.read(1).astype(np.float32)
                    ndvi_data[ndvi_data == src.nodata] = np.nan

                ndvi_scaled = (ndvi_data - np.nanmin(ndvi_data)) / (np.nanmax(ndvi_data) - np.nanmin(ndvi_data))
                cmap = cm.get_cmap("YlGn", 256)
                norm = Normalize(vmin=0, vmax=1)
                rgba = (cmap(norm(ndvi_scaled)) * 255).astype(np.uint8)

                overlay_filename = f"overlay_{filename.replace('.tif', '')}.png"
                overlay_path = os.path.join(OUTPUT_FOLDER, overlay_filename)
                image = Image.fromarray(rgba, mode="RGBA")
                image.save(overlay_path)

                # 🔽 Enhance: Format filename into a readable date label
                raw_label = filename.replace(".tif", "")
                match = re.search(r"(\d{4})-(\d{2})-(\d{2})", raw_label)
                if match:
                    date_obj = datetime.strptime(match.group(0), "%Y-%m-%d")
                    readable_date = date_obj.strftime("%d %b %Y")
                else:
                    readable_date = raw_label  # fallback

                overlays.append({
                    "date": readable_date,
                    "file": overlay_filename,
                    "bounds": [[lat - 0.05, lon - 0.05], [lat + 0.05, lon + 0.05]]
                })

            except Exception as e:
                print(f"❌ Failed to process {filename}: {e}")
    
    if not overlays:
        return "<p style='color:red'>❌ No valid NDVI overlays were generated.</p>"

    return render_template("result_slider.html", overlays=overlays, lat=lat, lon=lon)

@app.route("/output/<path:filename>")
def output_file(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)
