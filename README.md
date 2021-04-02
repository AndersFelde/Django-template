## Django template - with bootstrap

### Rename your project

> Not tested after adding models!

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

> Website will now be accessible on http://localhost:8000

## WIKI

### Add a new page

```
- create side.html in webpage/templates/webpage/
- create side.py in webpage/views/side.py
- add path("side", side.side, name="side"), in webpage/urls.py

- copy code from index.py to side.py
	change "index.html" to "side.html"
	to send data, use "context" parameter in render()

- copy code from index.html to side.html
	change title to "side"
	change value of active element to "side"

- change webpage/templates/webpage/includes/navbar.html
	add a new element in navbar
```

### Adding a new model

```
- create a new file "testModel.py" in webpage/submodels/

look at exampleModel.py to steal code

- import model in webpage/models.py
	from .submodels.testModel1 import modelName

- run python manage.py makemigrations webpage
- run python manage.py migrate

- add admin.site.register(modelName) i webpage/models.py
	from .submodels.testModel1 import modelName

l- og in to http://localhost:8000/admin to view the model
	admin:admin

Tips
	define __str__ in a model to make it look better on the admin page
		make it return the name or id of the model
```
