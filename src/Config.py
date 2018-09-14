Config = {
    'vehicle': {
        'speed': 5,
        'safe_distance': 10,
        'body_length': 50,
        'body_width': 30,
        'safe_spawn_factor': 1.2
    },
    'simulator': {
        'screen_width': 800,
        'screen_height': 800,
        'bumper_distance': 10,
        'spawn_gap': 600,  # millisecond
        'frame_rate': 30,
        'gap_between_traffic_switch': 1  # second
    },
    'colors': {
        'black': (0, 0, 0),
        'white': (255, 255, 255),
        'dark_gray': (169, 169, 169),
        'traffic_yellow': (250, 210, 1)
    },
    'traffic_light': {
        'red_light_duration': 3,  # second
        'yellow_light_duration': 1,  # second
        'green_light_duration': 5,  # second
        'distance_from_center': (60, 60),
        'body_height': 60,
        'body_width': 25
    },
    'background': {
        'road_marking_width': 6,
        'road_marking_alternate_lengths': (30, 20),
        'junction_cover': (50, 50, 50, 50),  # top, right, bottom, left
        'total_vehicles_position': (5, 5),
        'total_vehicles_font_size': 20
    }
}
