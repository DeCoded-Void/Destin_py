from source import destin
import asyncio


async def main():
    destiny = destin.api('YOUR API KEY HERE')
    weeklymilestone = await destiny.Destiny2.GetPublicMilestones()
    print(weeklymilestone)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
