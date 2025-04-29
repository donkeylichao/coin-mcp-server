from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
from typing import Annotated
from pydantic import Field

mcp =  FastMCP("coin")

COIN_API_BASE = "https://www.binance.com/bapi/asset/v2/public/asset-service/product/get-product-by-symbol"    

async def get_coin_price(coin_id:str) -> dict[str,Any] | None:
    """Get coin price"""
    async with httpx.AsyncClient(proxy='http://127.0.0.1:7890') as client:
        try:
            url = f"{COIN_API_BASE}?symbol={coin_id}USDT"
           
            response = await client.get(url, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None


@mcp.tool()
async def get_price(coin: str = Field(
        ...,
        description='加密货币名称。e.g. BTC, ETH, USDT',
    )) -> str:
    """获取指定加密货币的当前价格。"""
    
    ret = await get_coin_price(coin)

    if not ret or "data" not in ret:
        return "Unable to fetch data."

    if not ret["data"]:
        return "No data for coin."

    if "c" in ret["data"] and ret["data"]["c"]:
        price = ret["data"]["c"]
    return price



if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')