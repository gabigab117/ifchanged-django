# `{% ifchanged %}` — Django template tag

Ce projet illustre l'utilisation du tag `{% ifchanged %}` dans un template Django.

## Ce que fait `{% ifchanged %}`

`{% ifchanged %}` s'utilise à l'intérieur d'un `{% for %}`. Il n'affiche son contenu **que si la valeur a changé** depuis l'itération précédente.

Ici, les articles sont triés par date. Le titre de la date n'est affiché qu'une seule fois, avant le premier article de chaque jour :

```html
{% for post in posts %}
  {% ifchanged post.created_at %}
    <h2>{{ post.created_at }}</h2>
  {% endifchanged %}
  <article>
    <h3>{{ post.title }}</h3>
    <p>{{ post.content }}</p>
  </article>
{% endfor %}
```

La vue reste simple — elle passe juste la liste des articles :

```python
def post_list(request):
    posts = Post.objects.all()
    return render(request, "blog/post_list.html", {"posts": posts})
```

---

## Sans `{% ifchanged %}`, que faudrait-il faire ?

Il faudrait regrouper les articles par date **dans la vue**, puis faire une **double boucle** dans le template.

**Vue :**

```python
def post_list(request):
    posts = Post.objects.all()

    grouped = {}
    for post in posts:
        grouped.setdefault(post.created_at, []).append(post)

    return render(request, "blog/post_list.html", {"grouped_posts": grouped})
```

**Template :**

```html
{% for date, posts in grouped_posts.items %}
  <h2>{{ date }}</h2>
  {% for post in posts %}
    <article>
      <h3>{{ post.title }}</h3>
      <p>{{ post.content }}</p>
    </article>
  {% endfor %}
{% endfor %}
```

`{% ifchanged %}` évite tout ça : pas de `groupby`, pas de double boucle, pas de données restructurées.
# ifchanged-django
