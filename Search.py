from DataProcessing import get_actor_info, get_actors_for_movie, get_title_id_to_title
from Node import ActorNode
import pickle

# Load Data
# Actor info
actor_id_to_name, name_to_actor_id, actor_id_to_movies = get_actor_info('dataset/name.basics.tsv')
print(name_to_actor_id)
# Title info
title_to_actor_ids = get_actors_for_movie('dataset/title.principals.tsv')
# Title id to actual titles
title_id_to_title = get_title_id_to_title('dataset/title.akas.tsv')

# Check if pickled node cluster exists and load it
try:
    nodes = pickle.load(open('nodes.pickle', 'rb'))
except FileNotFoundError: # If it doesn't exist, load the data and make the file
    # Build all nodes if a batch doesn't already exist. Will be link of actor_id: ActorNode
    nodes = {}
    # Build nodes
    for actor_id in actor_id_to_name.keys():
        nodes[actor_id] = ActorNode(actor_id, actor_id_to_name[actor_id])
        for title in actor_id_to_movies[actor_id]:
            try:
                for actor in title_to_actor_ids[title]:
                    nodes[actor_id].add_neighbor(title, actor)
            except KeyError: # Sometimes the movie doesn't exist for whatever reason so just continue on
                continue
    # Save nodes
    pickle.dump(nodes, open('nodes.pickle', 'wb'))

# Dictionary that stores the destinations we have found and the source from where they are found
dest_src = {}
# List holding the nodes to search. Will be a link of actor_id : ActorNode as it allows searching to be O(1) sometimes
nodes_to_search = {}

actor_to_find = input('What actor would you like to find the connection of Kevin Bacon to?\n').lower()

