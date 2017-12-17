import json

config_json = json.load(open('./saves/config.json'))



username=config_json['username']
password=config_json['password']
client_id = config_json['client_id']
client_secret = config_json['client_secret']
user_agent = config_json['user_agent']


sub_json = json.load(open('./saves/sub_categories.json'))

sub_categories = {}

sub_categories['meme'] = set(sub_json['meme'])
sub_categories['default'] = set(sub_json['default'])
sub_categories['porn'] = set(sub_json['porn'])
sub_categories['political'] = set(sub_json['political'])
sub_categories['cool'] = set(sub_json['cool'])
sub_categories['educational'] = set(sub_json['educational'])
