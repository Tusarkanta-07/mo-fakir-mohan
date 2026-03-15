import urllib.request

try:
    url = 'http://127.0.0.1:8000/static/portal/css/style.css?v=2'
    with urllib.request.urlopen(url, timeout=5) as response:
        content = response.read().decode('utf-8')
        print("CSS loaded successfully!")
        print("First 500 characters:")
        print(content[:500])
except Exception as e:
    print(f"Error: {e}")
