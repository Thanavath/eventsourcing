# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative.api import declarative_base
# from sqlalchemy.orm import scoped_session, sessionmaker


from eventsourcing.infrastructure.datastore import Datastore

# ActiveRecord = declarative_base()

DEFAULT_SQLALCHEMY_DB_URI = 'sqlite:///:memory:'


# DEFAULT_SQLALCHEMY_DB_URI = 'mysql://username:password@localhost/eventsourcing'
# DEFAULT_SQLALCHEMY_DB_URI = 'postgresql://username:password@localhost:5432/eventsourcing'


# class DjangoSettings(DatastoreSettings):
#     DB_URI = os.getenv('DB_URI', DEFAULT_SQLALCHEMY_DB_URI)
#
#     def __init__(self, uri=None):
#         self.uri = uri or self.DB_URI


class DjangoDatastore(Datastore):

    # def __init__(self, base=ActiveRecord, tables=None, connection_strategy='plain',
    #              session=None, **kwargs):
    #     super(DjangoDatastore, self).__init__(**kwargs)
    #     self._session = session
    #     self._engine = None
    #     self._base = base
    #     self._tables = tables
    #     self._connection_strategy = connection_strategy

    # @property
    # def session(self):
    #     if self._session is None:
    #         if self._engine is None:
    #             self.setup_connection()
    #         session_factory = sessionmaker(bind=self._engine)
    #         self._session = scoped_session(session_factory)
    #     return self._session

    def setup_connection(self):
        pass
        # assert isinstance(self.settings, DjangoSettings), self.settings
        # if self._engine is None:
        #     self._engine = create_engine(
        #         self.settings.uri,
        #         strategy=self._connection_strategy,
        #     )

    def setup_tables(self, tables=None):
        pass
        # if self._tables is not None:
        #     for table in self._tables:
        #         self.setup_table(table)

    def setup_table(self, table):
        pass
        # table.__table__.create(self._engine, checkfirst=True)

    def drop_tables(self):
        pass
        # if self._tables is not None:
        #     for table in self._tables:
        #         self.drop_table(table)

    def drop_table(self, table):
        pass
        # table.__table__.drop(self._engine, checkfirst=True)

    def truncate_tables(self):
        pass
        # self.drop_tables()

    def close_connection(self):
        pass
        # if self._session:
        #     self._session.close()
        #     self._session = None
        # if self._engine:
        #     self._engine = None
