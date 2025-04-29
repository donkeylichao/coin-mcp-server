from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
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
        return "无法获取数据。"

    if not ret["data"]:
        return f"未找到 {coin} 的数据。"

    if "c" in ret["data"] and ret["data"]["c"]:
        price = ret["data"]["c"]
        return f"{coin} 当前价格: {price} USDT"
    return "无法获取价格信息。"

def main():
    """启动 MCP 服务器"""
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()