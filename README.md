# ha-api-mcp

Reusable Home Assistant API core for MCP-compatible servers.

## What this package provides

`ha-api-mcp` extracts reusable logic that was previously embedded in
`ha-api-mcp` integration-core code, including:

- API endpoint discovery from Home Assistant router
- deterministic tool schema generation for MCP clients
- request argument validation
- proxy translation between MCP tool calls and HA REST API
- minimal aiohttp MCP server (`/health`, `/mcp/tools`, `/mcp/call`)
- scope allowlist and read-only enforcement
- TTL cache for generated tools schema

## Installation

### From PyPI (recommended after publish)

```bash
python3 -m pip install ha-api-mcp
```

### From GitHub tag

```bash
python3 -m pip install "git+https://github.com/slavonnet/ha-api-mcp.git@v0.1.0"
```

## Quick usage example

```python
from ha_api_mcp.catalog import ApiCatalog
from ha_api_mcp.models import McpSettings
from ha_api_mcp.proxy import ApiProxy
from ha_api_mcp.schema import SchemaCache
from ha_api_mcp.server import McpHttpServer

settings = McpSettings(
    bind_address="0.0.0.0",
    port=8124,
    auth_token="",
    target_user="owner",
    read_only=False,
    scope_allowlist=(),
    schema_cache_ttl=300,
    timeout=15,
    base_url="http://homeassistant.local:8123",
)

catalog = ApiCatalog(hass=your_hass_object)
proxy = ApiProxy(settings)
cache = SchemaCache(ttl_seconds=settings.schema_cache_ttl)
server = McpHttpServer(
    settings=settings,
    catalog=catalog,
    proxy=proxy,
    schema_cache=cache,
)
```

## Development and quality gates

```bash
python3 -m pip install -r requirements-dev.txt
python3 -m pip install -e ".[test]"
python3 -m ruff check .
python3 -m mypy src tests
python3 -m pytest -q --cov=src --cov-branch --cov-fail-under=100 --cov-report=term-missing
```

The repository enforces:

- linting with Ruff
- type checks with mypy
- unit + quality tests
- **100% branch coverage** gate
- API docstring quality checks
- public export integrity checks

## License

MIT License. See [LICENSE](LICENSE).
