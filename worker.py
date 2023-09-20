import requests

ETHERSCAN_API_KEY = "SAWPNIM5KKPSQXRS28YA12B25SU1E3D3IF"
RESERVE_ADDRESS = "0x1E91bB97e4DEdb4923c3e499fEcDC6aeAf14ca74"


def get_all_eth_from_address(address, start):
    # Construct the Etherscan API URL
    url = (
        f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&apikey={ETHERSCAN_API_KEY}"
        f"&sort=asc&startblock={start}"
    )
    # Make the GET request
    response = requests.get(url)
    response.raise_for_status()
    # Parse the response
    # if r.status_code == 200 and r.json()['message'] == 'OK':

    data = response.json()
    transactions = data["result"]
    result = []

    for trans in transactions:
        if trans["to"].lower() == address.lower():
            result.append(trans)

            print(trans["hash"])
            print(trans["value"])
            print(trans["blockNumber"])
            print("-" * 80)
    return result


pp = get_all_eth_from_address(RESERVE_ADDRESS, 0)

print(pp)
