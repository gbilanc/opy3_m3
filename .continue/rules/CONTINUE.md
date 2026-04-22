# Project Guide: omronpy-m2

## Project Overview
**omronpy-m2** is a control application for a 2-axis plotter machine (with tool control) that communicates with an Omron NJ PLC using the FINS/UDP protocol.

- **Key Technologies:** Python 3.13+, PySide6 (GUI), ezdxf (DXF processing), FINS/UDP.
- **Purpose:** Import DXF paths, send them to a PLC, monitor axis status (X, Y, C), and manage tool-specific parameters (Roller, Pen, Cutter).
- **High-Level Architecture:** A PySide6 desktop application that serves as a bridge between DXF design files and a hardware PLC.

## Getting Started
### Prerequisites
- Python ≥ 3.13
- `uv` (recommended) or `pip`

### Installation
```bash
# Using uv
uv sync

# Using pip
pip install -r requirements.txt
```

### Basic Usage
Run the application using:
```bash
python -m opy3_m3
# OR
python __main__.py
```

### Running Tests
*(Verification needed: No explicit test suite found in root. Check `classes/` or `fins/` for internal tests)*.

## Project Structure
- `__main__.py`: Application entry point.
- `MainWindow.py`: Main application logic and window management.
- `DialogPreview.py`: Graphic preview of DXF paths.
- `DialogSettings.py`: Machine parameter configuration.
- `statics.py`: Enums, constants, and utility functions.
- `csettings.py`: Logic for reading/writing `settings.ini`.
- `ccolorpref.py` / `cmemopref.py`: DXF layer color and preference management.
- `classes/`: Data models for points, polylines, layers, and the workspace.
- `fins/`: Low-level implementation of the FINS protocol (UDP, TCP, USB).
- `ui/`: Qt Designer generated UI files.
- `resources.py`: Embedded assets and icons.
- `settings.ini`: Configuration file for IP addresses, offsets, and speeds.

## Development Workflow
- **Coding Standards:** Pythonic style (PEP 8). Use of PySide6 for UI components.
- **Configuration:** Modifications to machine behavior should generally be done via `DialogSettings.py` or by editing `settings.ini`.
- **Build/Deployment:** The project uses `pyproject.toml` and `setup.py` for packaging.

## Key Concepts
- **FINS Protocol:** Factory Interface Network System. The core communication layer between the PC and the Omron PLC.
- **DXF Processing:** The app parses DXF files into internal geometric representations (points/polylines) before translating them into PLC commands.
- **Axes (X, Y, C):** X and Y represent the 2D plane; C typically refers to the tool/cutter rotation or z-axis movement.

## Common Tasks
### Adding a New Tool Parameter
1. Add the parameter to `settings.ini`.
2. Update `csettings.py` to handle the new key.
3. Update `DialogSettings.py` and its corresponding `.ui` file to allow user modification.

### Modifying PLC Communication
1. Navigate to the `fins/` directory.
2. Modify the UDP/TCP implementation based on the Omron FINS specifications.

## Troubleshooting
- **PLC Connection Issues:** Check `settings.ini` for the correct `plcUrl` and `plcPort` (default 9600). Ensure the PC is on the same subnet as the PLC.
- **DXF Import Errors:** Ensure the DXF file is compatible with `ezdxf` version 1.4.3+.
- **UI Glitches:** Since UI files are generated, use Qt Designer to edit `.ui` files in the `ui/` folder, then re-run the application.

## References
- [ezdxf Documentation](https://ezdxf.readthedocs.io/)
- Omron FINS Protocol Specifications (External)