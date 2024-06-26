import networkx as nx
from .venue import venue
from matplotlib import pyplot as plt
import sys

class market:
    """
    A class to represent a market of trading venues as a non-directed multi-graph.
    The edges of this non-directed graph contain venues information, while the nodes
    are the coin pairs that can be swapped in such venues.
    
    Note:
        - This class is not developed to treat multi-assets liquidity pools!

    Attributes:
    -----------
    venues : list
        A list containing venue instances.
    graph : networkx.Graph
        A graph where each unique coin is a node and each reserve acts as an edge.
    
    Methods:
    --------
    generate_graph():
        Generates a graph from the venues.
    plot_graph(file, verbose):
        Prints the graph with matplotlib.
    price_function(sell_amount, liquidity_sell_token, liquidity_buy_token, market_type):
        Calculates the amount of tokens bought in a specific liquidity pool given sell amount.
    """

    def __init__(self, venues):
        """
        Constructs all the necessary attributes for the market object.
        
        Parameters:
        -----------
        venues : list
            A list containing venue instances.
        """
        self.venues = venues
        self.graph = nx.Graph()
        self.generate_graph()

    def generate_graph(self):
        """
        Generates the market graph from the market venues and token pairs

        This method performs the following steps:
        1. Iterates over the venues to add tokens as nodes in the graph.
        2. Creates edges between tokens based on the venues' reserves.
        3. If an edge between two tokens already exists, it updates the edge's attributes
           with additional venue information -- multigraph
        4. If an edge does not exist, it creates a new edge with the venue's name and
           reserve information as attributes.
        """
        # Create nodes with the tokens
        for venue in self.venues:
            for token, amount in venue.reserves.items():
                if token not in self.graph:
                    self.graph.add_node(token)

        # Create edges with the venues in the market
        for venue in self.venues:
            tokens = list(venue.reserves.keys())
            for i in range(len(tokens)):
                for j in range(i + 1, len(tokens)):
                    token1 = tokens[i]
                    token2 = tokens[j]
                    # Check if edge exists already
                    if self.graph.has_edge(token1, token2):
                        # If edge already exists, update the 'venues' attribute - multigraph
                        self.graph[token1][token2]['venues'].append(venue.name)
                        self.graph[token1][token2]['tokens'].append([token1,token2])
                        self.graph[token1][token2]['liquidity_token1'].append(venue.reserves[token1])
                        self.graph[token1][token2]['liquidity_token2'].append(venue.reserves[token2])
                    else:
                        # Otherwise, add a new edge with venue name as attribute
                        self.graph.add_edge(token1, token2,
                                            venues=[venue.name],
                                            tokens=[[token1, token2]],
                                            liquidity_token1=[venue.reserves[token1]],
                                            liquidity_token2=[venue.reserves[token2]])
        

    def plot_graph(self, file=None, verbose=False):
        """
        Plots the graph using matplotlib. If a file path is provided, the plot is saved to the file.
    
        Parameters:
        -----------
        file :str, optional
          The path to save the plot image. If None, the plot is displayed.
        verbose : bool, optional
          If True, prints details about the graph nodes and edges. Default is False.
        """
        pos = nx.spring_layout(self.graph)  # positions for all nodes
        plt.figure(figsize=(10, 8))
    
        # Draw nodes
        nx.draw_networkx_nodes(self.graph, pos, node_size=7000, node_color='lightblue')
    
        # Draw edges
        nx.draw_networkx_edges(self.graph, pos, width=2)
    
        # Draw node labels
        nx.draw_networkx_labels(self.graph, pos, font_size=12, font_family='sans-serif')
    
        # Draw edge labels
        edge_labels = {(u, v): ', '.join(data['venues']) for u, v, data in self.graph.edges(data=True)}
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels, font_size=10, font_family='sans-serif')
    
        plt.title("Market Graph")
        if file:
            plt.savefig(file)
        else:
            plt.show()
    
        if verbose:
            print("Graph Nodes:")
            print(self.graph.nodes())
            print("\nGraph Edges:")
            for edge in self.graph.edges(data=True):
                print(edge)

    @staticmethod
    def price_function(coin_amount, liquidity_sell_token, liquidity_buy_token, market_type='constant_product', what_='buy'):
        """
        Calculate the amount of tokens bought in a specific liquidity pool given the sell amount, the type of
        Automated Market Maker (AMM) of the pool, and the initial liquidities of the buy and sell tokens.

        Note:
            - The formula for bought b tokens of Bgiven the amount a of A tokens sold is
              b = [B]a/([A] + a), where [A], [B] are the liquidities of tokens A and B
              respectively.
            - We are not considering any fee for the liquidity providers

        Parameters
        ----------
        coin_amount : int
            The amount of the token either bought or sold by the AMM
        liquidity_sell_token : int
            The current liquidity of the sell token in the liquidity pool.
        liquidity_buy_token : int
            The current liquidity of the buy token in the liquidity pool.
        market_type : str, optional
            The type of AMM mechanism used by the liquidity pool. Default is 'constant_product'.
            Supported values:
            - 'constant_product': Uses the constant product formula (x * y = k) for price calculation.
        what_ : str, optional
            The type of operation performed by the AMM
            Supported values:
            - 'buy', 'sell' if AMM either is buying or selling

        Returns
        -------
        float
            The calculated amount of buy tokens received for the given sell amount.

        Raises
        ------
        ValueError
            If an unsupported market type is provided.
        """
        if market_type == 'constant_product':
            if what_ == 'buy': 
                buy_amount = liquidity_buy_token * (coin_amount/ (liquidity_sell_token + coin_amount))
                return buy_amount
            if what_ == 'sell':
                sell_amount = -liquidity_sell_token * (-coin_amount / (liquidity_buy_token - coin_amount))
                return sell_amount
        else:
            raise ValueError(f"Unsupported market type: {market_type}")

