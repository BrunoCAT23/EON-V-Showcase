from hardware.backend_factory import create_hardware_backend


def main() -> None:
    hardware = create_hardware_backend("simulation")

    hardware.move(0.6, 0.6)
    hardware.set_servo(0, 45.0)
    hardware.display({"eyes": "happy"})
    hardware.speak("EON-V simulation is running.")
    hardware.stop()

    print("Simulation demo completed successfully.")


if __name__ == "__main__":
    main()