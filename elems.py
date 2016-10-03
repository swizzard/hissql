from copy import deepcopy

import psycopg2

class HisSQLError(Exception):
    pass


class ValidationError(HisSQLError):
    def __init__(self, messages):
        self.messages = messages

    def __repr__(self):
        return '\n'.join(self.messages)


class DB(object):
    def __init__(self, *conn_params):
        self.db = self.adapter.connect(*conn_params)
        self._cursor = None

    @property
    def cursor(self):
        if self._cursor is None:
            self._cursor = self.db.cursor()
        return self._cursor

    def prepare(self, func):
        def wrapped(*args, **kwargs):


    def __getattr__(self, name):
        attr = getattr(self.cursor, name)
        if hasattr(attr, '__call__'):
            return self.prepare(attr)
        else:
            return attr



class Table(object):
    def __init__(self, db, name, alias=None, validate=None):
        self.db = db
        self.name = name
        self._alias = alias
        if validate is None:
            self.validate = lambda anything: None
        else:
            self.validate = validate

    @property
    def alias(self):
        if self._alias is None:
            self._alias = ''.join(w[0] for w in self.name.split('_'))
        return self._alias


class Clause(object):
    def __init__(self, table):
        self.table = table
        self.content = []

    def __add__(self, other):
        if isinstance(other, Clause):
            if other.table != this.table:
                if other.table is not None:
                    raise HisSQLError("Clauses are bound to different tables")
                else:
                    other.table = this.table
            self.content.append(other)
            return self
        else:
            raise NotImplementedError

    def __and__(self, other):
        return self.__add__(other)

    def __str__(self):
        return '\n'.join(c.as_string() for c in self.content)

    def __call__(self, table):
        cpy = self._cpy()
        cpy.table = table
        return cpy

    def _cpy(self):
        return deepcopy(self)


class Select(Clause):
    def __init__(self, table, 
