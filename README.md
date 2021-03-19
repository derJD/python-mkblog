# python-mkblog

[![PyPI version](https://badge.fury.io/py/mkblog.svg)](https://badge.fury.io/py/mkblog)
[![PyPI downloads](https://img.shields.io/pypi/dm/mkblog)](https://pypi.org/project/mkblog/)
[![pylint](https://gitlab.der-jd.de/python/mkblog/-/jobs/artifacts/main/raw/pylint.svg?job=lint:pylint)](#python-mkblog)

This is yet another MkDocs plugin adding basic blogging functionality.
With this plugin you store your blogposts in a separate `blog` directory.

![example tree](/img/mkblog_example_tree.jpg)

As you can see it doesn't matter how you store your posts in the `blog` directory.
Instead of directory structures, this plugin relies on markdown Metadata `date`.

![example page](/img/mkblog_example_page.jpg)

Use this plugin alongside with the plugin [awesome-pages](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin).
`awesome-pages` will take care of generating the whole nav bar, so you (or this blog plugin) don't have to do it.

## Features

* Extra directory for your blog posts
* Utilizing markdown meta `date`
* No need for date directories and subdirectories and sub sub directories

## Installation

* from pypi: `pip install python-mkblog`
* from github: `pip install git+https://github.com./derJD/python-mkblog.git`

### Local Build

```sh
git clone https://github.com/derJD/python-mkblog.git
cd python-mkblog
pip install .
```

## Usage

There is an complete [example](/example/) directory.
Take a look by cloning this repository and issuing `mkdocs serve -f example/mkdocs.yml`

**Most basic example `mkdocs.yml`**:

```yaml
---

site_name: basic test page

plugins:
  - awesome-pages
  - mkblog

```

**This example uses `material theme` to make the site prettier and it uses `discus extra` to give people the opportunity to leave a comment**:

```yaml
---

site_name: test page with comments

theme:
  name: material
  features:
    - tabs
  palette:
    primary: green
    accent: yellow

plugins:
  - mkblog
  - search
  - awesome-pages

extra:
  disqus: <YOUR DISQUS TOKEN>

```

**You can configure the name of your blog directory**:

```yaml
---

plugins:
  - mkblog:
      blog_dir: bloggiemcblogger

```

## Documentation

* [General documentation](https://der-jd.de/python-mkblog/intro/)
* [Reference](https://der-jd.de/python-mkblog/reference/mkblog/)

## License

* Code released under [MIT License](https://opensource.org/licenses/MIT)

## Author

* [derJD](https://github.com/derJD/)
