import pytest

from hardware.backend_factory import create_hardware_backend
from hardware.simulation_hardware import SimulationHardware
from hardware_interfaces.hardware_backend import HardwareBackend


def test_factory_creates_simulation_backend():
    backend = create_hardware_backend("simulation")

    assert isinstance(backend, SimulationHardware)
    assert isinstance(backend, HardwareBackend)


def test_factory_uses_simulation_by_default():
    backend = create_hardware_backend()

    assert isinstance(backend, SimulationHardware)


def test_factory_normalizes_backend_name():
    backend = create_hardware_backend("  SIMULATION  ")

    assert isinstance(backend, SimulationHardware)


def test_factory_rejects_unknown_backend():
    with pytest.raises(ValueError, match="Unsupported hardware backend"):
        create_hardware_backend("unknown")