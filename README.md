
### Installing Manually
Install using uv:

1.首先，确保安装了 uv：
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
2.然后，直接从 github 安装：
```bash
uv pip install git+https://github.com/donkeylichao/coin-mcp-server.git --system
```

或者，您也可以克隆仓库后本地安装：

```bash
# 克隆仓库
git clone https://github.com/donkeylichao/coin-mcp-server.git
cd coin-mcp-server

# 安装依赖
uv pip install -e .
```


安装完成后，您就可以运行：

```bash
coin-mcp-server
```

cursor 配置
```
{
  "mcpServers": {
    "coin": {
        "command": "coin-mcp-server"
    }
  }
}
```