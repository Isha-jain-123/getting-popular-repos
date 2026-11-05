# Getting Popular Repos

A Django web app that finds the most popular repositories in a GitHub organisation and lists their top committers. It uses the GitHub API (via [PyGithub](https://github.com/PyGithub/PyGithub)) to search repos, ranks them by fork count, and then walks through each repo's commit history to count commits per author.

## How it works

1. Visit `/gitmining/?org_name=<org>&repo_count=<n>&comm_count=<m>`
2. The app searches all repositories under `<org>`, sorts them by forks (most forked first) and picks the top `n`.
3. For each repository it counts every committer's commits and keeps the top `m`.
4. The result is rendered as an HTML table using [json2html](https://github.com/softvar/json2html).

## Project structure

```
ocs/            Django project settings (settings.py, urls.py, wsgi.py, asgi.py)
gitmining/      Django app
  ├── ocs.py    Core logic: queries the GitHub API and builds the result dict
  ├── views.py  Receives the request, calls ocs.py, returns the HTML table
  └── urls.py   Routes /gitmining/ to the view
manage.py       Django management script
```

## Running locally

```bash
pip install django PyGithub json2html
```

Before starting the server, open `gitmining/ocs.py` and replace the token string inside `Github(...)` with your own [GitHub personal access token](https://github.com/settings/tokens):

```python
g = Github("YOUR_TOKEN_HERE")
```

Then:

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/gitmining/?org_name=google&repo_count=5&comm_count=3` to try it out.
