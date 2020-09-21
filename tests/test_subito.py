from os import getenv

import pytest

from subito import __version__, Subito

app = Subito(getenv("GRAPHQL_SERVER"))


def test_version():
    assert __version__ == "0.1.0"


@pytest.mark.asyncio
@app.subscribe("subscription { stationFeedback }")
async def test_subscription():
    print("Subscribed as fuck!")
