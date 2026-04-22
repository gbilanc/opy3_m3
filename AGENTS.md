"# AI Agents Guide: omronpy-m2

This document provides instructions for AI agents working on this codebase to ensure consistency and correctness.

## Context & Domain
This project is a specialized industrial control application for an Omron plotter. The critical path is:
`DXF File` $\rightarrow$ `ezdxf Parsing` $\rightarrow$ `Coordinate Scaling` $\rightarrow$ `FINS/UDP Protocol` $\rightarrow$ `Omron NJ PLC`.

## Technical Guidelines

### 1. GUI Development (PySide6)
- **Threading:** Never perform PLC communication or heavy DXF parsing on the main thread. Use `QThread` or `QRunnable` and communicate via `Signal/Slot`.
- **UI Generation:** UI files are managed in the `ui/` directory. When modifying the interface, update the `.ui` file via Qt Designer rather than hard-coding layouts in Python.

### 2. Communication (FINS Protocol)
- The `fins/` directory contains the protocol implementation.
- Always implement timeouts for UDP requests to avoid hanging the application.
- Ensure data types sent to the PLC match the PLC's expected memory mapping (Words, DWords).

### 3. Data Modeling & Geometry
- Geometric logic is centralized in the `classes/` directory.
- Respect the `scale_unit` defined in `settings.ini` when converting DXF units to PLC machine units.

### 4. Configuration
- Use `csettings.py` for any interaction with `settings.ini`. 
- Do not hard-code IP addresses or machine offsets; always retrieve them from the settings manager.

## Common Patterns to Follow
- **Constants:** Use `statics.py` for project-wide enums and constants.
- **Preferences:** Use `ccolorpref.py` and `cmemopref.py` for persisting user-specific visual preferences.
"