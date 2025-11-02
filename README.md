# E-commerce (MAC Shop)

Lightweight Django-based e-commerce example app (shopping/catalog, cart, checkout, order tracking) originally built as a learning/demo project. The repo contains a small online store with two Django apps: `shop` (product catalog, cart, checkout) and `blog` (example blog pages).

## Features

- Product catalog by category with image support
- Product detail (product view) pages
- Simple cart interactions (Add to Cart / Buy Now) using client-side JS
- Checkout flow that creates an order record
- Order tracker endpoint that returns JSON for order status
- Contact form that saves messages to the database

## Repo layout (important paths)

- `MAC/manage.py` - Django project entry point
- `MAC/MAC/settings.py` - Django settings
- `MAC/shop/` - Shop app (models, views, templates, static)
- `MAC/blog/` - Blog app (example content)
- `MAC/media/` - Uploaded product images (if any)
- `MAC/db.sqlite3` - SQLite database used by the project (if present)

## Prerequisites

- Python 3.8+ (3.10/3.11 recommended)
- pip
- (Optional) virtual environment tool: `venv` or `virtualenv`

Note: This README includes PowerShell commands for Windows (the development environment where this project is used). Adjust commands for other shells/OS as needed.

## Quick start (Windows PowerShell)

1. Open PowerShell and change to the project directory (where `manage.py` lives):

```powershell
cd 'C:\Users\srish\OneDrive\Desktop\Python\E\MAC'
```

2. Create and activate a virtual environment (recommended):

```powershell
py -3 -m venv .venv; .\.venv\Scripts\Activate.ps1
```

3. Install dependencies. If a `requirements.txt` is not present, install Django (example):

```powershell
pip install django
# If there's a requirements file: pip install -r requirements.txt
```

4. Run migrations and start the dev server:

```powershell
py -3 manage.py migrate
py -3 manage.py runserver
```

5. Open your browser at http://127.0.0.1:8000/ to view the site.

## Notes on media & static files

- Product images are stored under `MAC/media/shop/images` (if you add images using the admin or via the filesystem). Ensure `MEDIA_ROOT` and `MEDIA_URL` are configured in `MAC/settings.py` when running in development.
- Static files (CSS/JS) are in `MAC/shop/static/` and `MAC/blog/static/`.

## Important implementation details

- The `shop.product` model uses `product_id = AutoField(primary_key=True)`. Templates and views should use `product.product_id` or `product.pk` to reference the primary key. If you see a "Reverse for 'ProductView' with arguments '('',)' not found" error, it's usually because templates are still using `product.id` instead of the model's PK field.

## Recommended changes & tips

- Prefer `product.pk` in templates and view lookups for portability (works whether the primary key is `id` or another field):

	- Template: `{% url 'shop:ProductView' product.pk %}`
	- View: `get_object_or_404(product, pk=myid)`

- Commit any media files or large binaries to a separate storage (Git LFS or cloud storage) rather than the repo.

## Running tests

There are no automated tests included in the repo currently. To add tests, create test modules in each app under `tests.py` or `tests/` and use Django's test runner:

```powershell
py -3 manage.py test
```

## Contributing

1. Fork the repo and create a feature branch.
2. Make changes, run the app locally, and ensure there are no obvious template/view errors.
3. Open a pull request with a clear description of changes.

## License

This project does not include an explicit license file. Add a LICENSE file if you intend to make the repository open-source and want to grant permissions (MIT, Apache 2.0, etc.).

## Contact / Questions

If you need help with the project, provide context (error messages, traceback, which page triggered the error) and I'll help diagnose issues.

---
