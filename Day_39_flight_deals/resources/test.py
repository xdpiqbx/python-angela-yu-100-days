test = {
    'id': '16ec0a7c4cbc0000f7ac1103_0|16ec0a7c4cbc0000f7ac1103_1',
    'flyFrom': 'RZE',
    'flyTo': 'ORY',
    'cityFrom': 'Rzeszów',
    'cityCodeFrom': 'RZE',
    'cityTo': 'Paris',
    'cityCodeTo': 'PAR',
    'countryFrom': {
        'code': 'PL',
        'name': 'Poland'
    },
    'countryTo': {
        'code': 'FR',
        'name': 'France'
    },
    'nightsInDest': None,
    'quality': 92.175536,
    'distance': 1426.41,
    'duration': {
        'departure': 19500,
        'return': 0,
        'total': 19500
    },
    'price': 41,
    'conversion': {
        'EUR': 36.842341,
        'USD': 41
    },
    'fare': {
        'adults': 41,
        'children': 41,
        'infants': 41
    },
    'bags_price': {
        '1': 80
    },
    'baglimit': {
        'hand_height': 38,
        'hand_length': 55,
        'hand_weight': 8,
        'hand_width': 22,
        'hold_dimensions_sum': 158,
        'hold_height': 52,
        'hold_length': 78,
        'hold_weight': 23,
        'hold_width': 28
    },
    'availability': {
        'seats': 7
    },
    'airlines': ['LH'],
    'route': [
        {
            'id': '16ec0a7c4cbc0000f7ac1103_0', 'combination_id': '16ec0a7c4cbc0000f7ac1103',
            'flyFrom': 'RZE',
            'flyTo': 'MUC',
            'cityFrom': 'Rzeszów',
            'cityCodeFrom': 'RZE',
            'cityTo': 'Munich',
            'cityCodeTo': 'MUC',
            'airline': 'LH',
            'flight_no': 1605,
            'operating_carrier': 'CL',
            'operating_flight_no': '',
            'fare_basis': 'K30LGTU9',
            'fare_category': 'M',
            'fare_classes': 'K',
            'fare_family': '',
            'return': 0,
            'bags_recheck_required': False, 'vi_connection': False, 'guarantee': False, 'equipment': None,
            'vehicle_type': 'aircraft',
            'local_arrival': '2023-10-14T14:35:00.000Z',
            'utc_arrival': '2023-10-14T12:35:00.000Z',
            'local_departure': '2023-10-14T13:10:00.000Z',
            'utc_departure': '2023-10-14T11:10:00.000Z'
        },
        {
            'id': '16ec0a7c4cbc0000f7ac1103_1', 'combination_id': '16ec0a7c4cbc0000f7ac1103',
            'flyFrom': 'MUC',
            'flyTo': 'ORY',
            'cityFrom': 'Munich',
            'cityCodeFrom': 'MUC',
            'cityTo': 'Paris',
            'cityCodeTo': 'PAR',
            'airline': 'LH',
            'flight_no': 9430,
            'operating_carrier': 'EN',
            'operating_flight_no': '8362',
            'fare_basis': 'K30LGTU9',
            'fare_category': 'M',
            'fare_classes': 'K',
            'fare_family': '',
            'return': 0,
            'bags_recheck_required': False, 'vi_connection': False, 'guarantee': False, 'equipment': None,
            'vehicle_type': 'aircraft',
            'local_arrival': '2023-10-14T18:35:00.000Z',
            'utc_arrival': '2023-10-14T16:35:00.000Z',
            'local_departure': '2023-10-14T17:00:00.000Z',
            'utc_departure': '2023-10-14T15:00:00.000Z'}
    ],
    'facilitated_booking_available': True, 'pnr_count': 1, 'has_airport_change': False, 'technical_stops': 0,
    'throw_away_ticketing': False, 'hidden_city_ticketing': False, 'virtual_interlining': False,
    'local_arrival': '2023-10-14T18:35:00.000Z',
    'utc_arrival': '2023-10-14T16:35:00.000Z',
    'local_departure': '2023-10-14T13:10:00.000Z',
    'utc_departure': '2023-10-14T11:10:00.000Z'}

prices_from_sheety = {'prices': [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2},
                                 {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 42, 'id': 3},
                                 {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4},
                                 {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551, 'id': 5},
                                 {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6},
                                 {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7},
                                 {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8},
                                 {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9},
                                 {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 378, 'id': 10}]}

sheet_ids_iata_codes = [{'id': 2, 'iataCode': 'PAR'}, {'id': 3, 'iataCode': 'BER'}, {'id': 4, 'iataCode': 'TYO'},
                        {'id': 5, 'iataCode': 'SYD'}, {'id': 6, 'iataCode': 'IST'}, {'id': 7, 'iataCode': 'KUL'},
                        {'id': 8, 'iataCode': 'NYC'}, {'id': 9, 'iataCode': 'SFO'}, {'id': 10, 'iataCode': 'CPT'}]
