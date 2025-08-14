from fastmcp import FastMCP
from fastmcp.server.proxy import ProxyClient


REMOTE_GOWEB3_MCP_SERVER = "https://mcp.goweb3.fyi/mcp/"


# Bridge remote server to local stdio
app = FastMCP.as_proxy(
    ProxyClient(REMOTE_GOWEB3_MCP_SERVER),     
    name="Remote-to-Local GOWEB3 MCP Bridge"
)


# Run locally via stdio for Claude Desktop
if __name__ == "__main__":
    app.run()  