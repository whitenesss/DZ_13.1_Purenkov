class ObjectCreationMixin:
    def __init__(self, *args):
        print(repr(self))

    def __repr__(self):
        object_attributes = ''
        for key, value in self.__dict__.items():
            object_attributes += f'{key}: {value}, '
        return f"создан объект со свойствами {object_attributes})"

# class ObjectCreationMixin:
#     def __repr__(self):
#         class_name = self.__class__.__name__
#         attributes_list = []
#         for key in self.__dict__:
#             attribute_string = f'{key}={getattr(self, key)}'
#             attributes_list.append(attribute_string)
#         attributes_string = ', '.join(attributes_list)
#         return f"{class_name}({attributes_string})"