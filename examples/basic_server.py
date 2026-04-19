"""Minimal usage example for ha-api-mcp package."""

from ha_api_mcp.catalog import ApiCatalog
from ha_api_mcp.models import McpSettings
from ha_api_mcp.proxy import ApiProxy
from ha_api_mcp.schema import SchemaCache
from ha_api_mcp.server import McpHttpServer


def build_server(hass_object: object) -> McpHttpServer:
    """Build MCP server instance from Home Assistant runtime object."""
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
    catalog = ApiCatalog(hass=hass_object)
    proxy = ApiProxy(settings)
    cache = SchemaCache(ttl_seconds=settings.schema_cache_ttl)
    return McpHttpServer(
        settings=settings,
        catalog=catalog,
        proxy=proxy,
        schema_cache=cache,
    )
