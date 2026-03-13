# Mo Fakir Mohan - Digital Heritage Portal

## Project Overview

A Django-based digital heritage portal dedicated to **Fakir Mohan Senapati** (1843-1920), the revered Odia poet, novelist, and philosopher. This portal preserves and showcases his literary works, life history, and legacy in a bilingual (Odia & English) format.

---

## Technical Stack

| Component | Technology |
|-----------|------------|
| **Framework** | Django 6.0.1 |
| **Language** | Python |
| **Database** | SQLite3 |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Fonts** | Google Fonts (Noto Sans Oriya) |
| **File Storage** | Git LFS (for PDF files) |
| **Version Control** | Git & GitHub |

---

## Project Structure

```
mo_fakir_mohan/
├── mo_fakir_mohan/          # Main Django project settings
│   ├── settings.py          # Django configuration
│   ├── urls.py              # Root URL routing
│   ├── asgi.py              # ASGI config
│   └── wsgi.py              # WSGI config
│
├── portal/                  # Main application
│   ├── models.py            # Database models (7 models)
│   ├── views.py             # View functions (14 views)
│   ├── urls.py              # URL patterns
│   ├── admin.py             # Django admin configuration
│   ├── templates/portal/    # HTML templates (11 files)
│   ├── migrations/          # Database migrations
│   └── static/              # Static files
│
├── books/                   # Fakir Mohan's original PDF books (9 files)
│   ├── Chha Mana Atha Guntha by Fakir Mohan Senapati (Odia).pdf
│   ├── Rebati FM.pdf
│   ├── Mamu FM.pdf
│   ├── Patent medicine FM.pdf
│   ├── Garudi mantra FM.pdf
│   ├── Birei bisala FM.pdf
│   ├── Dakamunis FMU.pdf
│   ├── RP Ananta FM.pdf
│   └── fakir-mohan-senapati.jpg
│
├── media/                   # User-uploaded content
├── static/                  # Project-wide static files
├── templates/               # Global templates
├── manage.py                # Django management script
└── .gitattributes           # Git LFS configuration
```

---

## Database Models

### 1. **Category**
- Organizes content into categories
- Bilingual support (Odia & English names)
- Auto-generated slug

### 2. **Article**
- Articles about Fakir Mohan Senapati's life, works, and legacy
- Rich text content in Odia & English
- Featured article support
- Image attachments

### 3. **Document**
- Downloadable PDF documents
- **Login required** for downloads
- Download count tracking
- Category-based organization

### 4. **Book**
- Books written by Fakir Mohan Senapati
- **Login required** for downloads
- File path tracking (stored in `/books/` directory)
- Download statistics

### 5. **GalleryImage**
- Photo gallery images
- Featured image support
- Odia & English captions

### 6. **TimelineEvent**
- Chronological events from Fakir Mohan's life
- Year-based ordering
- Bilingual descriptions

### 7. **UserProfile**
- Extended user profile (OneToOne with Django User)
- Phone number & bio fields

---

## URL Routes

| Route | View | Description |
|-------|------|-------------|
| `/` | `home` | Homepage with featured content |
| `/about/` | `about` | Biography & timeline |
| `/works/` | `works` | Literary works |
| `/legacy/` | `legacy` | Legacy & influence |
| `/books/` | `books_list` | List of all books |
| `/books/<id>/download/` | `download_book` | **Login required** |
| `/documents/` | `documents_list` | Document library |
| `/documents/<id>/download/` | `download_document` | **Login required** |
| `/article/<slug>/` | `article_detail` | Article detail page |
| `/gallery/` | `gallery` | Photo gallery |
| `/register/` | `register_view` | User registration |
| `/login/` | `login_view` | User login |
| `/logout/` | `logout_view` | User logout |
| `/admin/` | Django Admin | Admin dashboard |

---

## Key Features

