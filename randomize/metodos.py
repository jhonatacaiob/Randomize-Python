from discord import team
from database import operations
from random import shuffle


def add_members(members):
    for member in members:
        operations.save(member)


def remove_members(members):
    for member in members:
        operations.delete(member.id, member.guild.id)

def remove_all(guild_id):
    operations.delete_all(guild_id)


def group(guild_id):
    nomes  = []
    for member in operations.read(guild_id):
        if member.nick == None:
            nomes.append(member.name)
        else:
            nomes.append(member.nick)

    return list(map(lambda nome: '\t' + nome, nomes))

def show_list(title, list):
    msg = [f"{title}\n\n"] + list
    return "\n".join(msg)

def randomize(guild_id):
    group_shuffled = group(guild_id)
    shuffle(group_shuffled)

    middle = len(group_shuffled)//2

    teams = [group_shuffled[middle:], group_shuffled[:middle]]
    
    

    
    return "\n\n\n".join(list(map(lambda team:  show_list("-------------------\n Team", team), teams)))
