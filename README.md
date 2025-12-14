# Advent of Code Solutions

This repository contains my solutions to [Advent of Code](https://adventofcode.com/) problems, implemented in Python.

## Project Structure

```
advent-of-code/
├── day_1/
│   ├── problem1.py      # Solution for Part 1
│   ├── problem2.py      # Solution for Part 2
│   ├── input.py         # Input parsing utilities
│   ├── utils.py         # Helper functions/ Core logic functions
│   └── input.txt        # Problem input (gitignored)
├── .gitignore
└── README.md
```

## Day 1: Dial Rotation Problem

### Problem Overview

This problem involves rotating a dial with 100 positions (numbered 0-99). The dial starts at position 50 and follows a series of rotation instructions.

**Input Format:**

- Each line contains a rotation instruction: `L<distance>` or `R<distance>`
- `L` = Left (counter-clockwise)
- `R` = Right (clockwise)
- `<distance>` = Number of positions to rotate

**Examples:**

- `R29` = Rotate right 29 positions
- `L8` = Rotate left 8 positions

### Part 1

Counts how many times the dial passes through position 0 during all rotations.

**Solution:** `day_1/problem1.py`

**How to run:**

```bash
python day_1/problem1.py
```

### Part 2

Counts the number of full rotations (complete 100-position cycles) the dial makes during all rotations.

**Solution:** `day_1/problem2.py`

**How to run:**

```bash
python day_1/problem2.py
```

## Files Description

### `input.py`

Contains the `parse_input()` function that reads input files and returns a list of rotation instructions.

**Usage:**

```python
import input
instructions = input.parse_input("day_1/input.txt")
```

### `utils.py`

Contains utility functions for dial operations:

- **`rotate(current_pos, direction, distance)`**

  - Computes the new dial position after a rotation
  - Handles wrapping around the 0-99 range
  - Supports both left (L) and right (R) rotations

- **`calculate_full_rotations(start_pos, direction, distance)`**
  - Calculates how many complete 100-position cycles are completed
  - Used for Part 2 of the problem

### `problem1.py` & `problem2.py`

Main solution files that:

1. Parse the input file
2. Process each rotation instruction
3. Track the required metrics (position 0 crossings or full rotations)
4. Output the final result

## Requirements

- Python 3.x
- No external dependencies (uses only standard library)

## Getting Started

1. Clone this repository
2. Add your `input.txt` file to the respective day's directory
3. Run the solution:
   ```bash
   cd day_1
   python problem1.py  # or problem2.py
   ```

## Notes

- Input files (`input.txt`) are gitignored to avoid committing personal puzzle inputs
- Each day's solution is self-contained in its own directory
- Solutions are designed to be readable and well-documented

## License

This repository is for personal learning purposes as part of the Advent of Code challenge.
