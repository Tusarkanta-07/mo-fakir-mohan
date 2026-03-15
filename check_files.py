import os

css_path = r'D:\gemini cli vs codium\projects\mo fakir mohan\static\portal\css\style.css'
js_path = r'D:\gemini cli vs codium\projects\mo fakir mohan\static\portal\js\main.js'

print('CSS exists:', os.path.exists(css_path))
if os.path.exists(css_path):
    print('CSS size:', os.path.getsize(css_path), 'bytes')
    with open(css_path, 'r', encoding='utf-8') as f:
        first_line = f.readline()
        print('CSS first line:', first_line.strip())

print('\nJS exists:', os.path.exists(js_path))
if os.path.exists(js_path):
    print('JS size:', os.path.getsize(js_path), 'bytes')
