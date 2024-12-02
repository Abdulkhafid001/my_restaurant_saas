from datetime import datetime, date
import json
from decimal import Decimal

# Custom JSON encoder


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        return super().default(obj)  # Use default encoding for other types
