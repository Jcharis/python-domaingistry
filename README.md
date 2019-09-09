# python-domaingistry
DomainGistry - A Domain Name Generation Package For Python

### Installation

```bash
pip install domaingistry 
```

#### Usage
```python
>>> from domaingistry.domaingistry import Domain
>>> d = Domain('example','common')
>>> d.generate()
```

#### Alternatively
```python
>>> from domaingistry.domaingistry import Domain
>>> d = Domain()
>>> d.name ='yourdomain'
>>> d.category = 'extra'
>>> d.generate()
```

#### Get Common Domain Names
```python
>>> from domaingistry.domaingistry import Domain
>>> d = Domain('example')
>>> d.get_common()
```

#### Get New Domain Names
```python
>>> from domaingistry.domaingistry import Domain
>>> d = Domain('example')
>>> d.get_new()
```

#### Get Extra Domain Names
```python
>>> from domaingistry.domaingistry import Domain
>>> d = Domain('example')
>>> d.get_extra()
```

#### Get Prefixed Domain Names
```python
>>> from domaingistry.domaingistry import Domain
>>> d = Domain('example')
>>> d.get_prefix()
```

#### Get Suffixed Domain Names
```python
>>> from domaingistry.domaingistry import Domain
>>> d = Domain('example')
>>> d.get_suffix()
```

#### Get Shuffled Domain Names
```python
>>> from domaingistry.domaingistry import Domain
>>> d = Domain('example')
>>> d.get_shuffled()
```

### Saving Results To JSON

#### Get Common Domain Names
```python
>>> from domaingistry.domaingistry import Domain
>>> d = Domain('example','common')
>>> d.to_json()
```


#### DomainGistry Suite of Tools
+ DomainGistry Pkgs
+ Domain-Gistry CLI
+ DomainGistry.js


#### Author
+ Jesse E.Agbe(JCharis)
+ Jesus Saves @JCharisTech