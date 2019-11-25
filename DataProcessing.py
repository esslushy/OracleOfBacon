def get_actor_info(file_location):
    """
      Gets the information tied to each acter id needed to build the tree.
      This includes the actors real name and movies they appeared in.

      Args:
        file_location: location of the data file that holds the actor information
    """
    actor_id_to_name = {}
    actor_id_to_titles = {}
    # Gather data
    for line in open(file_location, errors='ignore'):
        # Split lines into their major parts
        parts = line.replace('\n', '')
        parts = parts.split('\t')
        # parts[0] is id and parts[1] is the actor's name
        actor_id_to_name[parts[0]] = parts[1]
        # parts[0] is id and parts[5].split(',') gets a list of movies
        actor_id_to_titles[parts[0]] = parts[5].split(',')
    return actor_id_to_name, actor_id_to_titles

def get_actors_for_movie(file_location):
    """
      Gets the actors who acted in each title.

      Args:
        file_location: location of the data file that holds the actor to title information
    """
    title_to_actor_ids = {}
    # Gather and unite data
    for line in open(file_location, errors='ignore'):
        # Split lines into their major parts
        parts = line.replace('\n', '')
        parts = parts.split('\t')
        # Get movie title
        title = parts[0]
        # Check to see if movie title already exists in dataset
        if title in title_to_actor_ids:
            title_to_actor_ids[title].append(parts[2])
        else:
            title_to_actor_ids[title] = [parts[2]]
    return title_to_actor_ids

def get_title_id_to_title(file_location):
    """
      Gets the list of title ids to titles

      Args:
        file_location: Location of the data file that holds the title information
    """
    title_id_to_title  = {}
    # Gather and parse data
    for line in open(file_location, errors='ignore'):
        # Split lines into their major parts
        parts = line.replace('\n', '')
        parts = parts.split('\t')
        # Add to dictionary if its the first time it occurs (it can repeat multiple times in the file)
        if not parts[0] in title_id_to_title:
            title_id_to_title[parts[0]] = parts[2]
    return title_id_to_title