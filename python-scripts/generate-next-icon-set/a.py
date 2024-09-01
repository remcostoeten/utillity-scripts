import os
import shutil
from PIL import Image
import argparse
import json
import textwrap

ICON_SIZES = {
    "favicon.ico": [16, 32],  # Multiple sizes for .ico
    "apple-icon.png": 180,    # Apple Touch Icon
    "icon.png": 32,           # Default icon (32x32 as per Next.js conventions)
    "icon-192x192.png": 192,  # Android/Chrome favicon
    "icon-256x256.png": 256,
    "icon-384x384.png": 384,
    "icon-512x512.png": 512,
}

def check_dimensions(image_path):
    """Check the dimensions of the input image."""
    with Image.open(image_path) as img:
        width, height = img.size
        print(f"Image dimensions: {width}x{height}")
        return width, height

def generate_icons(image_path, output_dir):
    """Generate icons in various sizes from a single image."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with Image.open(image_path).convert("RGBA") as img:
        for name, size in ICON_SIZES.items():
            output_path = os.path.join(output_dir, name)
            if name == "favicon.ico":
                # For favicon.ico, save multiple sizes in one .ico file
                img.save(output_path, format='ICO', sizes=[(s, s) for s in size])
            else:
                resized_img = img.resize((size, size) if isinstance(size, int) else size, Image.LANCZOS)
                if name.endswith('.png'):
                    resized_img.save(output_path, 'PNG')
                else:
                    resized_img.convert("RGB").save(output_path)
            print(f"Saved: {output_path}")
    
    # Prompt for app name
    app_name = input("Enter your app name for the manifest.json: ")
    
    # Create manifest.json
    manifest = {
        "name": app_name,
        "short_name": app_name,
        "icons": [
            {"src": f"/icons/{icon}", "sizes": f"{size}x{size}", "type": "image/png"}
            for icon, size in [("icon-192x192.png", 192), ("icon-256x256.png", 256), ("icon-384x384.png", 384), ("icon-512x512.png", 512)]
        ],
        "theme_color": "#ffffff",
        "background_color": "#ffffff",
        "display": "standalone"
    }
    with open(os.path.join(output_dir, "manifest.json"), "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"Created manifest.json with app name: {app_name}")

def get_app_name():
    """Prompt the user for the app name and confirm it."""
    while True:
        app_name = input("What is your app name? ")
        confirm = input(f"Is '{app_name}' correct? (Y/N): ").strip().lower()
        if confirm == 'y':
            return app_name

def implement_icons(icons_path, project_path):
    """Implement the generated icons in the Next.js project structure."""
    app_dir = os.path.join(project_path, "src", "app")
    icons_dir = os.path.join(app_dir, "icons")

    # Create directories if they don't exist
    os.makedirs(app_dir, exist_ok=True)
    os.makedirs(icons_dir, exist_ok=True)

    # Move favicon.ico and icon.png to app directory
    shutil.copy(os.path.join(icons_path, "favicon.ico"), app_dir)
    shutil.copy(os.path.join(icons_path, "icon.png"), app_dir)

    # Move other icons to the icons directory
    for icon in ["icon-192x192.png", "icon-256x256.png", "icon-384x384.png", "icon-512x512.png", "apple-icon.png"]:
        shutil.copy(os.path.join(icons_path, icon), icons_dir)

    # Check if manifest.json exists, if not create a basic one
    manifest_path = os.path.join(icons_path, "manifest.json")
    if not os.path.exists(manifest_path):
        print("manifest.json not found. Creating a basic one.")
        
        # Get app name with confirmation
        app_name = get_app_name()
        
        # Create a basic manifest
        manifest = {
            "name": app_name,
            "short_name": app_name,
            "start_url": ".",
            "display": "standalone"
        }
        
        with open(manifest_path, "w") as f:
            json.dump(manifest, f, indent=2)

    # Move manifest.json to app directory
    shutil.copy(manifest_path, app_dir)

    print(f"Icons implemented in {project_path}")
    print("Don't forget to update your metadata in src/app/layout.js or src/app/layout.tsx!")

def main():
    parser = argparse.ArgumentParser(
        description='Next.js Icon Generator and Implementer',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''
        ... [help text remains the same] ...
        '''))
    
    parser.add_argument('--check-dimensions', action='store_true', 
                        help='Check dimensions of the input image')
    parser.add_argument('--implement', action='store_true', 
                        help='Implement icons in the Next.js project structure')
    parser.add_argument('--image-path', type=str, 
                        help='Path to the input image (e.g., logo.png, favicon.jpg)')
    parser.add_argument('--output-dir', type=str, default='icons', 
                        help='Directory to save generated icons (default: icons)')
    parser.add_argument('--icons-path', type=str, 
                        help='Path to the directory containing generated icons')
    parser.add_argument('--project-path', type=str, 
                        help='Path to the Next.js project root')

    args = parser.parse_args()

    if args.check_dimensions:
        if not args.image_path:
            parser.error("--check-dimensions requires --image-path")
        check_dimensions(args.image_path)
    elif args.implement:
        if not args.icons_path or not args.project_path:
            parser.error("--implement requires both --icons-path and --project-path")
        implement_icons(args.icons_path, args.project_path)
    else:
        if not args.image_path:
            parser.error("--image-path is required when not using --implement or --check-dimensions")
        generate_icons(args.image_path, args.output_dir)

if __name__ == "__main__":
    main()
