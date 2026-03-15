import os
import shutil

base_dir = r'D:\gemini cli vs codium\projects\mo fakir mohan'

# Check static folder structure
print("=== Static Folder Structure ===")
static_dir = os.path.join(base_dir, 'static')
for root, dirs, files in os.walk(static_dir):
    level = root.replace(static_dir, '').count(os.sep)
    indent = ' ' * 2 * level
    print(f'{indent}{os.path.basename(root)}/')
    subindent = ' ' * 2 * (level + 1)
    for file in files:
        filepath = os.path.join(root, file)
        size = os.path.getsize(filepath)
        print(f'{subindent}{file} ({size} bytes)')

# Check portal app static folder
print("\n=== Portal App Static Folder ===")
portal_static = os.path.join(base_dir, 'portal', 'static')
if os.path.exists(portal_static):
    for root, dirs, files in os.walk(portal_static):
        level = root.replace(portal_static, '').count(os.sep)
        indent = ' ' * 2 * level
        print(f'{indent}{os.path.basename(root)}/')
        subindent = ' ' * 2 * (level + 1)
        for file in files:
            filepath = os.path.join(root, file)
            size = os.path.getsize(filepath)
            print(f'{subindent}{file} ({size} bytes)')
