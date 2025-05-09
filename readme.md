# 📍 Phone Location Tracker

A Python script that retrieves a phone number's geographical location and service provider details, then generates an interactive HTML map showing the estimated location.

## 🛠 Features
✅ Extracts country and service provider information from a phone number
✅ Fetches precise location data using OpenCage Geocode API
✅ Displays geographical details including city, state, country, and coordinates
✅ Generates an interactive map (`mylocation.html`) with:
   - A marker for the estimated location
   - A circle indicating an approximate area
   - A bounding box for the possible location range

## 📦 Requirements
Before running the script, ensure you have the following installed:

- Python 3.x
- Required libraries:
  ```sh
  pip install phonenumbers folium opencage
  ```
- OpenCage API Key (Get it from [OpenCage](https://opencagedata.com/api))

## 🚀 Usage
1. **Download the script** from this repository.
2. **Replace the OpenCage API key** in the script with your own key.
3. **Run the script**:
   ```sh
   python phone_tracker.py
   ```
4. **Enter the phone number** in international format (e.g., `+254123456789`).
5. The script will:
   - Retrieve the location details
   - Display information in the console
   - Generate an interactive map (`mylocation.html`)
6. **Open `mylocation.html` in your browser** to view the location map.

## 🔍 Example Output
```
Phone Number Location Tracker
============================
Enter phone number with country code (e.g., +254123456789): +254712345678

Country Location: Kenya
Service Provider: Safaricom
Coordinates: -1.286389, 36.817223
Map has been saved as 'mylocation.html'
```

## ⚠️ Disclaimer
This script **does not provide real-time tracking**. It uses phone number prefixes to estimate location and carrier details. The accuracy of the location depends on the phone number's registered region and the OpenCage API data.

## 📝 Contributing
Feel free to fork the repository, make improvements, and submit a pull request!

🌍 **Tip:** Ensure your OpenCage API key is active and has sufficient quota to retrieve location data!

