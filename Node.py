class ActorNode():
    """
      Builds an Actornode which contains the basic information of each
      actor along with the ids of its neighbors and what movies they connect too.

      Args:
        actor_id: The id of the actor in the data files
        actor_name: The name of the actor
    """
    def __init__(self, actor_id, actor_name):
        self.actor_id = actor_id
        self.actor_name = actor_name
        self.neighbors = {} # Where it is an actor_id : title_id combo

    def add_neighbors(self, titles, titles_to_actor_ids):
        """
          Assembles the neighbors for this actor from the list of titles
          that they appear in and the main actors for those titles

          Args:
            titles: The titles the actor appears in
            titles_to_actor_ids: The titles to the main actors they are in
        """
        for title in titles:
            for actor_id in titles_to_actor_ids:
                # Don't want to overwrite already existing actors in the neighbor list or add itself as a neighbor.
                if not actor_id in self.neighbors and actor_id != self.actor_id:
                    self.neighbors[actor_id] = title