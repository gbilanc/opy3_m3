"---
invokable: true
---

Review this code for potential issues, including:

- **PySide6 Threading:** Ensure that any long-running PLC communication tasks in `fins/` or data processing in `classes/` are not running on the main GUI thread to prevent the application from freezing.
- **FINS Protocol Robustness:** Check for proper timeout handling and error recovery in the UDP/TCP communication layer.
- **Resource Management:** Verify that file handles (DXF) and network sockets are correctly closed.
- **Settings Validation:** Ensure that values loaded from `settings.ini` via `csettings.py` are validated for type and range before being used in calculations.
- **DXF Coordinate Precision:** Check if floating point precision issues occur when translating DXF units to PLC units via `scale_unit`.

Provide specific, actionable feedback for improvements."