# ChEMBL-MCP-Server

基于chembl_webresource_client包的FastMCP包装服务器，提供ChEMBL数据库的API访问功能。

## 功能特点

- 提供ChEMBL数据库的完整API访问
- 使用FastMCP框架实现异步API调用
- 内置错误处理和超时机制
- 支持HTTP和stdio两种传输方式
- 完整的类型注解和文档字符串

## 安装

```bash
# 克隆仓库
git clone https://github.com/yourusername/ChEMBL-MCP-Server.git
cd ChEMBL-MCP-Server

# 安装依赖
pip install -r requirements.txt
```

## 使用方法

### 启动服务器

```bash
# 使用默认配置启动HTTP服务器
python chembl_api_server.py

# 指定主机和端口
python chembl_api_server.py --host 0.0.0.0 --port 8080

# 使用stdio传输方式
python chembl_api_server.py --transport stdio

# 设置日志级别
python chembl_api_server.py --log-level DEBUG
```

### 可用参数

- `--host`: 服务器主机地址，默认为127.0.0.1
- `--port`: 服务器端口，默认为8000
- `--transport`: 传输方式，可选http或stdio，默认为http
- `--log-level`: 日志级别，可选DEBUG、INFO、WARNING、ERROR、CRITICAL，默认为INFO

## API功能

服务器提供以下API功能：

### 数据实体API

- `example_activity`: 获取活性数据
- `example_assay`: 获取测定数据
- `example_target`: 获取靶点数据
- `example_molecule`: 获取分子数据
- `example_drug`: 获取药物数据
- 更多数据实体API...

### 化学工具API

- `example_canonicalizeSmiles`: 规范化SMILES字符串
- `example_smiles2inchi`: 将SMILES转换为InChI
- `example_smiles2svg`: 将SMILES转换为SVG图像
- `example_structuralAlerts`: 获取结构警报
- 更多化学工具API...

## 示例

查看`chembl_api_search.py`文件获取各API的使用示例。

## 依赖

- chembl_webresource_client: ChEMBL Web服务客户端
- mcp: MCP框架
- fastapi: FastAPI框架
- uvicorn: ASGI服务器
- asyncio: 异步IO库

## 许可

[MIT](LICENSE)