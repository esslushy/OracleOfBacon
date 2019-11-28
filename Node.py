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

    def add_neighbor(self, title, neighbor_id):
        """
          Assembles the neighbors for this actor from the list of titles
          that they appear in and the main actors for those titles

          Args:
            title: The title the actor appears in
            neighbor_id: The actor the neighbor appears with
        """
        if not neighbor_id in self.neighbors and neighbor_id != self.actor_id:
            self.neighbors[neighbor_id] = title