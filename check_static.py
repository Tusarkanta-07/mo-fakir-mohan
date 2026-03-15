import os
import shutil

# Check static folder
static_dir = r'D:\gemini cli vs codium\projects\mo fakir mohan\static'
print("Static folder contents:")
for root, dirs, files in os.walk(static_dir):
    level = root.replace(static_dir, '').count(os.sep)
    indent = ' ' * 2 * level
    print(f'{indent}{os.path.basename(root)}/')
    subindent = ' ' * 2 * (level + 1)
    for file in files:
        print(f'{subindent}{file}')

# Check portal static folder
print("\nPortal static folder contents:")
portal_static = r'D:\gemini cli vs codium\projects\mo fakir mohan\portal\static'
for root, dirs, files in os.walk(portal_static):
    level = root.replace(portal_static, '').count(os.sep)
    indent = ' ' * 2 * level
    print(f'{indent}{os.path.basename(root)}/')
    subindent = ' ' * 2 * (level + 1)
    for file in files:
        print(f'{subindent}{file}')

# Check if staticfiles has old CSS
print("\nStaticfiles CSS check:")
staticfiles_css = r'D:\gemini cli vs codium\projects\mo fakir mohan\staticfiles\portal\css\style.css'
if os.path.exists(staticfiles_css):
    with open(staticfiles_css, 'r') as f:
        first_lines = ''.join([f.readline() for _ in range(10)])
        print("First 10 lines of staticfiles CSS:")
        print(first_lines)
