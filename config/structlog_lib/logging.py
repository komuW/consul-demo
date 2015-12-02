import json


def _serializer(obj):
    """
    Render particular types in an appropriate way for logging. Allow
    the json module to handle the rest as usual.
    """
    # Datetime-like objects
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        return 'Object type {0} with value {1} is not JSON serializable'.format( type(obj), repr(obj) )


class KeyValueRenderer(object):
    """
    Render event_dict as a list of Key=json.dumps(str(Value)) pairs.

    This is a drop-in replacement for the structlog
    KeyValueRenderer. The primary motivation for using it is to avoid
    logging Python object representations for things like datetimes
    and unicode strings. json.dumps ensures that strings are
    double-quoted, with embedded quotes conveniently escaped.
    """

    def __call__(self, logger, name, event_dict):
        def serialize(v):
            """
            Try and serialize dict objects without appending extra escape charactes.
            """
            try:
                v = json.loads(v)
            except Exception as e:
                v = v
            return json.dumps(v, default=_serializer)

        return ', '.join('{0}={1}'.format(k, serialize(v))
                         for k, v in event_dict.items())