import networkx as nx

graph = nx.Graph()


def add_relationship(entity1, entity2, relation):

    graph.add_node(entity1)

    graph.add_node(entity2)

    graph.add_edge(
        entity1,
        entity2,
        relation=relation
    )


def get_related_entities(entity):

    if entity not in graph:
        return []

    return list(graph.neighbors(entity))


def build_graph_from_chunks(chunks):

    for chunk in chunks:

        words = chunk.split()

        entities = list(set(words[:10]))

        for i in range(len(entities) - 1):

            add_relationship(
                entities[i],
                entities[i + 1],
                "related"
            )


def graph_expand(query):

    related = get_related_entities(query)

    return related