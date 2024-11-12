# Description: This program generates a Fibonacci sequence of a given length and plots it in a polar coordinate system.

# Importing the necessary libraries.
import numpy as np
from matplotlib import pyplot as plt

# Generates a Fibonacci sequence of a given length.
def fibonacci(length: int) -> list[int]:
    if length <= 0:
        return []

    if length == 1:
        return [0]

    sequence = [0, 1]
    while len(sequence) < length:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence

# Plots the Fibonacci sequence in a polar coordinate system.

def plot_fibonacci(sequence: list[int]):
    golden_ratio = sequence[-1] / sequence[-2]
    angles = np.linspace(0, 8 * np.pi, num=len(sequence))
    radius = golden_ratio ** (angles / np.pi)

    x = radius * np.cos(angles)
    y = radius * np.sin(angles)
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, color="green", linewidth=1)
    plt.axis("equal")
    plt.axis("off")
    plt.show()

# Main function that prompts the user for the length of the Fibonacci sequence and generates the sequence and plot.
def main():
    while True:
        try:
            length = int(input("Enter the length of the Fibonacci sequence: "))
            if length < 0:
                print("Please enter a non-negative integer.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")

    sequence = fibonacci(length)
    plot_fibonacci(sequence)

# Entry point of the program.
if __name__ == "__main__":
    main()