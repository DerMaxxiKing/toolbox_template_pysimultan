import logging
from pysimultanui import MethodMapper
from .mapper import mapper

method_mapper = MethodMapper()

logger = logging.getLogger('my_toolbox')


# Define a function that will be called by the method mapper
def my_function(*args, **kwargs):

    user = kwargs.get('user')
    data_model = kwargs.get('data_model')

    logger.info('Hello from my function!')


# Register the function with the method mapper
method_mapper.register_method(
    name='My function',
    method=my_function,
    add_data_model_to_kwargs=True,
    add_user_to_kwargs=True,
    io_bound=False
)


# map a class method
Class1 = mapper.get_mapped_class('class1')

method_mapper.register_method(
    cls=Class1,
    name='Class1 method',
    method=Class1.add,
    add_data_model_to_kwargs=False,
    add_user_to_kwargs=False,
    io_bound=False
)
