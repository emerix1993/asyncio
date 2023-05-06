import asyncio
import httpx
from pprint import pprint as print


class ExchangeRates:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    @classmethod
    async def create(cls):
        self = cls()
        await self.fetch_from_api()
        return self

    async def fetch_from_api(self) -> None:
        async with httpx.AsyncClient() as client:
            response = await client.get("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=UAH&apikey=PASTE_YOUR_API_KEY")
            self.data = response.json()

async def main():
    er = await ExchangeRates.create()
    print(er.data)

if __name__ == "__main__":
    asyncio.run(main())
