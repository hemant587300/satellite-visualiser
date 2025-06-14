# 🌿 Satellite NDVI Time-Series Viewer

A lightweight web application to **visualize, compare, and export NDVI satellite imagery over time**. This tool helps in environmental monitoring, crop analysis, and urban vegetation tracking using NDVI GeoTIFF files.

---

## 🚀 Features

✅ Upload and visualize multiple NDVI GeoTIFFs  
✅ Leaflet-based interactive map with overlays  
✅ Time-series slider to switch between dates  
✅ Opacity control to compare with base map  
✅ NDVI statistics (mean, min, max) per layer  
✅ Export full map view as **PNG** with metadata  
✅ Toggle overlays, auto-play time-series, download images

---

## 🛠️ Tech Stack

| Component      | Technology Used              |
|----------------|------------------------------|
| Backend        | Python Flask                 |
| Frontend       | HTML, CSS, JS, Leaflet.js    |
| Image Handling | rasterio, PIL, matplotlib    |
| Visualization  | Leaflet Map + Slider         |
| Export         | html2canvas, leaflet-image   |

---

## 📂 Project Structure

```
📦 satellite-ndvi-viewer/
├── app.py                  # Flask app logic
├── templates/
│   ├── index.html          # Upload and search UI
│   └── result_slider.html  # Interactive map UI
├── static/ (optional)
│   └── custom.js/css       # (if added later)
├── output/
│   ├── *.tif               # NDVI GeoTIFF uploads
│   ├── *.png               # Generated overlays
│   └── ndvi_web_map.html   # Downloadable static map
└── README.md               # Project guide
```

---

## 🧪 How to Use

1. 🔼 Upload multiple NDVI `.tif` GeoTIFF files via the form  
2. 📍 Select city, click on map or search for a place  
3. 🚀 Click "Fetch & View NDVI Map"  
4. 🕹️ Use slider to switch dates  
5. 🎛️ Adjust opacity or play timeline  
6. 📊 View NDVI stats below map  
7. 📸 Use **Export as Image** to download final PNG

---

## 📸 Sample Screenshots

| UI | Exported Map |
|----|---------------|
| ![Slider UI](output/sample_slider_ui.png) | ![Export PNG](output/exported_png_sample.png) |

---

## 🧠 Future Enhancements

- Google Earth Engine Integration for live NDVI  
- Region selection and zonal statistics  
- Download GeoTIFF outputs  
- ML-based vegetation classification

---

## 📜 License

MIT License

---

## 🙏 Acknowledgements

- NASA MODIS & EarthData APIs  
- Leaflet.js and html2canvas  
- rasterio & matplotlib  
- Your efforts and contribution!

---

> Created with ❤️ by Hem Pathak  
> Final Year BTech CSE, Amity University Mumbai  
> Project Aligned with ISRO 🌏
