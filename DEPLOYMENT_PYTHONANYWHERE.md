# Deploy Mo Fakir Mohan to PythonAnywhere - Step by Step Guide

## Prerequisites
- A free PythonAnywhere account (sign up at https://www.pythonanywhere.com)
- Your project pushed to a GitHub repository (already done: https://github.com/Tusarkanta-07/mo-fakir-mohan)

---

## Step 1: Sign Up & Open Bash Console

1. Go to https://www.pythonanywhere.com and create a free account
2. After logging in, click **"Consoles"** → **"Bash"** to open a bash console
3. All subsequent commands should be run in this bash console

---

## Step 2: Clone Your Repository

```bash
# Clone your GitHub repository
git clone https://github.com/Tusarkanta-07/mo-fakir-mohan.git
cd "mo-fakir-mohan"

# If you have Git LFS files, install and pull them
git lfs install
git lfs pull
```

**Note:** If you don't have Git LFS installed on PythonAnywhere, install it first:
```bash
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
sudo apt-get install git-lfs
git lfs install
git lfs pull
```

---

## Step 3: Create a Virtual Environment

```bash
# Create virtual environment in your home directory
cd ~
mkvirtualenv --python=/usr/bin/python3.10 mo-fakir-mohan-env
```

---

## Step 4: Install Dependencies

```bash
# Install requirements
pip install -r requirements.txt

# Install additional required packages
pip install gunicorn
```

---

## Step 5: Configure Django Settings for Production

Create a production settings file or set environment variables. We'll use environment variables:

```bash
# Set environment variables for production
export SECRET_KEY='your-secret-key-here-generate-a-new-one'
export DEBUG=False
export ALLOWED_HOSTS=Tusar.pythonanywhere.com
```

**Generate a new secret key:**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

**Important:** Replace `yourusername` with your actual PythonAnywhere username.

---

## Step 6: Configure WSGI File

1. Go to **Web** tab in PythonAnywhere
2. Click **"Add a new web app"**
3. Select **"Manual configuration"** (not the Django wizard)
4. Choose **Python 3.10**
5. Enter your domain: `Tusar.pythonanywhere.com`

After creating the web app:

6. Scroll down to the **"WSGI configuration file"** section
7. Click on the WSGI file link to edit it
8. Replace ALL content with:

```python
import os
import sys

# Add your project directory to the sys.path
project_home = '/home/Tusar/mo-fakir-mohan'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set environment variables
os.environ['DJANGO_SETTINGS_MODULE'] = 'mo_fakir_mohan.settings'
os.environ['SECRET_KEY'] = 'your-secret-key-here'
os.environ['DEBUG'] = 'False'
os.environ['ALLOWED_HOSTS'] = 'Tusar.pythonanywhere.com'

# Serve static files and run Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

**Replace `yourusername` with your actual PythonAnywhere username and update the SECRET_KEY.**

---

## Step 7: Configure the Web App

In the **Web** tab, configure these settings:

### Source Code
- **Source code:** `/home/Tusar/mo-fakir-mohan`
- **Working directory:** `/home/Tusar/mo-fakir-mohan`

### Virtual Environment
- **Virtualenv:** `/home/Tusar/.virtualenvs/mo-fakir-mohan-env`

### Static Files
Add these static file mappings:

| URL | Directory |
|-----|-----------|
| `/static/` | `/home/Tusar/mo-fakir-mohan/staticfiles/` |
| `/media/` | `/home/Tusar/mo-fakir-mohan/media/` |
| `/books/` | `/home/Tusar/mo-fakir-mohan/books/` |

---

## Step 8: Collect Static Files

Back in your Bash console:

```bash
# Activate virtual environment
workon mo-fakir-mohan-env

# Navigate to project
cd ~/mo-fakir-mohan

# Set environment variables temporarily for this command
export SECRET_KEY='your-secret-key-here'
export DEBUG=False
export ALLOWED_HOSTS=Tusar.pythonanywhere.com

# Collect static files
python manage.py collectstatic --noinput
```

---

## Step 9: Run Migrations

```bash
# Run database migrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser
```

Follow the prompts to create an admin user (you'll need this to access `/admin/`).

---

## Step 10: Set File Permissions

```bash
# Make sure Django can write to media and staticfiles directories
chmod -R 755 ~/mo-fakir-mohan/media
chmod -R 755 ~/mo-fakir-mohan/staticfiles
chmod -R 755 ~/mo-fakir-mohan/books
```

---

## Step 11: Reload the Web App

1. Go back to the **Web** tab
2. Click the green **"Reload"** button for your web app
3. Wait a few seconds for it to reload

---

## Step 12: Test Your Website

Visit: `https://Tusar.pythonanywhere.com`

You should see your Mo Fakir Mohan website live!

Test these URLs:
- Homepage: `https://Tusar.pythonanywhere.com/`
- Admin: `https://Tusar.pythonanywhere.com/admin/`
- Books: `https://Tusar.pythonanywhere.com/books/`
- Gallery: `https://Tusar.pythonanywhere.com/gallery/`

---

## Step 13: (Optional) Set Up Environment Variables Permanently

To avoid setting environment variables every time, add them to your virtualenv's postactivate script:

```bash
# Edit the postactivate script
nano ~/.virtualenvs/mo-fakir-mohan-env/bin/postactivate
```

Add these lines:
```bash
export SECRET_KEY='your-secret-key-here'
export DEBUG=False
export ALLOWED_HOSTS=Tusar.pythonanywhere.com
```

Save and exit (Ctrl+X, then Y, then Enter).

---

## Troubleshooting

### Issue: 500 Internal Server Error
**Check error logs:**
- Go to **Web** tab → Scroll to **"Error log"**
- Click on the error log file link to see what went wrong

Common fixes:
- **Import errors:** Make sure all dependencies are installed: `pip install -r requirements.txt`
- **Static files not loading:** Verify static file paths in Web tab configuration
- **Database errors:** Run `python manage.py migrate` again

### Issue: Static files not loading
1. Make sure you ran `python manage.py collectstatic`
2. Verify the static file mappings in the Web tab are correct
3. Check that the paths exist: `ls ~/mo-fakir-mohan/staticfiles/`

### Issue: Media files not uploading
1. Check media directory permissions: `chmod 755 ~/mo-fakir-mohan/media`
2. Verify media URL mapping in Web tab

### Issue: Admin CSS not loading
Add this to your static files mapping in Web tab:
- URL: `/static/admin/`
- Directory: Find Django admin static path by running:
  ```bash
  python -c "import django; print(django.__path__[0])"
  ```
  Then add: `/home/Tusar/.virtualenvs/mo-fakir-mohan-env/lib/python3.10/site-packages/django/contrib/admin/static/admin/`

---

## Updating Your Website

When you make changes to your code:

```bash
# Navigate to project
cd ~/mo-fakir-mohan

# Pull latest changes
git pull origin main

# Install any new dependencies
pip install -r requirements.txt

# Collect static files (if static files changed)
python manage.py collectstatic --noinput

# Run migrations (if models changed)
python manage.py migrate
```

Then go to **Web** tab and click **"Reload"**.

---

## Using a Custom Domain (Optional)

If you have a custom domain:

1. In PythonAnywhere Web tab, click **"Add a new web app"**
2. Enter your custom domain name
3. Configure your domain's DNS to point to PythonAnywhere
4. Update `ALLOWED_HOSTS` to include your custom domain

---

## Database Notes

- Your project uses SQLite (`db.sqlite3`), which works fine on PythonAnywhere free tier
- For better performance, consider upgrading to PostgreSQL (requires paid account)
- SQLite database file location: `/home/yourusername/mo-fakir-mohan/db.sqlite3`

---

## Free Tier Limitations

PythonAnywhere free accounts:
- Must reload the web app every 3 months
- Limited to 1 web app
- 512MB disk space
- No always-on tasks (but web apps work fine)
- Access only to whitelisted external sites (GitHub is whitelisted)

---

## Quick Reference Commands

```bash
# Activate virtual environment
workon mo-fakir-mohan-env

# Navigate to project
cd ~/mo-fakir-mohan

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Create superuser
python manage.py createsuperuser

# Test Django shell
python manage.py shell

# Check Django deployment checklist
python manage.py check --deploy
```

---

## Security Checklist

- [x] DEBUG = False
- [x] SECRET_KEY is set and secure
- [x] ALLOWED_HOSTS is configured
- [ ] Consider using HTTPS (automatic on PythonAnywhere)
- [ ] Regular backups of database (`db.sqlite3`)
- [ ] Keep dependencies updated

---

## Support

- PythonAnywhere Help: https://help.pythonanywhere.com/
- Django Documentation: https://docs.djangoproject.com/
- PythonAnywhere Forums: https://www.pythonanywhere.com/forums/

---

**Your Mo Fakir Mohan portal is now live! 🎉**
