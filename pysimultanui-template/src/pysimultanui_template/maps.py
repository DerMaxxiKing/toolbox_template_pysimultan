from .mapper import mapper
from .contents import contents
from PySimultan2.taxonomy_maps import TaxonomyMap

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
