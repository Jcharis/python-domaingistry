# python-domaingistry
## DomainGistry - A Domain Name Generation Package For Python

[![Build Status](https://travis-ci.com/Jcharis/python-domaingistry.svg?branch=master)](https://travis-ci.com/Jcharis/python-domaingistry)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/domaingistry)

DomainGistry also comes with a CLI that you can use in the terminal as well as the package itself.

#### DomainGistry Suite of Tools
+ DomainGistry Pkg
+ Domain-Gistry CLI
+ DomainGistry.js

### Installation
+ To install DomainGistry, simply use pip or pipenv
```bash
pip install domaingistry 
```

#### Usage
```python
>>> from domaingistry import Domain
>>> d = Domain('example','common')
>>> d.generate()
```

#### Alternatively
```python
>>> from domaingistry import Domain
>>> d = Domain()
>>> d.name ='yourdomain'
>>> d.category = 'extra'
>>> d.generate()
```
These will generate a list of domain names using the name and category supplied. The categories include the following:

- common : for common domain names.This is the default
- new : for new domain name extensions eg ai,io
- extra : for extra domain name extensions eg. tv,app
- prefix : for prefixed domain names eg. adomain,thedomain,topdomain
- suffix: for suffixed domain names eg. domainify.com,domainly.com
- shuffled: this shuffles two or more terms given.

Let us see how to use each category

#### Get Common Domain Names
```python
>>> from domaingistry import Domain
>>> d = Domain('example')
>>> d.get_common()
```

#### Get New Domain Names
```python
>>> from domaingistry import Domain
>>> d = Domain('example')
>>> d.get_new()
```

#### Get Extra Domain Names
```python
>>> from domaingistry import Domain
>>> d = Domain('example')
>>> d.get_extra()
```

#### Get Prefixed Domain Names
```python
>>> from domaingistry import Domain
>>> d = Domain('example')
>>> d.get_prefix()
```

#### Get Suffixed Domain Names
```python
>>> from domaingistry import Domain
>>> d = Domain('example')
>>> d.get_suffix()
```

#### Get Shuffled Domain Names
```python
>>> from domaingistry import Domain
>>> d = Domain('example')
>>> d.get_shuffled()
```


#### Get Sub Domain Names
```python
>>> from domaingistry import Domain
>>> d = Domain('example')
>>> d.get_subdomain()
```

#### Get Sub Domain Names (Alternatively)
```python
>>> from domaingistry import Domain
>>> d = Domain('example')
>>> d.subdomain
```

### Saving Results To JSON

#### Get Common Domain Names
```python
>>> from domaingistry import Domain
>>> d = Domain('example','common')
>>> d.to_json()
```

## Working with the Command Line Interface(CLI) DomainGistry CLI
The CLI is made for easy of use in the terminal.
### Usage

#### Global Usage
```bash
domain-gistry --help
```

#### Local Usage If You Used The Repository to Install
```bash
python domain-gistry.py --help
```


#### Generating Domain Names
+ Generate the domain name, shows you the common domain name generated, saves to a json file
```bash
domain-gistry generate yourdomainname
```
or

```bash
domain-gistry generate "yourdomainname"
```

+ Generate the domain name by category and with the option to save
```bash
 domain-gistry generate yourdomainname --category common --save yes
```
or

```bash
domain-gistry generate "yourdomainname" --category common --save yes
```


#### Generating Domain Names By Category 
+ [Common | Extra | New | Prefixed | Suffixed | SubDomain]
+ Generate the domain name per category and show it on the console

#### Get Common Domain Names[.com,.org]
```bash
domain-gistry get-common "yourdomain name"

```
#### Get New Domain Names[.ai,.io]
```bash
domain-gistry get-new "yourdomain name"

```

#### Get Extra Domain Names[.tv,.media]
```bash
domain-gistry get-extra "yourdomain name"

```
#### Get Prefixed Domain Names[myexample.com,theexample.com]
```bash
domain-gistry get-prefix "yourdomain name"

```

#### Get Suffixed Domain Names[exampleworld.com,examplify.com]
```bash
domain-gistry get-suffix "yourdomain name"

```

#### Get Sub Domain Names[blog.exampleworld.com,app.examplify.com,support.examplify.com]
```bash
domain-gistry get-subdomain "yourdomain name"

```

#### Get All Domain Names
```bash
domain-gistry get-all "yourdomain name"

```




#### Author
+ Jesse E.Agbe(JCharis)
+ Jesus Saves @JCharisTech