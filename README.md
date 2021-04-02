## Django template - with bootstrap

### Rename your project

> Not tested after adding models

```
python rename.py oldName newName
```

### If you don't have flask installed run

```
pip3 install django
or
pip install django
```

### To start the server

```
python manage.py runserver
```

### Website will now be accessible on http://localhost:8000

## WIKI

### For å legge til ny side

```
lag side.html i webpage/templates/webpage/side.html
lag side.py i webpage/views/side.py
legg til path("side", side.side, name="side"), i webpage/urls.py

kopier kode fra index.py til side.py
	endre index.html til side.html
	for å sende data, bruk "context" parameter

kopier kode fra index.html til side.html
	endre title til "side"
	endre value på active element til "side"

endre webpage/templates/webpage/includes/navbar.html
	legg til nytt element i navbar
	kopier kode over
```

### For å legge til model

```
Se exampleModel.py for å stjele kode

kjør python manage.py makemigrations webpage
kjør python manage.py migrate

legg til admin.site.register(ModelNavn) i webpage/models.py

logg inn på http://localhost:8000/admin for å se på modellen
	admin:admin

Tips
	definer __str__ i model for at den skal se bra ut på admin-page
```
