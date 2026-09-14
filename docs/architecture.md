# EON-V Showcase Architecture

EON-V Showcase demonstrates a modular hardware abstraction architecture for a Python-based robotics platform.

## Architecture Overview

```text
+-----------------------------+
|      Robot Application      |
|                             |
|  Behaviors / AI / Control   |
+--------------+--------------+
               |
               v
+-----------------------------+
|       Backend Factory       |
|                             |
|   create_hardware_backend() |
+--------------+--------------+
               |
               v
+-----------------------------+
|      HardwareBackend        |
|          Protocol           |
|                             |
| move()       set_servo()    |
| stop()       display()      |
| speak()                     |
+--------------+--------------+
               |
       +-------+--------+
       |                |
       v                v
+--------------+   +--------------+
|  Simulation  |   | Real Hardware|
|   Backend    |   |   Backend    |
|              |   |   (future)   |
+--------------+   +------+-------+
                         |
                         v
                  +--------------+
                  | Raspberry Pi |
                  |   Arduino    |
                  | Motors / I/O |
                  +--------------+
```

## Design Goals

The architecture is designed around several principles:

- hardware-independent robot logic
- interchangeable hardware backends
- simulation without physical hardware
- clear interfaces between software and devices
- automated testing of hardware behavior
- extensibility toward Raspberry Pi and Arduino hardware

## Hardware Abstraction

`HardwareBackend` defines the public contract used by higher-level robot software.

The current showcase implementation provides a `SimulationHardware` backend that implements this contract entirely in software.

This allows robot behavior and hardware commands to be tested without connecting physical motors, servos, displays, or speakers.

## Backend Factory

The backend factory separates backend selection from application logic.

```python
hardware = create_hardware_backend("simulation")
```

Future implementations can provide physical hardware backends while preserving the same high-level interface.

## Testing

The architecture is covered by automated tests validating:

- motor commands
- stop behavior
- servo state
- display state
- speech output
- protocol compatibility
- backend factory behavior