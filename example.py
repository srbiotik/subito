from os import getenv
import asyncio
from asyncio import get_event_loop


from subito import Subito


service = Subito(url=getenv("GRAPHQL_SERVER"))


@service.subscribe("subscription { stationFeedback }")
async def check_station_status(message):
    station = message.stationFeedback.station
    value = message.stationFeedback.value
    print(
        f"Message from station {station} for parent {value.name} function check_station_status"
    )


@service.subscribe("subscription { stationFeedback }")
async def do_something_else(message):
    station = message.stationFeedback.station
    value = message.stationFeedback.value
    print(
        f"Message from station {station} for parent {value.name} function do_something_else"
    )


if __name__ == "__main__":
    loop = get_event_loop()
    loop.run_until_complete(service.run())