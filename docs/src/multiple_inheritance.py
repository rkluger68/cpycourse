# multiple_inheritance.py

# A simple data processing pipeline.

# Base class of the user-defined class hierarchy.
class Node:
    """Base class.
    """
    def __init__(self, name):
        self.name = name


class ProducingNode(Node):
    """Node that produces data.
    """
    def __init__(self, name):
        super().__init__(name)
        self.out_nodes = []

    def add_out_nodes(self, nodes):
        self.out_nodes.extend(nodes)


class ConsumingNode(Node):
    """Node that consumes data.
    """

    def send(self, data, trail=None):
        ...


class Connector(ProducingNode, ConsumingNode):
    """Interconnector node, both consumes (receives) and produces (sends) data.
    """

    def send(self, msg, trail=None):
        """Send a data message to this object, which will get passed on to all
        connected consumer nodes.
        """
        trail = None if trail is None else trail + (self.name,)
        for node in self.out_nodes:
            node.send(msg, trail=trail)


class CounterSource(ProducingNode):
    """Produce counter data messages.
    """
    
    def __init__(self, name):
        super().__init__(name)
        self.count = 0

    def trigger(self, trail_msgs=False):
        """For every trigger invocation send a message with the current count
        to all connected consumers.
        """
        trail = (self.name,) if trail_msgs else None
        for node in self.out_nodes:
            msg = self.count
            node.send(msg, trail=trail)
        self.count += 1
        

class PrinterSink(ConsumingNode):
    """Consume and print incoming data messages.
    """

    def send(self, msg, trail=None):
        trail = None if trail is None else trail + (self.name,)
        print(f'{self.__class__.__name__} "{self.name}": msg={msg} '
              f'trail={trail or ()}')


if __name__ == '__main__':
    source = CounterSource('Source')
    node_a = Connector('A')
    node_b = Connector('B')
    node_c = Connector('C')
    sink = PrinterSink('Sink')
    source.add_out_nodes([node_a])
    node_a.add_out_nodes([node_b, node_c])
    node_b.add_out_nodes([sink])
    node_c.add_out_nodes([sink])
    # The set up graph is:
    #
    #               /--> B \
    # Source --> A <        >--> Sink 
    #               \--> C /
    #
    for i in range(3):
        source.trigger(trail_msgs=True)

    print(dir(node_a))
