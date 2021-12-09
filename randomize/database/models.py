from peewee import *
from decouple import config
from playhouse.dataset import DataSet




db = PostgresqlDatabase('member_guild', user=config('USER'), password=config('PASS'),
                           host=config('HOST'), port=config('PORT'))

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