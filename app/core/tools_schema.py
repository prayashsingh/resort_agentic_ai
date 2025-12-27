TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "create_food_order",
            "description": "Create restaurant food order",
            "parameters": {
                "type": "object",
                "properties": {
                    "room_number": {"type": "string"},
                    "items": {"type": "array", "items": {"type": "string"}}
                },
                "required": ["room_number", "items"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "create_room_service_request",
            "description": "Create room service request",
            "parameters": {
                "type": "object",
                "properties": {
                    "room_number": {"type": "string"},
                    "request_type": {"type": "string"}
                },
                "required": ["room_number", "request_type"]
            }
        }
    }
]
