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
Class1 = mapper.get_mapped_class('class1')

method_mapper.register_method(
    cls=Class1,
    name='Class1 method',
    method=Class1.method,
    add_data_model_to_kwargs=True,
    add_user_to_kwargs=True,
    kwargs={'io_bound': False}
)
