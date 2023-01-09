# means of bundling data and functionality together in new namespace
# new class becomes a new type in Python
# blueprint for creating objects of that type


# basic syntax
class ClassName:  # CamelCase by convention
    class_data_member = ...
    class_state = ...
    class_variable = ...
    class_property = ...
    class_attribute = ...  # use word "attribute" as convention

    def behavior():
        ...

    def function():
        ...

    def method():  # use word "method" as convention
        ...


print(type(123))
print(type(int))
print(type(ClassName))
