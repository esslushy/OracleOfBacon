from DataProcessing import get_actor_info, get_actors_for_movie, get_title_id_to_title
from Node import ActorNode
import pickle

# Check if pickled node cluster exists and load it
try:
    nodes = pickle.load(open('nodes.pickle', errors='ignore'))
    nodes_exist = True
except FileNotFoundError:
    nodes_exist = False

# Actor info
actor_id_to_name, actor_id_to_movies = get_actor_info('dataset/name.basics.tsv')
# Title info
title_to_actor_ids = get_actors_for_movie('dataset/title.principals.tsv')
# Title id to actual titles
title_id_to_title = get_title_id_to_title('dataset/title.akas.tsv')

# Dictionary that stores the destinations we have found and the source from where they are found
dest_src = {}
# List holding the nodes to search. Will be a link of actor_id : ActorNode as it allows searching to be O(1) sometimes
nodes_to_search = {}
# Build all nodes if a batch doesn't already exist. Will be link of actor_id: ActorNode
if not nodes_exist:
    nodes = {}
    # Build nodes
    for actor_id in actor_id_to_name.keys():
        nodes[actor_id] = ActorNode(actor_id, actor_id_to_name[actor_id])
        nodes[actor_id].add_neighbors(actor_id_to_movies[actor_id], title_to_actor_ids)
    # Save nodes
    pickle.dump(nodes, open('nodes.pickle', 'w+', errors='ignore'))

print(nodes)

"""
Best way would be to have 2 data structures. One of actor to movies they were in and one of movies to the actors that participated in them.

"""
