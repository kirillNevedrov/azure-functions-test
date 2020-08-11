import requests
from multiprocessing.dummy import Pool


def get_pi(digits):
    try:
        response = requests.get(
            f'https://kirill-nevedrov-test-function-3.azurewebsites.net/api/DigitsOfPi?digits={digits}')

        if response.status_code != 200:
            print(
                f'get_pi failed with status {response.status_code}')
            return None
        else:
            return response.text
    except:
        return None


def run():
    digits = list(range(5000, 6000))

    with Pool(1000) as pool:
        tickers_metadata = pool.map(get_pi, digits)


if __name__ == "__main__":
    run()
