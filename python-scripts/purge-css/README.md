# Unused CSS Checker

This Python script helps you identify unused SCSS/CSS classes in your Next.js project with Tailwind CSS. It analyzes your TSX files and compares the classes used with those defined in your SCSS files.

## Features

- Check for unused classes in the entire `src` directory
- Focus on specific directories like `src/app` or `src/components`
- Analyze a single SCSS file against all TSX files
- Provides a user-friendly command-line interface with help menu

## Prerequisites

- Python 3.6 or higher
- A Next.js project with Tailwind CSS and additional SCSS files

## Installation

1. Copy the `purge_css.py` script into your project's `src/core/scripts/` directory.

2. Ensure the script has executable permissions:

```bash
chmod +x src/core/scripts/purge_css.py
~```~

## Usage

Here are some examples of how to use the script:

1. Check all TSX files in the `src` directory:

```bash
python src/core/scripts/purge_css.py
```

2. Check only TSX files in the `src/app` directory:

```bash
python src/core/scripts/purge_css.py --app
```

3. Check only TSX files in the `src/components` directory:

```bash
python src/core/scripts/purge_css.py --components
```

4. Check a single SCSS file against all TSX files:

```bash
python src/core/scripts/purge_css.py --checkSingle src/styles/components/a-big-component.scss
```

5. Display the help menu:

```bash
python src/core/scripts/purge_css.py --help
```

## Configuration

The script uses several constants that you can modify to match your project structure:

- `ROOT_DIR`: The root directory for the project (default: "src")
- `APP_DIR`: The directory for app-specific files (default: "src/app")
- `COMPONENTS_DIR`: The directory for component files (default: "src/components")
- `MAIN_SCSS_FILE`: The main SCSS file (default: "app.scss")
- `TSX_EXTENSION`: The extension for TSX files (default: ".tsx")
- `SCSS_EXTENSION`: The extension for SCSS files (default: ".scss")

To change these, edit the constants at the top of the `purge_css.py` file.

## Limitations

- The script analyzes static class names and may not detect dynamically added classes or those used in JavaScript.
- It uses simple regex patterns to extract classes, which may not catch all possible ways of defining or using classes in SCSS and TSX files.

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements or encounter any problems.

## License

This project is open source and available under the [MIT License](LICENSE).
