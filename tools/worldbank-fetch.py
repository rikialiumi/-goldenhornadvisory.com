import urllib.request
import json
from datetime import datetime

def fetch(url):
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            data = json.loads(r.read().decode())
            return data[1] if len(data) > 1 else []
    except Exception as e:
        return {"error": str(e)}

def run_all():
    results = {
        'turkey_gdp_growth': fetch("https://api.worldbank.org/v2/country/TR/indicator/NY.GDP.MKTP.KD.ZG?format=json&mrv=5"),
        'turkey_trade_gdp': fetch("https://api.worldbank.org/v2/country/TR/indicator/NE.TRD.GNFS.ZS?format=json&mrv=5"),
        'eu_import_growth': fetch("https://api.worldbank.org/v2/country/EU/indicator/NE.IMP.GNFS.KD.ZG?format=json&mrv=5")
    }
    output = f"golden-horn/research/worldbank-{datetime.now().strftime('%Y-%m-%d')}.json"
    with open(output, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"Saved to {output}")
    return results

if __name__ == "__main__":
    run_all()
