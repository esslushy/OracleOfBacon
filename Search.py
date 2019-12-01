from DataProcessing import get_actor_info, get_actors_for_movie, get_title_id_to_title
from Node import ActorNode
import pickle
import os

# Load Data
# Actor info
actor_id_to_name, name_to_actor_id, actor_id_to_movies = get_actor_info('dataset/name.basics.tsv')
# Title info
title_to_actor_ids = get_actors_for_movie('dataset/title.principals.tsv')
# Title id to actual titles
title_id_to_title = get_title_id_to_title('dataset/title.akas.tsv')

# Check if pickled node cluster exists and load it
if os.path.exists('nodes.pickle'):
    nodes = pickle.load(open('nodes.pickle', 'rb'))
else: # If it doesn't exist, load the data and make the file
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

# Dictionary that stores the destinations we have found and the source from where they are found in actor_id
dest_src = {}
# List holding the nodes to search. Will be a list of actor_id
frontier = []

actor_to_find = input('What actor would you like to find the connection of Kevin Bacon to?\n').lower()
actor_id_to_find = name_to_actor_id[actor_to_find]

# Add Kevin Bacon to the top of the frontier and then continue from there until it is found
frontier.append(name_to_actor_id['kevin bacon'])

# Variable for tracking if the actor has been found
is_found = False

while(not is_found):
    # Pull out actor to search
    actor = nodes[frontier[0]]
    # Add its neighbors to the frontier and dest_src tree
    for neighbor in actor.neighbors:
        if neighbor not in frontier:
            frontier.append(neighbor)
        if neighbor not in dest_src:
            dest_src[neighbor] = actor.actor_id
    # Check if the searching for actor has been found
    is_found = actor_id_to_find in dest_src
    # Remove the processed actor from the list
    frontier.pop(0)

# After the actor is found print out the results
curr_actor_id = actor_id_to_find
# Go until you hit kevin bacon
while(curr_actor_id is not name_to_actor_id['kevin bacon']):
    # Find the shared movie
    shared_movie = title_id_to_title[nodes[dest_src[curr_actor_id]].neighbors[curr_actor_id]]
    # Print results
    print(f'{actor_id_to_name[curr_actor_id]} was in {shared_movie} with {actor_id_to_name[dest_src[curr_actor_id]]}')
    # Move onto next actor
    curr_actor_id = dest_src[curr_actor_id]