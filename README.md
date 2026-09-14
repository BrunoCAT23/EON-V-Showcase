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

The project separates high-level robot logic from physical hardware through a hardware abstraction layer.

```text
        EON-V Runtime
              |
       Application Layer
              |
        AI / Robot Logic
              |
     Hardware Abstraction
          /       \
         /         \
 Simulation     Real Hardware
                    |
              Raspberry Pi
                    |
                 Arduino
                    |
          Motors / Servos / I/O

## Simulation Demo

The showcase includes a small runnable simulation demonstrating the hardware abstraction architecture without requiring physical robot hardware.

Run from the repository root:

```bash
python -m examples.simulation_demo