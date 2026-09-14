from typing import Protocol, runtime_checkable

@runtime_checkable
class HardwareBackend(Protocol):
    """Public hardware abstraction contract for the EON-V showcase."""

    def move(self, left_speed: float, right_speed: float) -> None:
        """Control the left and right drive motors."""
        ...

    def stop(self) -> None:
        """Stop all drive motors."""
        ...

    def set_servo(self, channel: int, angle: float) -> None:
        """Set a servo to the requested angle."""
        ...

    def display(self, frame: object) -> None:
        """Send a frame or visual state to the robot display."""
        ...

    def speak(self, text: str) -> None:
        """Send text to the active audio output backend."""
        ...