# -*- coding: utf-8 -*-
"""Tutorial on using the InfluxDB client."""

import argparse

from influxdb import InfluxDBClient


def main(host='localhost', port=8086):
    """Instantiate a connection to the InfluxDB."""
    user = 'admin'
    password = 'secretpassword'
    dbname = 'votes'
    dbuser = 'votes_user'
    dbuser_password = 'secretpassword'
    json_body = [
        {
            "measurement": "vote",
            "tags": {"note": True},
            "time": "2020-08-29T16:00:00Z",
            "fields": {
                "voter": 1,
                "city": "mi",
                "happiness": 3,
                "note": "a note"
            }
        },
        {
            "measurement": "vote",
            "tags": {"note": True},
            "time": "2020-08-29T13:00:00Z",
            "fields": {
                "voter": 2,
                "city": "mi",
                "happiness": 4,
                "note": "a fantastic day"
            }
        },
        {
            "measurement": "vote",
            "tags": {"note": True},
            "time": "2020-08-29T14:00:00Z",
            "fields": { "voter": 2,
                "city": "tn",
                "happiness": 1,
                "note": "worst day"
            }
        }
    ]

    client = InfluxDBClient(host, port, user, password, dbname)

    print("Create database: " + dbname)
    client.create_database(dbname)

    print("Create a retention policy")
    client.create_retention_policy('awesome_policy', '3d', 3, default=True)

    print("Switch user: " + dbuser)
    client.switch_user(dbuser, dbuser_password)

    print("Write points: {0}".format(json_body))
    client.write_points(json_body)

    print("-----\n")
    query = 'select happiness from vote;'
    print("Querying data: " + query)
    result = client.query(query)

    print("Result: {0}".format(result))

    print("-----\n")
    query_where = 'select note from vote;'
    print("Querying data: " + query_where)
    result = client.query(query_where, bind_params={'note': True })

    print("Result: {0}".format(result))

    query_range = "SELECT happiness,note,voter FROM vote WHERE time >= '2020-08-29T11:00:00Z' AND time <= '2020-08-29T17:00:00Z'"
    print("Querying data: " + query_range)
    result = client.query(query_range)

    print("Result: {0}".format(result))
    print("-----\n")

    print("Switch user: " + user)
    client.switch_user(user, password)

    print("Drop database: " + dbname)
    client.drop_database(dbname)


def parse_args():
    """Parse the args."""
    parser = argparse.ArgumentParser(
        description='example code to play with InfluxDB')
    parser.add_argument('--host', type=str, required=False,
                        default='localhost',
                        help='hostname of InfluxDB http API')
    parser.add_argument('--port', type=int, required=False, default=8086,
                        help='port of InfluxDB http API')
    return parser.parse_args()
if __name__ == '__main__':
    args = parse_args()
    main(host=args.host, port=args.port)
