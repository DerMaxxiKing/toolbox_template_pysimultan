# pysimultanui_template

-----

## Table of Contents

- [Overview](#overview)
- [How does it work?](#how-does-it-work)
- [Package Structure](#package-structure)
- [Template Package Structure](#template-package-structure)
- [Mapper](#mapper)
  * [Mapping a class](#mapping-a-class)
    + [Contents](#contents)
    + [Mapping](#mapping)
    + [TaxonomyMap](#taxonomymap)
- [Method Mapper](#method-mapper)
  - [Register_method](#register-method)
- [View Manager](#view-manager)
- [Building the package](#building-the-package)
  * [Distribution](#distribution)

- [Installation](#installation)
- [License](#license)


## Overview
This Package provides a template for creating a new toolbox for PySimultanUI and is intended to be used as a starting 
point for creating a new toolbox.
It is also a minimal example of how to create a toolbox for PySimultanUI.

## How does it work?
In PySimultanUI, a toolbox is a Python package that contains a mapper, a method_mapper and a view_manager. When the package
is imported, the mapper, method_mapper and view_manager are added to the mapping of the toolbox. The mapper is used to map
the class to the SIMULTAN meta data model, the method_mapper is used to map the methods of the class to be used in the UI and the
view_manager is used to create the view of the class in the UI.

Here is the code snippet that shows how a `package` is imported and added to the mapping of the toolbox when the package is imported in the UI:

```python
new_package = importlib.import_module(package)
mapper = getattr(new_package, 'mapper')
method_mapper = getattr(new_package, 'method_mapper', None)
view_manager = getattr(new_package, 'view_manager', None)
mapping = create_mapping(name=package,
                         mapper=getattr(new_package, 'mapper'),
                         method_mapper=getattr(new_package, 'method_mapper', None),
                         view_manager=getattr(new_package, 'view_manager', None)
                         )
```

## Package Structure
A package which can be used as a toolbox for PySimultanUI must provide at least a mapper, which can be imported using
`from <package> import mapper`. 

Additionally, a method_mapper and a view_manager can be provided, which must be importable using
`from <package> import method_mapper` and `from <package> import view_manager`, respectively.


## Template Package Structure
To simplify the creation of a new toolbox, this package provides a template package that can be used as a starting point.
The template-package contains the following files:

- `mapper.py`: This file contains the mapper class that maps the class to be used in the UI. This does not need 
to be modified.
- `method_mapper.py`: This file contains the method_mapper where the methods of the class are mapped.
- `view_manager.py`: This file contains the view_manager class where views for the mapped classes can be created.
- `contents.py`: This file is used to define the contents of the mapped classes
- `main.py`: This file is the entry point of the package and is used to run the UI with the toolbox.
- `core`: This directory contains the class definition of the mapped classes

## Mapper

The mapper is the basis to integrate SIMULTAN in python and is used to map the class to the SIMULTAN meta data model.
In the template package, a mapper is initialized in the `mapper.py` file:

```python
from PySimultan2.object_mapper import PythonMapper
mapper = PythonMapper()
```

### Mapping a class
To map a class, the class to be mapped should be defined int the core directory. In this template package, the class
`ExampleClass1` is defined in the `core.class1` directory. The class is then added to the mapper in the `maps.py` file.

#### Contents
First, the contents and the class must be defined, which are used to map the class to the SIMULTAN meta data model. 
The contents are defined in the `contents.py` file as a list of dictionaries, where each dictionary represents a 
attribute of the class. For the `ExampleClass1` class, the contents `attr1` and `attr2` and `attr3` are defined.

Below is an example of how the content for the attribute `attr1` is defined:

```python
from PySimultan2.taxonomy_maps import Content
contents = dict()
contents['attr1'] = Content(text_or_key='attr1',
                            property_name='attr1',
                            type=None,
                            unit='',
                            documentation='',
                            component_policy='subcomponent',
                            ValueMin=-9999,
                            ValueMax=9999)
```

##### Content properties:

- `text_or_key`: text_or_key: The text or key which the parameter, subcomponent or reference is assigned to in SIMULTAN
- `property_name`: the name of the attribute of the python class. This can be different from the text_or_key
- `type`: The type of the parameter, subcomponent or reference. This can be `bool` for boolean, `int` for integer, `float` for float, 
`str` for string, `list` for list, `dict` for dictionary, `tuple` for tuple, `set` for set, `numpy.ndarray` for numpy array,
`pandas.DataFrame` for pandas DataFrame or `numpy.array` for numpy array. PySimultan will try to interpret the value of
the attribute as the specified type. If the value cannot be interpreted as the specified type, the default type will be used.
- `unit`: The unit of the parameter, subcomponent or reference. This must be a string.
- `documentation`: The documentation of the parameter, subcomponent or reference. This must be a string.
- `component_policy`: The component policy of the attribute which defines if a component is added as subcomponent or a reference. 
The value can be `subcomponent` to add components as subcomponent (if the component is not already a subcomponent of another component) 
or`reference` to add a component as a reference.
- `ValueMin`: The minimum value of the parameter. This must be a `int` or `float`. This applies only to numerical types.
- `ValueMax`: The maximum value of the parameter. This must be a `int` or `float`. This applies only to numerical types.


#### Mapping
The class is then mapped to the SIMULTAN meta data model in the `maps.py` file. The class is added to the mapper 
using the `register` method of the mapper. The `register` method takes the class to be mapped, the taxonomy map and the
taxonomy entry key as arguments.

Below is an example of how the `ExampleClass1` class is mapped to the SIMULTAN meta data model:
First the mapper and the contents are imported. Then the taxonomy map is created and the class is registered with the mapper.


```python
from .mapper import mapper
from .contents import contents
from PySimultan2.taxonomy_maps import TaxonomyMap

# import the class to be mapped
from .core.class1 import ExampleClass1


class1_map = TaxonomyMap(taxonomy_name='MyModule',
                         taxonomy_key='my_module',
                         taxonomy_entry_name='class1',
                         taxonomy_entry_key='class1',
                         content=[contents['attr1'],
                                  contents['attr2'],
                                  contents['attr3'],
                                  ]
                         )

mapper.register(class1_map.taxonomy_entry_key, ExampleClass1, taxonomy_map=class1_map)
MappedFreeCADGeometry = mapper.get_mapped_class(class1_map.taxonomy_entry_key)
```

#### TaxonomyMap
The `TaxonomyMap` class is used to define the taxonomy map of the class. The `TaxonomyMap` class takes the following arguments:

- `taxonomy_name`: The name of the taxonomy. This must be a string (SIMULTAN Taxonomy Name).
- `taxonomy_key`: The key of the taxonomy. This must be a string (SIMULTAN Taxonomy key).
- `taxonomy_entry_name`: The name of the taxonomy entry. This must be a string (SIMULTAN TaxonomyEntry name).
- `taxonomy_entry_key`: The key of the taxonomy entry. This must be a string (SIMULTAN TaxonomyEntry key).
- `content`: A list of contents that define the attributes of the class. This must be a list of `Content` objects.


### Method Mapper
The method mapper is used to map the methods of the class or functions to be used in the UI. 
The implementation of the method mapper is optional. The mapped methods are defined in the `method_mapper.py` file.
The mapped methods are then available in the UI and can be called from the UI (global Methods or mapped Methods).

The template package provides an example of how to map the function `my_function` and a class method `add` using the 
method mapper:


```python
from pysimultanui import MethodMapper
from .mapper import mapper

method_mapper = MethodMapper()


# Define a function that will be called by the method mapper
def my_function(*args, **kwargs):

    user = kwargs.get('user')
    data_model = kwargs.get('data_model')

    print('Hello from my function!')
    print(user, data_model)


# Register the function with the method mapper
method_mapper.register_method(
    name='My function',
    method=my_function,
    add_data_model_to_kwargs=True,
    add_user_to_kwargs=True,
    kwargs={'io_bound': False}
)


# map a class method

# get the mapped class from the mapper:
Class1 = mapper.get_mapped_class('class1')

# Register a class method that will be called by the method mapper
method_mapper.register_method(
    cls=Class1,
    name='Class1 method',
    method=Class1.add,
    add_data_model_to_kwargs=False,
    add_user_to_kwargs=False,
    args=[],
    kwargs={'io_bound': False}
)
```

#### Register_method
The `register_method` method is used to register a method with the method mapper. The `register_method` method takes the following arguments:

- `name`: The name of the method, which is displayed in the dropdown. This must be a string.
- `method`: The method to be called. This can be a function or a class method. If it is a class method, the `cls` argument must be provided.
- `cls`: The class of the method, if the method is a class method. This must be a class.
- `add_data_model_to_kwargs`: A boolean that defines if the data model should be added to the kwargs of the method. 
This is used to pass the data model to the method. This must be a boolean.
- `add_user_to_kwargs`: A boolean that defines if the user should be added to the kwargs of the method.
- `kwargs`: Additional kwargs that are passed to the method. This must be a dictionary. The kwarg `io_bound` is used to define if 
the method is handled as a IO bound method, which is executed in a separate process. If the method is executed in a separate process,
it is not possible to do ui related operations in the method.
- `args`: A list of arguments that are passed to the method. This must be a list.


### View Manager

The view manager is used to create the view of the class in the UI. The view manager is optional and can be used to 
customize the view of the class in the UI.

When a instance of a mapped class is selected, PySimultanUI looks for a registered view in the view manager and creates
a instance of the view class with the instances as self.component. Then the `ui_content` method of the view class is called
to show the view in the UI.

Here is an example of how a view is defined for the class `class1` in the `view_manager.py` file.
In the view, the attributes `attr1`, `attr2` and `attr3` of the instance are displayed in the UI.

```python
from pysimultanui import ViewManager
from pysimultanui.views.component_detail_base_view import ComponentDetailBaseView
from nicegui import ui

view_manager = ViewManager()

class Class1DetailView(ComponentDetailBaseView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @ui.refreshable
    def ui_content(self, *args, **kwargs):
        super().ui_content(*args, **kwargs)

        ui.label('attr1:')
        ui.label(self.component.attr1)

        ui.label('attr2:')
        ui.label(self.component.attr2)

        ui.label('attr3:')
        ui.label(self.component.attr3)


view_manager.views['class1'] = Class1DetailView

```

The `ViewManager` handles the registered views which are shown when a instance of a mapped class is selected. 
The view can be defined as a class that inherits from `ComponentDetailBaseView` and implements the `ui_content` method.
The `ComponentDetailBaseView` implements the basic functionality of the view.

When a instance of a mapped class is selected, a new instance of the view is created and the `ui_content` 
method is called. 

Within the ComponentDetailBaseView class, the `component (self.component)` attribute is available, which is the instance of 
the mapped class. Additionally, the `user (self.user)` and `data_model (self.data_model)` attributes are available, which are the current user
and the data model of the current user, respectively.

The `ui_content` method must be decorated with `@ui.refreshable`, which is used to refresh the view when the data of the
instance changes.


### Building the package
To build the package, `pyproject.toml` file is used to define the package metadata and dependencies. 
At minimum the following fields must be adapted in the `pyproject.toml` file:

- `name`: The name of the package. This must be a string.
- `version`: The version of the package. The version is defined in the `__about__.py` file.
- `description`: The description of the package. This must be a string.
- `author`: The author of the package. This must be a string.
- `license`: The license of the package. This must be a string.
- `dependencies`: The dependencies of the package. This must be a list of strings.
- `package`: The package name. This must be a string.


To build the package hatch is used. If not already installed, hatch can be installed using pip:

```console
pip install hatch
```

To build the package, the following command can be used:

Windows:
```console
py -m build
```

Linux/MacOS:
```console
python -m build
```

##### Distribution
The package can be distributed using PyPi. To distribute the package, the following command can be used:

```console
twine upload dist/*
```



## Installation

```console
pip install pysimultanui_template
```

## License

`pysimultanui_template` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
