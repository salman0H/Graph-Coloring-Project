# Graph Coloring Project

This repository contains a Python project that implements a **graph coloring** algorithm for two sets of provinces:

1. **Iran Provinces:** A set of provinces in Iran, interconnected based on their geographical borders.
2. **Khorasan Provinces:** A more localized set of provinces from the Khorasan region.

The algorithm assigns colors to each province such that no two neighboring provinces share the same color. This is useful for various applications, such as geographic mapping, resource allocation, and more.

---

## Features

- **Graph Representation:**
  - Provinces and their neighbors are represented as a graph.
  - Nodes represent provinces, and edges represent connections between neighboring provinces.

- **Coloring Algorithm:**
  - A backtracking algorithm ensures that provinces are assigned valid colors.
  - Supports up to 4 colors: Green, Red, Blue, and White.

- **Interactive GUI:**
  - Allows users to select a map (Iran or Khorasan) to visualize the coloring.
  - Displays the result in a color-coded table using Tkinter.

---

## Requirements

- Python 3.x
- Tkinter (comes pre-installed with Python)

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/graph-coloring.git
   cd graph-coloring
   ```

2. Run the script:
   ```bash
   python main.py
   ```

3. Select the map you want to color (Iran or Khorasan).

4. View the results in a dynamically generated table.

---

## Directory Structure

```
.
├── main.py          # Main executable script
├── README.md        # Project documentation
└── LICENSE          # License file
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request on GitHub.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

Special thanks to the developers and contributors who helped make this project possible.

---

Feel free to customize or enhance the functionality of this project as needed. Happy coding!
