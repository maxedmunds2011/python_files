# data.py

rooms = {
    "cell": {
        "description": "A cold detention cell with dim lights and a locked door to the north.",
        "exits": {"north": "hallway"},
        "items": []
    },
    "hallway": {
        "description": "A narrow hallway patrolled by droids. East leads to a control room. West leads to an armoury.",
        "exits": {"south": "cell", "east": "control_room", "west": "armoury"},
        "items": []
    },
    "armoury": {
        "description": "Stacks of weapons and equipment. There’s a blaster on the shelf.",
        "exits": {"east": "hallway", "north": "barracks"},
        "items": ["blaster"]
    },
    "control_room": {
        "description": "Screens flash with security alerts. A terminal glows. North leads to the escape pod.",
        "exits": {"west": "hallway", "north": "escape_pod", "east": "ventilation"},
        "items": ["keycard"]
    },
    "escape_pod": {
        "description": "A single escape pod sits waiting. The panel blinks: Insert Keycard.",
        "exits": {"south": "control_room", "north": "hangar"},
        "items": []
    },

    # New rooms start here
    "barracks": {
        "description": "Bunks, lockers, and signs of a recent fight. Blood on the wall.",
        "exits": {"south": "armoury"},
        "items": ["medkit"]
    },
    "ventilation": {
        "description": "A narrow, dark vent. You can hear voices above. There's a grate leading east.",
        "exits": {"east": "server_room", "west": "control_room"},
        "items": []
    },
    "server_room": {
        "description": "Banks of computers and humming lights. An access chip lies on the floor.",
        "exits": {"west": "ventilation"},
        "items": ["access_chip"]
    },
    "hangar": {
        "description": "A giant hangar bay with TIE fighters. A door to the north reads 'EXIT'.",
        "exits": {"north": "freedom_gate", "south": "escape_pod"},
        "items": []
    },
    "freedom_gate": {
        "description": "Security gate with retina scanner. Requires access chip to pass.",
        "exits": {},
        "items": []
    }
}

starting_room = "cell"
