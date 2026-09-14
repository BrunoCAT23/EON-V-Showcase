from hardware.simulation_hardware import SimulationHardware


def test_move_updates_motor_speeds() -> None:
    hardware = SimulationHardware()

    hardware.move(0.5, -0.25)

    assert hardware.left_speed == 0.5
    assert hardware.right_speed == -0.25


def test_stop_resets_motor_speeds() -> None:
    hardware = SimulationHardware()

    hardware.move(1.0, 1.0)
    hardware.stop()

    assert hardware.left_speed == 0.0
    assert hardware.right_speed == 0.0


def test_set_servo_stores_position() -> None:
    hardware = SimulationHardware()

    hardware.set_servo(1, 90.0)

    assert hardware.servo_positions[1] == 90.0


def test_display_stores_last_frame() -> None:
    hardware = SimulationHardware()
    frame = {"eyes": "happy"}

    hardware.display(frame)

    assert hardware.last_frame == frame


def test_speak_stores_last_text() -> None:
    hardware = SimulationHardware()

    hardware.speak("Hello from EON-V")

    assert hardware.last_spoken_text == "Hello from EON-V"

def test_simulation_hardware_satisfies_backend_contract() -> None:
    from hardware_interfaces.hardware_backend import HardwareBackend

    hardware = SimulationHardware()

    assert isinstance(hardware, HardwareBackend)