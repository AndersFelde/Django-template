## Django template - with bootstrap

### Rename your project

> Not tested after adding models! Make sure to do it early in the project
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

- create `page.html` in `webpage/templates/webpage/`
- create `page.py` in `webpage/views/`
- add `path("page", page.page, name="page")`, in `webpage/urls.py`
	- `from .views import page`

- copy code from `index.py` to `page.py`
	- change _index.html_ to _page.html_
	- to send data, use `context` parameter in `render()`
		- pass a dictionary `{test: "123"}`
		- access in html with `{{ test }}`
			- will output `123`

- copy code from `index.html` to `page.html`
	- change `title` to _page_
	- change value of active element to _page_
		- hidden input element at the top

- change `webpage/templates/webpage/includes/navbar.html`
	- add a new element in navbar

> For more information about html template visit: [Templates | Django documentation](https://docs.djangoproject.com/en/3.1/topics/templates/)

***

### Adding a new model


- create a new file "testModel.py" in webpage/submodels/
	- look at exampleModel.py to steal code

- import model in webpage/models.py
	- `from .submodels.testModel1 import modelName`

- run `python manage.py makemigrations webpage`
- run `python manage.py migrate`

- add admin.site.register(modelName) in webpage/admin.py
	- `from .submodels.testModel1 import modelName`


- log in to http://localhost:8000/admin to view the model
>admin:admin


***

Tips:
- define `__str__` in a model to make it look better on the admin page
	- make it return the name or id of the model
