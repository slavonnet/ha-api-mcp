# ha-api-mcp

Reusable Home Assistant API core for MCP-compatible servers.

## About the package

`ha-api-mcp` is a reusable core for exposing Home Assistant API capabilities through MCP tools.
It is designed to be used as an independent Python package, separate from Home Assistant integration adapters.

## Installation

### Install from package index

```bash
python3 -m pip install ha-api-mcp
```

### Install from GitHub release/tag

```bash
python3 -m pip install "git+https://github.com/slavonnet/ha-api-mcp.git@v0.1.0"
```

### Build from source

```bash
python3 -m pip install build
python3 -m build
python3 -m pip install dist/ha_api_mcp-0.1.0-py3-none-any.whl
```

## Features

- ✅ Home Assistant API endpoint discovery from runtime router
- ✅ MCP tools schema generation
- ✅ Tool call argument validation
- ✅ MCP call -> Home Assistant REST API proxy translation
- ✅ Scope filtering and read-only enforcement
- ✅ TTL cache for tool schemas
- ✅ Embedded HTTP MCP server (`/health`, `/mcp/tools`, `/mcp/call`)

## Roadmap

- 🔜 Generate package documentation from source code/docstrings

## Documentation

- 📚 Package docs: [docs/README.md](docs/README.md)

## Usage examples

- ▶️ See [examples/basic_server.py](examples/basic_server.py)

## Dependency security

- ✅ Dependency security gate is enforced in CI (`pip-audit`)
- ✅ Dependency security reviewed on: **2026-03-13**

## Coverage

- ✅ Documentation coverage: **100%**
- ✅ Test coverage: **100%**

## Test matrix

- ✅ Unit tests
- ✅ Version compatibility tests (migrated subset)
- ✅ Quality tests (API docstrings and public exports)
- ⚪ Integration flow tests (Client -> MCP -> HA API mock): remain in integration repository
- ⚪ Install smoke tests: remain in integration repository

## Home Assistant compatibility

- ✅ 2026.3

## License

MIT License. See [LICENSE](LICENSE).
