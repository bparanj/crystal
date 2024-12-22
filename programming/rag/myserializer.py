import json

def serialize(obj):
    """Custom serializer for non-JSON-serializable objects."""
    if hasattr(obj, "__dict__"):  # For objects with attributes
        return obj.__dict__
    else:
        return str(obj)  # Fallback for objects without __dict__

def print_stream(graph, input):
    """Process and print stream data from a graph using the custom serializer."""
    for c in graph.stream(input):
        try:
            print(json.dumps(c, indent=4, default=serialize))
        except TypeError as e:
            print(f"Error serializing object: {e}")
            print(c)
