import random

# import requests
import sys

import aiohttp
import asyncio


async def get_image(session: aiohttp.ClientSession, width=200, height=300):
    base_url = 'https://picsum.photos/'
    url = f'{base_url}/{width}/{height}'

    headers = {
        'authority': 'picsum.photos',
        'method': 'GET',
        'path': f'/ {width} / {height}',
        'scheme': 'https',
        'accept': 'text / html, application / xhtml + xml, application / xml',
        'referer': 'https://picsum.photos/',
        'sec-fetch-mode': 'navigate',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
    }
    # response = requests.get(url, headers=headers, proxies=proxies)

    async with session.get(url=url, headers=headers) as response:
        # with open('file.jpeg', 'wb') as file:
        #     file.write(await response.content)
        return response.url


async def execute(amount=5):
    tasks = []
    async with aiohttp.ClientSession() as session:
        for _ in range(amount):
            w = random.randint(400, 1000)
            h = random.randint(400, 1000)
            # url = get_image(width=w, height=h)
            # print(f"'{url}'", end=',\n')
            task = asyncio.create_task(get_image(session, width=w, height=h))
            tasks.append(task)

        completed_tasks = await asyncio.gather(*tasks)

        for task in completed_tasks:
            print(f"'{task}'", end=',\n')


def main():
    x = int(sys.argv[1])
    asyncio.get_event_loop().run_until_complete(execute(x))


if __name__ == '__main__':
    x = int(input('amount: '))
    asyncio.get_event_loop().run_until_complete(execute(x))
