# Cleanup Comments Script

This repository contains a Node.js script designed to clean up single-line comments from TypeScript (.tsx) files within a project. It supports both Prettier and ESLint formatting options, allowing for automatic code formatting after removing comments.

```shell
┌─[remcostoeten@keyboar] - [~/development/minimal-cv] - [10041]
└─[$] pnpm cleanup InfiniteSlider.tsx                                                                                                                                        [21:46:28]

> minimal-cv@0.1.0 cleanup /home/remcostoeten/development/minimal-cv
> node src/core/scripts/cleanup-comments.js "InfiniteSlider.tsx"

Trying to load prettier...
Loaded prettier
Removed comments: // wadwwa,//fwafaw,//  let a= 'b',//;test
Removed comments from /home/remcostoeten/development/minimal-cv/src/components/effects/InfiniteSlider.tsx
Formatted /home/remcostoeten/development/minimal-cv/src/components/effects/InfiniteSlider.tsx
```

## Features

- Removes single-line comments from `.tsx` files.
- Supports automatic code formatting using either Prettier or ESLint.
- Works recursively through directories starting from a specified base directory.

## Usage

To use this script, you need to have Node.js installed on your system. You can run the script from the command line as follows:

bash node src/core/scripts/cleanup-comments.js `<filename>`

Replace `<filename>` with the name of the `.tsx` file you want to clean up comments from.

### Example

Assuming you have a project structure similar to the following:

```
/my-project
├── src/
│   ├── components/
│   │   └── MyComponent.tsx
└── package.json
```

To clean up comments from `MyComponent.tsx`, navigate to the root of your project (`my-project`) and run:

`bash node src/core/scripts/cleanup-comments.js MyComponent.tsx`

This will remove single-line comments from `MyComponent.tsx` and then apply either Prettier or ESLint formatting, depending on what is available in your environment.

## Integration with npm scripts

The script can be integrated into your project's npm scripts for easier usage. Here's how you might add it to your `package.json`:

`json "scripts": { ... "cleanup": "node src/core/scripts/cleanup-comments.js" `

Then, you can run the cleanup script with:

`pnpm cleanup <filename>`

<small>Or npm, yarn, bun..</small>
