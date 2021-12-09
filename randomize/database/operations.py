from peewee import *
from database.models import MemberGuild

def save(member):

    if len(read_one(member.id, member.guild.id)) == 0:

        m = MemberGuild()
        m.user_id = member.id
        m.guild_id = member.guild.id        
        m.name= member.name
        m.nick= member.nick
        m.guild_name = member.guild.name
        m.save(force_insert=True)


def delete(user_id, guild_id):
    MemberGuild.delete().where(MemberGuild.user_id == user_id).where(MemberGuild.guild_id == guild_id).execute()


def delete_all(guild_id):
    MemberGuild.delete().where(MemberGuild.guild_id == guild_id).execute()

def read(guild_id):
    return MemberGuild.select(MemberGuild.name, MemberGuild.nick).where(MemberGuild.guild_id == guild_id)

def read_one(user_id, guild_id):
    return MemberGuild.select().where(MemberGuild.user_id == user_id).where(MemberGuild.guild_id == guild_id)
    
