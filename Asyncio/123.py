from pprint import pprint as print
import requests
import httpx
import asyncio


class ExchangeRates:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    async def __init__(self) -> None:
        if ExchangeRates._initialized:
            return

        self.data = self.fetch_from_api()
        ExchangeRates._initialized = True

    @staticmethod
    async def fetch_from_api() -> dict:
        async with httpx.AsyncClient() as client:
            response = await client.get("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=UAH&apikey=PASTE_YOUR_API_KEY")
            print(response)
            return response.json()


async def main():
    er = ExchangeRates()
    await er.fetch_from_api()
    print(er.data)


if __name__ == "__main__":
    asyncio.run(main())
# er = ExchangeRates()
# er = object.__new__(ExchangeRates)
# er <= ExchangeRates.__init__() <= ExchangeRates.__new__()


# print(er.data)
# er2 = ExchangeRates()
# er2 = ExchangeRates()
# er2 = ExchangeRates()
# er2 = ExchangeRates()
# er2 = ExchangeRates()
# print(er2.data)