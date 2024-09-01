# Next.js Icon Generator and Implementer

This script automates the process of generating and implementing icons for Next.js projects. It supports various image formats and creates all necessary icons as per Next.js conventions.

## Features

- Generate icons from a single source image
- Check dimensions of the source image
- Implement generated icons in your Next.js project structure
- Support for multiple input formats (PNG, JPEG, WebP, GIF, BMP, etc.)
- Interactive prompt for app name to use in manifest.json

## Installation

1. Ensure you have Python 3.x installed
2. Install the required dependencies:

```
pip install Pillow
```

3. Download the `icon-generator.py` script to your local machine

## Usage

### Generate Icons

```
python icon-generator.py --image-path path/to/logo.png --output-dir ./icons
```

You can omit the `--output-dir` flag to use the default output directory `./icons`:

```
python icon-generator.py --image-path logo.webp
```

You will be prompted to enter your app name for the manifest.json file.

### Check Image Dimensions

```
python icon-generator.py --check-dimensions --image-path path/to/logo.jpg
```

### Implement Icons in Project

```
python icon-generator.py --implement --icons-path ./icons --project-path /path/to/nextjs/project
```

## Generated Icons

- favicon.ico: 16x16, 32x32 (multi-size ICO file)
- apple-icon.png: 180x180
- icon.png: 32x32
- icon-192x192.png: 192x192
- icon-256x256.png: 256x256
- icon-384x384.png: 384x384
- icon-512x512.png: 512x512
- manifest.json: Web app manifest file

## Resulting Next.js Project Structure

```
src/app/
├── favicon.ico
├── icon.png
├── manifest.json
└── icons/
    ├── apple-icon.png
    ├── icon-192x192.png
    ├── icon-256x256.png
    ├── icon-384x384.png
    └── icon-512x512.png
```

## Integrating Icons into Next.js Project

1. Generate icons using this script (you'll be prompted for the app name)
2. Implement icons in your project structure using the `--implement` flag
3. In your `app/layout.js` or `app/layout.tsx`, add the following metadata:

```
export const metadata = {
  icons: {
    icon: '/icon.png',
    shortcut: '/favicon.ico',
    apple: '/icons/apple-icon.png',
    other: {
      rel: 'apple-touch-icon-precomposed',
      url: '/icons/apple-touch-icon-precomposed.png',
    },
  },
  manifest: '/manifest.json',
}
```

## Note

After implementation, remember to review and update your metadata in `src/app/layout.js` or `src/app/layout.tsx` if necessary.

For more information on Next.js icon conventions, visit:
https://nextjs.org/docs/app/api-reference/file-conventions/metadata
