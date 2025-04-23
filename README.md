📄 requirements.txt
txt
geocoder
requests
rich
Add more if needed (like tkinter or flask, depending on your UI or web interface).

📘 README.md
md
# 🌍 GeoLocator

**GeoLocator** is a lightweight Python-based IP geolocation tool. You can locate any public IP address and retrieve detailed information such as country, city, coordinates, ISP, and more.

---

## ✨ Features

- 🔍 Locate any IP address
- 🌐 Auto-detect your own IP
- 🧭 Get GPS coordinates, region, country, ISP & timezone
- 🎨 Pretty CLI output using Rich

---

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
🚀 Usage
Run the script with Python:

bash
python geolocator.py
You’ll be prompted to enter an IP address. You can also use your own by leaving the input blank.

🛠 Example Output
csharp
[IP] 8.8.8.8
[Country] United States
[City] Mountain View
[Region] California
[ISP] Google LLC
[Latitude] 37.386
[Longitude] -122.0838
[Timezone] America/Los_Angeles
💡 Notes
Requires internet connection.

Uses geocoder with default providers (IPinfo, ip-api, or similar).

For better accuracy and more detailed data, consider using a paid API key.

📂 Project Structure
GeoLocator/
├── geolocator.py
├── requirements.txt
└── README.md
🧑‍💻 Author
Made by Simit
Instagram: https://www.instagram.com/Redsimit
YouTube: https://www.youtube.com/@redsimitofficial
