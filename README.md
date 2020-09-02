# DRF-rest-api-starter-pack

A Django Rest framework based REST API. Django makes creating REST APIs fast and easy. The features are vast and quickly configurable. 

### Major Packages Installed
---
- Django
- Django Rest Framework
- DRF-yasg 
- django-filter
- Gunicorn

### Features
---
- REST API with CRUD functionality for all the provided models.
- Sqlite3 DB is used for backend, can be reconfigured to Postgres.
- Browsable API endpoints for visual navigation. 
- Swagger and Redoc Documentation and testing for URL endpoints. 
- Deployement config for Heroku.
- List view Filtering, pagination and searching. 
- Strict REST standards. 
- Token based authentication. 
- I18n language agnostic translation and everything else Django provides. 

### How to use? 
---
- Git clone this repo.
```bash
git clone https://github.com/Trevahok/DRF-rest-api-starter-pack.git
```

- Navigate to the project root and create virtualenv using:
```bash
cd DRF-rest-api-starter-pack/
python3 -m venv venv
```
- Install packages in virtualenv:
```bash
pip3 install -r requirements.txt
```
- Create new model in   `mainapp/models.py`. 
```py
class Post(models.Model):  
    title = models.CharField(max_length=1024)
```
- Create serializer for the model in   `mainapp/serializers.py`.
```py
class PostSerializer(
        serializers.HyperlinkedModelSerializer
    ):
    class Meta:
        model = Post
        fields = "__all__"
```
- (Optional) Add filtering rules. More about it at: `https://django-filter.readthedocs.io/` 
```py
class PostFilter(filters.FilterSet):
    search = filters.NumberFilter(field_name="title", lookup_expr='in')
    class Meta:
        model = Post
        fields  = [ 'title' , 'text']
```
- Create viewset for the model in `mainapp/views.py`. 
```py
class PostViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing post instances.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # if you have filtering class:
    filterset_class = PostFilter
    # else:
    filterset_fields = '__all__'
```
- Create url router for the model in `mainapp/urls.py`.
```py
router = DefaultRouter()
router.register(r'posts', PostViewSet)
```
- Make migrations for DB and create Admin superuser.

```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
```

- Run the development server using: 
```bash
python3 manage.py runserver 0:8000
```
- Witness the power of DRF with fully functional browsable REST API with pagination, JWT authentication, Swagger and Redoc documentation and more.


### Endpoints
---

|URL |  Purpose |
|:---| ---:|
|/swagger| Swagger documentation|
|/redoc | Redoc documentation|
|/  | API root with browsable models and filtering|
|/?format=json | JSON results|
|/?format=api | HTML browsable view|
|/token | Obtain Token for Auth|

