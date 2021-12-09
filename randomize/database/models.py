from peewee import *
from decouple import config
from playhouse.db_url import connect



db = connect(config('DATABASE_URL'))

class MemberGuild(Model):
    user_id = BigIntegerField()
    guild_id = BigIntegerField()
    name = CharField()
    nick = CharField(null = True)
    guild_name = CharField()
    
    class Meta:
        database = db
        primary_key = CompositeKey('user_id', 'guild_id')

db.connect()
db.create_tables([MemberGuild])