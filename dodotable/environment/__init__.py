""":mod:`dodotable.environment` --- Environment for dodotable.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
__all__ = 'Environment',


class Environment(object):
    """Top-level environment class, every environment class implemented by
    inherit this class.

    """

    #: (:class:`tuple`) methods that
    __env_methods__ = 'get_session',

    def build_url(self, *args, **kwargs):
        raise NotImplementedError()

    def get_session(self):
        raise NotImplementedError()

    def isinstance(self, instance, cls: (str, type)):
        if not isinstance(cls, type):
            try:
                name = cls.split(':')
                _mod = __import__(name[0], globals(), locals(), [name[1]], 0)
                mod = getattr(_mod, name[1])
            except (ImportError, IndexError):
                return False
        else:
            mod = cls
        return isinstance(instance, mod)


    def __dict__(self):
        env = {}
        for attribute in dir(self):
            if not (attribute.startswith('__') or
                    attribute in self.__env_methods__):
                env.update({attribute: getattr(self, attribute)})
        return env