### ✅ Content Management
- Bilingual content (Odia & English)
- Django Admin integration for all models
- Rich text articles with categories
- Featured content highlighting

### ✅ User Authentication
- User registration & login
- Session management
- Protected downloads (login required)
- User profiles with extended information

### ✅ Digital Library
- 9 PDF books by Fakir Mohan Senapati
- Git LFS for large file versioning
- Download tracking & statistics
- Category-based filtering

### ✅ Media & Gallery
- Photo gallery with featured images
- Timeline of life events
- Article images support

### ✅ Odia Language Support
- Odia Unicode fonts (Noto Sans Oriya)
- Bilingual field labels in admin
- Odia navigation menu
- Traditional Odia calendar year in footer (୨୦୨୫)

---

## Git & Version Control

### Repository
- **Remote**: https://github.com/Tusarkanta-07/mo-fakir-mohan
- **Branch**: `main` (tracking `origin/main`)

### Git LFS Configuration
Large PDF files are tracked using Git LFS:
```
*.pdf filter=lfs diff=lfs merge=lfs -text
```

### Commit History
1. `9ea9148` - "Remove" (latest)
2. `eaf41cc` - Add Git LFS tracking
3. `8c8296b` - Initial commit

### Pushed Content
- 8 LFS objects (44 MB total)
- 67 Git objects
- All PDF books uploaded successfully

---

## Admin Configuration

All models are registered with custom admin configurations:

| Model | Admin Features |
|-------|----------------|
| Category | Prepopulated slug, search |
| Article | Prepopulated slug, filters, ordering |
| Document | Filters, search, download count |
| GalleryImage | Filters, featured toggle |
| TimelineEvent | Year-based ordering |
| UserProfile | User search, phone display |
| Book | Filters, download statistics |

---

## Settings & Configuration

### Key Settings
- **DEBUG**: `True` (development mode)
- **SECRET_KEY**: Django-generated secure key
- **DATABASE**: SQLite3 (`db.sqlite3`)
- **MEDIA_URL**: `/media/`
- **STATIC_URL**: `/static/`
- **BOOKS_DIR**: `/books/`
- **LOGIN_URL**: `/login/`
- **LOGIN_REDIRECT_URL**: `/`

### Installed Apps
- `django.contrib.admin`
- `django.contrib.auth`
- `django.contrib.contenttypes`
- `django.contrib.sessions`
- `django.contrib.messages`
- `django.contrib.staticfiles`
- `portal` (custom app)

---

## Templates

| Template | Purpose |
|----------|---------|
| `base.html` | Base template with navigation & footer |
| `home.html` | Homepage with featured content |
| `about.html` | Biography & timeline |
| `works.html` | Literary works listing |
| `legacy.html` | Legacy content & gallery |
| `books.html` | Books listing |
| `documents.html` | Document library |
| `article_detail.html` | Single article view |
| `gallery.html` | Photo gallery |
| `login.html` | Login form |
| `register.html` | Registration form |

---

## Future Enhancements

- [ ] Production deployment configuration
- [ ] PostgreSQL database migration
- [ ] Advanced search functionality
- [ ] Book reader (inline PDF viewing)
- [ ] Comment system for articles
- [ ] Social media sharing
- [ ] Responsive design improvements
- [ ] SEO optimization
- [ ] Analytics integration

---

## Project Status

**✅ Completed:**
- Django project setup
- All database models created & migrated
- User authentication system
- Admin panel configuration
- 11 HTML templates
- Git LFS for PDF storage
- GitHub repository pushed
- 9 PDF books uploaded

**🔄 In Progress:**
- Static files (CSS, JS)
- Content population (articles, timeline events)

---

## Contact & Repository

- **GitHub**: https://github.com/Tusarkanta-07/mo-fakir-mohan
- **Framework**: Django 6.0.1
- **Language**: Python, Odia, English

---

*This project is dedicated to preserving and promoting Odia literature and culture through digital means.*
