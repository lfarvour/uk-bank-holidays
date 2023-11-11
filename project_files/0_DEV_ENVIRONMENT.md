# Local Development Environment

> My friend Habiba hates when I start counting at zero. This project was originally designed to support her learning as the intern on our security operations team, thus I start counting at zero as an homage to my dedication to being a silly, obstinate goose.

* [Skip to the Table of Things](0_DEV_ENVIRONMENT.md#table-of-things)

## WORDS: Installing the Language

To get any python project up and running, folks will at minimum need Python installed on their computers. It is recommended to stick to the latest version (3.10 at time of writing). That being said, one can use whichever version of python makes most sense for their use case. 

Most of the libraries/packages that are used in this project will be "Living off the Land" (LOL). That is, you can use libraries/packages that come in a vanilla install. The one exception is `requests`, which is not vanilla but probably the most widely used non-vanilla python package for HTTP-based snek communication. 

`requests` is the reason I recommend using virtual environments up front, because if you install `requests` in your base install of python, it will be included in every future python project you use, whether you need it or not. And as cyber defenders know, `least needed access` is a fundamental security requirement.

## WORDS: Why We Install More Stuff
While having Python installed is technically sufficient to write code, it fails to adopt tools and practices that assist modern developers in moving fast and getting things done. 

For this reason, I offer the following listing of my local development technology stack. Getting all of these tools working together takes a bit of time, elbow grease, and plenty of Google searching. Perhaps even asking ChatGPT if you get stuck ;)

In particular, setting up `pyenv virtualenv` (virtual environments) is quite sassy. If you encounter a brick wall while setting up your system, I recommend sticking to `venv` for virtual environment creation and management, as it built in natively to Python core.

## Table of Things

| Development Terminology | Recommended Tool | Purpose | Words About It |
| -- | -- | -- | -- |
| Terminal | Windows Subsystem for Linux (WSL) <br><br>*OR* whatever is native to your Linux/Unix based OS | The terminal is the text-based interface for your computer filesystem. It also runs helpful binaries such as apt/yum/homebrew that allow easy installation of binaries packaged by manufacturers and [load bearing internet people (LBIP)](http://esr.ibiblio.org/?p=8383). | I hope to never become a load bearing internet person (LBIP). |
| Python | Python 3.10 | Python is the number one programming language among cybersecurity folks. While other languages are just as capable, Python is what has taken hold due to its accessibility to both less-deep and deep nerds. | i love snek. |
| PIP | Comes with Python | PIP is the Python package manager. The default install of python uses a remote package manager called PyPi (https://pypi.org/). Organizations often have their own internal remote package management solutions that allow the creation of custom, potentially proprietary, Python packages that do special things. | As a defender, I try to stick to living off the land -- only use Python's built-in packages. The one that I usually compromise for is [the `requests` library](https://pypi.org/project/requests/) because it does all the heavy lifting for web-based communications, whereas built in `urlllib3` requires a lot of work to do what `requests` does natively. |
| Integrated Development Environment (IDE) | Visual Studio Code |  IDE's provide everything a person needs to code stuff. They provide suggestions, lint (i.e. grammar check), run tests, enable debugging, and are just generally helpful development pals. | This free IDE is the best thing Microsoft has ever done for the world. It supports development in just about any language you can think of and allows open source development of extensions<sup>1</sup> that make life even easier |
| Virtual Environment | pyenv virtualenv <br><br> *OR* venv (built into Python base install) | Virtual environments allow developers to create environments for development projects that are separate from the base installation of Python (or any other language). Virtual environments are handy because they ensure that developers can test code using any version of Python they need (e.g. backwards compatibility testing). They also keep the package environments of different projects separate, which ensures that during packaging only minimum necessary packages are included. | Using virtual environments for projects like this one is definitely overkill. However, the process of learning what virtual environments are and how they work is invaluable for when a person is juggling multiple projects with lots of different package requirements, as can quickly happen when code starts flowing. |

<sup>1</sup> Practice safe installation of unknown code. VSCode does not sandbox extensions, and they *can* be used to deliver malware. That being said, extensions are generally signed and attributed, discouraging malicious behavior. [This StackOverflow discussion offers more insights](https://stackoverflow.com/questions/67493012/how-safe-are-extensions-in-visual-studio-code).

# Visual Studio Code Extensions

| Extension | Author | Description |
| -- | -- | -- |
| Pylint | Microsoft | Grammar checking, for code! Has a configuration file that allows setting tolerances for grammatical errors. For example, setting maximum line lengths to improve code readabillity. |
| Python Extension Pack | Don Jaymanne | Collection of handy Python extensions, including tab completion, auto docstring, and AI assist for development |
| Gitlens | Git Kraken | Awesome visualizer for git local and remote source code management visualization |
