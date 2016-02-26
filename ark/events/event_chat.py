from ark.chat_commands import ChatCommands
from ark.cli import *
from ark.database import Db
from ark.rcon import Rcon

class EventChat(object):

    @classmethod
    def output_chat_from_server(cls,text,line):
        out(line)

    @classmethod
    def parse_chat_command(cls,steam_name,player_name,text,line):
        ChatCommands.parse(steam_name,player_name,text)

    @classmethod
    def update_player_name(cls,steam_name,player_name,text,line):
        steam_id = Rcon.find_online_steam_id(steam_name)
        if steam_id:
            Db.update_player(steam_id, steam_name=steam_name, name=player_name)

    @classmethod
    def store_chat(cls,steam_name,player_name,text,line):
        player = Db.find_player(steam_name=player_name)
        player_id = player.id if player is not None else None
        Db.create_chat_entry(player_id,player_name,text)

    @classmethod
    def output_chat(cls,steam_name,player_name,text,line):
        out(line)
    
    @classmethod
    def filter_chat(cls,steam_name,player_name,text,line):
        mots=text.split()
        res=None
        for mot in mots:
            if res is None:
                res=Db.check_mot(mot)
        if res:
            player=Db.find_player(steam_name=steam_name)
            steamid=player.steam_id if player is not None else None
            if steamid is not None:
                """Rcon.kick_player(steamid)"""
                """msg="Le joueur {} a ete kick pour avoir utiliser le mot {} !".format(player_name,res)"""
                msg="Attention {}, le mot '{}' est interdit dans le chat !".format(player_name,res)
                Rcon.broadcast(msg, None)
