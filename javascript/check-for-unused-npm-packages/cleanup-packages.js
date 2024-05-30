# Cleanup Packages Script

This script is used to maintain the health of your project's dependencies. It checks for unused and outdated npm packages in your project.

## Usage

To run this script, navigate to the directory containing `cleanup-packages.js` and run the following command:

```bash
./cleanup-packages.js
```

Easiest would be to place the script in a lib or script folder in your projects and then modify the `package.json` file to include a script that runs the script. For example:

```json
"scripts": {
  "cleanup": "node ./scripts/cleanup-packages.js"
}
```

## What it Does

1. **Check for unused dependencies**: The script uses `depcheck` to find and list any dependencies in your project that are not being used.

2. **Check for outdated packages**: The script uses `npm outdated` to find and list any dependencies in your project that are outdated.

## Prerequisites

Ensure that you have `depcheck` installed globally. If not, you can install it using the following command:

```bash
npm install -g depcheck
```
