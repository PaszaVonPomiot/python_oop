class Exercise:
    static_var = 2

    def __init__(self):
        self.public = 20
        self._protected = 10
        self.__private = "private"  # no direct access from subclass
        self._decorated_property = 3

    def bound_method(self):
        return self.public

    @classmethod
    def class_method(cls):
        return cls.static_var

    @staticmethod
    def static_method():
        return 1

    @property
    def public_hidden(self):
        return self.public

    @property
    def protected_hidden(self):
        return self._protected

    @property
    def private_hidden(self):
        return self.__private

    def decorated_property_get(self):
        return self._decorated_property

    def decorated_property_set(self, new_value):
        self._decorated_property = new_value

    def decorated_property_del(self):
        print("no deleting please")

    decorated_property = property(
        fget=decorated_property_get,
        fset=decorated_property_set,
        fdel=decorated_property_del,
    )
