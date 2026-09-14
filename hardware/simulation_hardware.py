from typing import Any


class SimulationHardware:
    """In-memory hardware backend used for development and testing."""

    def __init__(self) -> None:
        self.left_speed: float = 0.0
        self.right_speed: float = 0.0
        self.servo_positions: dict[int, float] = {}
        self.last_frame: Any | None = None
        self.last_spoken_text: str | None = None

    def move(self, left_speed: float, right_speed: float) -> None:
        """Simulate differential drive motor control."""
        self.left_speed = left_speed
        self.right_speed = right_speed

    def stop(self) -> None:
        """Stop the simulated drive motors."""
        self.left_speed = 0.0
        self.right_speed = 0.0

    def set_servo(self, channel: int, angle: float) -> None:
        """Store the requested simulated servo position."""
        self.servo_positions[channel] = angle

    def display(self, frame: object) -> None:
        """Store the latest simulated display frame."""
        self.last_frame = frame

    def speak(self, text: str) -> None:
        """Store the latest simulated speech output."""
        self.last_spoken_text = text