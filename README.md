![Logo](https://raw.githubusercontent.com/AbTrax/algofinder/main/res/Algo%20Finder%20Banner.png)

# Algo-Finder

An Open source code formatter that uses machine learning to determine the **time and space-complexity** of your algorithm
and its efficiency and recommends a faster and more efficient algorithms of a lower time, and if chosen space-complexity whilst keeping
code function and integrity, for Python and Rust (Planned).

## Features

- Logging of space and time complexity.
- Before and after time complexity comparison.
- Smart variable detection to allow ease of converting.
- Programming language detection.
- Revert back to previous algorithm if code errors do occur.
- Machine learning-based complexity prediction.

## Demo

## Color Reference

| Time Complexity             | Color                                                                |
| ----------------- | ------------------------------------------------------------------ |
| O(1), O(log n) | ![#1CF423](https://placehold.co/10/00ff9f/1cf423.png) #1CF423 |
| O(n log n) | ![#F98FAD](https://placehold.co/10/f98fad/f98fad.png) #F98FAD |
| ≤ O(n²)  | ![#FF4846](https://placehold.co/10/ff4846/ff4846.png) #FF4846 |

## Screenshots

![Screenshot](Temp)

## Usage/Examples

```bash
python -m algofinder <path_to_python_file>
```

## Training the Model

To train the model, you need a CSV file containing the training data. The CSV file should have the following columns:

- `num_loops`: The number of loop statements in the algorithm.
- `num_conditionals`: The number of conditional statements in the algorithm.
- `num_variables`: The number of variables in the algorithm.
- `num_arrays`: The number of arrays in the algorithm.
- `complexity`: The complexity of the algorithm.

You can train the model using the following command:

```bash
python -m algofinder train <path_to_csv_file>
```

## Analyzing Complexity

To analyze the complexity of the algorithms in a Python file, use the following command:

```bash
python -m algofinder analyze <path_to_python_file>
```

## Roadmap

- Improved CLI

- Better Variable Detection

- Rust and Other Language Support

- Web Demo

- ~~Language Detection~~ (Done)

- Use Click For CLI

## Lessons Learned

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Acknowledgements

- [Rosetta Code](https://rosettacode.org/wiki/Rosetta_Code)
- [Guesslang](https://github.com/yoeo/guesslang)
- [Libraries.io For Training Algorithms](https://libraries.io/data)
