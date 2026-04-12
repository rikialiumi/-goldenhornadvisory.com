import urllib.request
import json
import sys
from datetime import datetime

def fetch_turkey_trade_data(commodity_code=None, year=2024, flow='X'):
    base_url = "https://comtradeapi.un.org/public/v1/preview/C/A/HS"
    params = f"?reporterCode=792&period={year}&flowCode={flow}"
    if commodity_code:
        params += f"&cmdCode={commodity_code}"
    params += "&partnerCode=0&partner2Code=0&customsCode=C00&motCode=0"
    url = base_url + params
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'GoldenHornAdvisory/1.0'})
        with urllib.request.urlopen(req, timeout=30) as response:
            data = json.loads(response.read().decode())
            return data
    except Exception as e:
        return {"error": str(e)}

def fetch_textiles():
    print("Fetching Turkey textile exports (HS 61-62)...")
    data = fetch_turkey_trade_data(commodity_code='61', year=2024, flow='X')
    output = f"golden-horn/research/comtrade-textiles-{datetime.now().strftime('%Y-%m-%d')}.json"
    with open(output, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Saved to {output}")
    return data

def fetch_food():
    print("Fetching Turkey food exports (HS 07-21)...")
    data = fetch_turkey_trade_data(commodity_code='07', year=2024, flow='X')
    output = f"golden-horn/research/comtrade-food-{datetime.now().strftime('%Y-%m-%d')}.json"
    with open(output, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Saved to {output}")
    return data

def fetch_building():
    print("Fetching Turkey building materials exports (HS 68-70)...")
    data = fetch_turkey_trade_data(commodity_code='69', year=2024, flow='X')
    output = f"golden-horn/research/comtrade-building-{datetime.now().strftime('%Y-%m-%d')}.json"
    with open(output, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Saved to {output}")
    return data

if __name__ == "__main__":
    if len(sys.argv) > 1:
        sector = sys.argv[1]
        if sector == "textiles":
            fetch_textiles()
        elif sector == "food":
            fetch_food()
        elif sector == "building":
            fetch_building()
    else:
        print("Fetching all sectors...")
        fetch_textiles()
        fetch_food()
        fetch_building()
