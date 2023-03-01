import asyncio

from cdx.settings.settings import Settings


async def main():
    token = 'Bearer <token>'
    s = Settings(token=token)

    #// configure the tenant
    await s.enable_lc()
    await s.enable_storyline()
    await s.enable_stories()

if __name__ == '__main__':
    asyncio.run(main())
