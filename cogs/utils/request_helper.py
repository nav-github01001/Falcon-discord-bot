import aiohttp

async def get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as rqst:
            if rqst.status == 200:
                return await rqst.json()