# Writing Sphinx documentation

This project is set up to produce documentation using [Sphinx][sphinx]; this page should give you a quick overview on
how to write documentation for it. If you're looking for information on how to write **good** documentation take a look
[here][writethedocs]; for Agile projects, consider [documenting late][agilemodeling] as well.

```{contents}
:local:
:depth: 2
```

## Why should I bother? And why Sphinx?

Keeping as much of the documentation in a centralised location is a good thing — it means contributors, users, and
anyone else can quickly find as much information as they need to understand and/or run what you've done.

Sphinx is a Python-based package to compile documentation into different formats, including HTML. This means you can
write your documentation and, with a single terminal command, build it into a searchable website.

It's widely used, such as for the documentation of the [pandas][pandas], and [PyTorch][pytorch] Python packages as well
as many [others][sphinx-examples], and is highly customisable with different extensions, and themes. Included with this
project is:

- Support for both [reStructuredText (ReST)][rest], and [ReST-enabled Markdown][myst];
- Automatic building of documentation from Python docstrings; and
- Support for [ReStructuredText][docstring-rst], [NumPy][docstring-numpy], or [Google][docstring-google] docstring
  formats.

### Creating a searchable website

To create a website with your documentation, run the following command in your terminal at the top-level of this
project:

```shell
make docs
```

This should create an HTML version of your documentation accessible from `docs/_build/index.html`.

## Writing in reStructuredText

Sphinx provides [good documentation][sphinx-rst] on writing in ReST — we would highly recommend reading that for
guidance. We will cover automatically creating docstrings in the next subsection.

### Automatically creating docstring documentation (ReST)

Let us say that `src/__init__.py` has functions called `hello` and `world` imported into it, and both have docstrings.
To automatically generate docstring documentation, create a ReST file, and add the following line to reference the
`src` module:

```rest
.. currentmodule:: src
```

Then, elsewhere in the body, call the [`autosummary`][sphinx-autosummary] directive to generate the docstrings as ReST
stub files.

```rest
.. autosummary::
    :toctree: api/

    hello
    world

```

This will create something similar to the pandas [API reference][pandas-api-reference].

## Writing in ReST-enabled Markdown

We use the [`myst-parser`][myst] package (MyST) to write Markdown that can also include ReST elements; the package
[documentation][myst] is detailed, so we would recommend reviewing it. We will cover some of the more widely used
elements in the following subsections.

### Embedding ReST directives

Most ReST directives can be embedded into MyST Markdown — see [here][myst-rst-directives] for further details.

### Automatically creating docstring documentation (MyST Markdown)

Let us say that `src/__init__.py` has functions called `hello` and `world` imported into it, and both have docstrings.
To automatically generate docstring documentation, create a Markdown file, and add the following line to reference the
`src` module:

````md
```{eval-rst}
.. currentmodule:: src
```
````

Then, elsewhere in the body, call the [`autosummary`][sphinx-autosummary] directive to generate the docstrings as ReST
stub files.

````md
```{eval-rst}
.. autosummary::
    :toctree: api/

    hello
    world

```
````

### Including Markdown files outside the `docs` folder

MyST lets you include Markdown files outside the `docs` folder [easily][myst-include].

If a Markdown file (`../example.md`) only contains links that do not reference anything else in this project (including
images), create a Markdown file within the `docs` folder with the following lines:

````md
```{include} ../example.md
```
````

However, if it includes relative links referencing other files in this project (including images), we need to tell MyST
what those links actually refer. For example, if the relative link is `../hello/world.md`, we need to create a Markdown
file within the `docs` folder with the following lines:

````md
```{include} ../example.md
:relative-docs: ../hello
:relative-images:
```
````

[agilemodeling]: http://agilemodeling.com/essays/documentLate.htm
[docstring-google]: http://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings
[docstring-numpy]: https://numpydoc.readthedocs.io/en/latest/format.html
[docstring-rst]: https://www.python.org/dev/peps/pep-0287/
[myst]: https://myst-parser.readthedocs.io/
[myst-include]: https://myst-parser.readthedocs.io/en/latest/using/howto.html#include-a-file-from-outside-the-docs-folder-like-readme-md
[myst-rst-directives]: https://myst-parser.readthedocs.io/en/latest/using/syntax.html#directives-a-block-level-extension-point
[pandas]: https://pandas.pydata.org/docs/
[pandas-api-reference]: https://pandas.pydata.org/docs/reference/index.html
[pytorch]: https://pytorch.org/docs/stable/index.html
[rest]: https://docutils.readthedocs.io/en/sphinx-docs/user/rst/quickstart.html
[sphinx]: https://www.sphinx-doc.org/
[sphinx-autosummary]: https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html
[sphinx-examples]: https://www.sphinx-doc.org/en/master/examples.html
[sphinx-rst]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html
[writethedocs]: https://www.writethedocs.org/guide/writing/beginners-guide-to-docs/
