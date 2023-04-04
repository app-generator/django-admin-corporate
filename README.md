# Django Admin Corporate

Modern template for **Django Admin Interface** coded on top of **Corporate UI Dashboard**, an open-source `Bootstrap 5` design from [Creative-Tim](https://www.creative-tim.com/?AFFILIATE=128200).

> Actively supported by [AppSeed](https://appseed.us/) via `Email` and `Discord`.

<br />

> KIT: https://github.com/creativetimofficial/corporate-ui-dashboard

<br />

## Features: 

- [Django Corporate Dashboard](#) - `Product` that uses the library
  - `Features`: Fully-configured, `CI/CD` via Render
- **UI Kit**: [Corporate Dashboard BS5](https://www.creative-tim.com/product/corporate-ui-dashboard?AFFILIATE=128200) by `Creative-Tim`
- **Sections Covered**: 
  - `Admin Section`, reserved for `superusers`
  - `All pages` managed by `Django.contrib.AUTH`
  - `Registration` page
  - `Misc pages`: colors, icons, typography, blank-page 

<br />

![Django Corporate Dashboard](https://user-images.githubusercontent.com/51070104/229719846-cfe96c5c-89c2-4ea0-89a9-7be69ebbb228.png)

<br>

## Why `Django Admin Soft`

- Modern [Bootstrap 5](https://www.admin-dashboards.com/bootstrap-5-templates/) Design
- `Responsive Interface`
- `Minimal Template` overriding
- `Easy integration`

<br />

## How to use it

<br />

> **Install the package** via `PIP` 

```bash
$ pip install django-admin-corporate
// OR
$ pip install git+https://github.com/app-generator/django-admin-corporate.git
```

<br />

> Add `admin_corporate` application to the `INSTALLED_APPS` setting of your Django project `settings.py` file (note it should be before `django.contrib.admin`):

```python
    INSTALLED_APPS = (
        ...
        'admin_corporate.apps.AdminCorporateDashboardConfig',
        'django.contrib.admin',
    )
```

<br />

> Add `LOGIN_REDIRECT_URL` and `EMAIL_BACKEND` of your Django project `settings.py` file:

```python
    LOGIN_REDIRECT_URL = '/'
    # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

<br />

> Add `admin_corporate` urls in your Django Project `urls.py` file

```python
    from django.urls import path, include

    urlpatterns = [
        ...
        path('', include('admin_corporate.urls')),
    ]
```

<br />

> **Collect static** if you are in `production environment`:

```bash
$ python manage.py collectstatic
```

<br />

> **Start the app**

```bash
$ # Set up the database
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Create the superuser
$ python manage.py createsuperuser
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
```

Access the `admin` section in the browser: `http://127.0.0.1:8000/`

<br />

## How to Customize 

When a template file is loaded in the controller, `Django` scans all template directories starting from the ones defined by the user, and returns the first match or an error in case the template is not found. 
The  theme used to style this starter provides the following files: 

```bash
< LIBRARY_ROOT >                      # This exists in ENV: LIB/admin_corporate
   |
   |-- templates/                     # Root Templates Folder 
   |    |          
   |    |-- accounts/       
   |    |    |-- login.html           # Sign IN Page
   |    |    |-- register.html        # Sign UP Page
   |    |
   |    |-- includes/       
   |    |    |-- footer.html          # Footer component
   |    |    |-- sidebar.html         # Sidebar component
   |    |    |-- navigation.html      # Navigation Bar
   |    |    |-- scripts.html         # Scripts Component
   |    |
   |    |-- layouts/       
   |    |    |-- base.html            # Masterpage
   |    |    |-- base-fullscreen.html # Masterpage for Auth Pages
   |    |
   |    |-- pages/       
   |         |-- index.html           # Dashboard page
   |         |-- profile.html         # Settings  Page
   |         |-- *.html               # All other pages
   |    
   |-- ************************************************************************
```

When the project requires customization, we need to copy the original file that needs an update (from the virtual environment) and place it in the template folder using the same path. 

For instance, if we want to customize the `footer.html` these are the steps:

- `Step 1`: create the `templates` DIRECTORY inside your app 
- `Step 2`: configure the project to use this new template directory
  - Edit `settings.py` TEMPLATES section 
- `Step 3`: copy the `footer.html` from the original location (inside your ENV) and save it to the `YOUR_APP/templates` DIR
  - Source PATH: `<YOUR_ENV>/LIB/admin_corporate/includes/footer.html`
  - Destination PATH: `YOUR_APP/templates/includes/footer.html`
- Edit the footer (Destination PATH)    

At this point, the default version of the `footer.html` shipped in the library is ignored by Django.

In a similar way, all other files and components can be customized easily.

<br />

## Recompile SCSS  

The SCSS/CSS files used to style the Ui are saved in the `static` directory. 
In order to update the Ui colors (primary, secondary) this procedure needs to be followed. 

```bash
$ yarn  # Install modules            
$ # Edit variables                                       
$ vi admin_corporate/static/scss/corporate-ui-dashboard/_variables.scss 
$ gulp # SCSS to CSS translation
```

The `_variables.scss` content defines the `primary` and `secondary` colors: 

```scss
$primary:       #774dd3 !default; // EDIT for customization
$secondary:     #64748b !default; // EDIT for customization
$info:          #55a6f8 !default; // EDIT for customization
$success:       #67c23a !default; // EDIT for customization
$warning:       #f19937 !default; // EDIT for customization
$danger:        #ea4e3d !default; // EDIT for customization
```

<br />

---
**Django Admin Corporate** - Modern Admin Interface provided by **[AppSeed](https://appseed.us/)**
