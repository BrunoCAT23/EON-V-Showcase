from hardware.simulation_hardware import SimulationHardware
from hardware_interfaces.hardware_backend import HardwareBackend


def create_hardware_backend(backend: str = "simulation") -> HardwareBackend:
    """Create a hardware backend for the EON-V showcase."""

    backend_name = backend.strip().lower()

    if backend_name == "simulation":
        return SimulationHardware()

    raise ValueError(f"Unsupported hardware backend: {backend}")