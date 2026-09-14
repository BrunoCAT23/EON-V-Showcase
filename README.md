# EON-V Showcase

EON-V is a personal AI robotics project focused on building a modular robot companion platform.

This repository is a public engineering showcase of selected EON-V components.  
The complete EON-V system and its proprietary AI/behavior architecture remain private.

## Project Goals

EON-V explores the integration of:

- Python robotics software
- Raspberry Pi
- Arduino
- Hardware abstraction
- Robot simulation
- Voice interaction
- Computer vision
- AI / LLM integration
- Modular robot behaviors
- Automated testing

## Architecture

EON-V Showcase uses a hardware abstraction layer to separate high-level robot software from physical hardware implementations.

The architecture currently includes:

- a common `HardwareBackend` protocol
- a software-based `SimulationHardware` backend
- a backend factory for selecting hardware implementations
- automated tests for hardware behavior and interface compatibility

This design allows robotics software to be developed and tested without requiring physical robot hardware.

For a detailed architecture overview, see:

[Architecture Documentation](docs/architecture.md)

## Simulation Demo

The showcase includes a small runnable simulation demonstrating the hardware abstraction architecture without requiring physical robot hardware.

Run from the repository root:

```bash
python -m examples.simulation_demo