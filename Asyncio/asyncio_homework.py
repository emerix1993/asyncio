from pprint import pprint as print
import asyncio
import httpx


class ExchangeRates:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self) -> None:
        if ExchangeRates._initialized:
            return

        self.data = asyncio.run(self.fetch_from_api())
        self.data1 = asyncio.run(self.get_rate())

        ExchangeRates._initialized = True

    async def fetch_from_api(self):
        async with httpx.AsyncClient() as client:
            url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=UAH&apikey=PASTE_YOUR_API_KEY"
            response = await client.get(url)
            await asyncio.sleep(1)
            return response.json()

    async def get_rate(self):
        async with httpx.AsyncClient() as client:
            url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=EUR&apikey=PASTE_YOUR_API_KEY"
            response = await client.get(url)
            await asyncio.sleep(1)
            return response.json()


async def main():
    er = ExchangeRates()
    er.data, er.data1 = await asyncio.gather(er.fetch_from_api(), er.get_rate())
    print(er.data)
    print(er.data1)


if __name__ == "__main__":
    asyncio.run(main())
