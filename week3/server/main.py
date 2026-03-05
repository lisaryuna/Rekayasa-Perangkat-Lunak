import sys
import logging
import httpx
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO, stream=sys.stderr, format='%(asctime)s - %(levelname)s - %(message)s')

# Inisialisasi server
mcp = FastMCP("Weather-Stats-Server")

BASE_URL = "https://api.open-meteo.com/v1/forecast"

@mcp.tool()
async def get_current_weather(latitude: float, longitude: float) -> str:
    """Mendapatkan data cuaca saat ini untuk lokasi spesifik berdasarkan koordinat."""
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True
    }
    try:
        # Menggunakan timeout 10 detik sebagai bentuk resilience
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(BASE_URL, params=params)
            response.raise_for_status() # Akan melempar error jika HTTP status bukan 200
            
            data = response.json()
            current = data.get("current_weather", {})
            return f"Cuaca saat ini: Suhu {current.get('temperature')}°C, Kecepatan angin {current.get('windspeed')} km/h."
            
    except httpx.TimeoutException:
        logging.error("Timeout saat menghubungi Open-Meteo API.")
        return "Error: Koneksi ke API cuaca terputus (Timeout). Silakan coba lagi nanti."
    except httpx.HTTPStatusError as e:
        logging.error(f"HTTP Error: {e.response.status_code}")
        return f"Error: Gagal mengambil data cuaca dari server API."
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return "Error: Terjadi kesalahan internal saat memproses data cuaca."

@mcp.tool()
async def get_temperature_stats(latitude: float, longitude: float, days: int = 3) -> str:
    """Mendapatkan tren/statistik suhu harian (maksimal dan minimal) untuk beberapa hari ke depan."""
    # Validasi input (resilience terhadap input tidak masuk akal / rate limit perlindungan)
    if days < 1 or days > 14:
        return "Error: Parameter 'days' harus antara 1 hingga 14 hari."

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": "temperature_2m_max,temperature_2m_min",
        "timezone": "auto",
        "forecast_days": days
    }
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(BASE_URL, params=params)
            response.raise_for_status()
            
            data = response.json()
            daily = data.get("daily", {})
            
            times = daily.get("time", [])
            temps_max = daily.get("temperature_2m_max", [])
            temps_min = daily.get("temperature_2m_min", [])
            
            result = [f"Statistik Suhu {days} Hari Kedepan:"]
            for t, t_max, t_min in zip(times, temps_max, temps_min):
                result.append(f"- Tanggal {t}: Max {t_max}°C, Min {t_min}°C")
            return "\n".join(result)
            
    except Exception as e:
        logging.error(f"Error pada get_temperature_stats: {str(e)}")
        return "Error: Gagal mengambil data statistik suhu."

if __name__ == "__main__":
    logging.info("Memulai Weather-Stats-Server di mode STDIO...")
    mcp.run(transport='stdio')