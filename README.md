# ha-api-mcp

Reusable Home Assistant API core for MCP-compatible servers.

## О пакете

`ha-api-mcp` — выделенный reusable core для работы с Home Assistant API из MCP-инструментов.
Пакет можно подключать независимо от Home Assistant integration-слоя.

## Как установить

### Из пакетов

```bash
python3 -m pip install ha-api-mcp
```

### Из GitHub релиза/тега

```bash
python3 -m pip install "git+https://github.com/slavonnet/ha-api-mcp.git@v0.1.0"
```

### Собрать самому

```bash
python3 -m pip install build
python3 -m build
python3 -m pip install dist/ha_api_mcp-0.1.0-py3-none-any.whl
```

## Возможности

- обнаружение API endpoint-ов Home Assistant из runtime router
- генерация MCP tools schema
- валидация аргументов вызова
- proxy MCP call -> Home Assistant REST API
- scope-filtering и read-only ограничения
- TTL cache для схем инструментов
- встроенный HTTP MCP server (`/health`, `/mcp/tools`, `/mcp/call`)

## Роадмап

- создание документации из исходников

## Документация

- удобная документация: [docs/README.md](docs/README.md)

## Примеры использования

- см. [examples/basic_server.py](examples/basic_server.py)

## Безопасность

Безопасность зависимостей проверена: **13.03.2026**.

## Покрытие

- Документация: **100%**
- Coverage: **100%**

## Тесты

- юнит-тесты
- версионные тесты
- quality-тесты (докстринги и публичные экспорты)

## Совместимость с Home Assistant

Релиз проверен на совместимость с HA версиями:

- 2026.3
