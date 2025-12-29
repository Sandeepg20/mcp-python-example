from mcp.server import Server
import asyncio

from tools import check_eligibility

server = Server(
    name="example-mcp-server",
    version="1.0.0"
)

# Register tools
server.add_tool(check_eligibility)

async def main():
    await server.start()

if __name__ == "__main__":
    asyncio.run(main())
