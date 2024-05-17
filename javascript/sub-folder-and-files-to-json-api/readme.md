### Folder and Recursive File to JSON API Format Converter

This JavaScript file provides functions to convert a folder structure and its files into a JSON API format.

## Installation

Clone this repository: `git clone https://github.com/your-repository.git`

Or curl straight into the file: `curl -O https://raw.githubusercontent.com/remcostoeten/utillity-scripts/main/javascript/folder-and-recursive-file-to-json-api-format.js`

## Usage

1. Update the `DOCUMENT_DIRECTORY` constant with the path to your folder structure.
2. Run the script: `node folder-and-recursive-file-to-json-api-format.js`
3. The JSON output will be saved in the `aaaa.json` file.

### Example

Given the following folder structure:

```
docs
├── graphql
│   ├── camelCase.mdx
│   ├── how-to-query.mdx
│   ├── JaCamelC.mdx
│   ├── testCamelCase.mdx
│   └── test-md.md
├── intro.mdx
├── react
│   ├── best-practices.mdx
│   ├── folder-structure.mdx
│   └── js-jsx-or-tsx?.mdx
├── styles
│   └── styled-components.mdx
└── workflow
    ├── eslint.mdx
    └── setup-husky-pre-commit.mdx
```

Running the script would generate the following JSON output:

```json
[
  {
    "name": "graphql",
    "icon": "graphql-icon.svg",
    "files": [
      "camelCase.mdx",
      "how-to-query.mdx",
      "JaCamelC.mdx",
      "testCamelCase.mdx",
      "test-md.md"
    ]
  },
  {
    "name": "react",
    "icon": "react-icon.svg",
    "files": [
      "best-practices.mdx",
      "folder-structure.mdx",
      "js-jsx-or-tsx?.mdx"
    ]
  },
  {
    "name": "styles",
    "icon": "styles-icon.svg",
    "files": [
      "styled-components.mdx"
    ]
  },
  {
    "name": "workflow",
    "icon": "workflow-icon.svg",
    "files": [
      "eslint.mdx",
      "setup-husky-pre-commit.mdx"
    ]
  }
]
```

This JSON output represents the folder structure in a format suitable for a JSON API.
