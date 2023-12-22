from startup import startup
from user_proxy import call_agent
import asyncio

if __name__ == "__main__":
    startup()
    async def _test():
        #output = await call_agent("who are you")
        #output = await call_agent("tell a joke about sports")
        output = await call_agent("send all invoices to me")
        print(output)
    asyncio.run(_test())