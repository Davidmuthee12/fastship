import logging
from config import telemetry_settings
import logtail

logger = logging.getLogger("fastship")
logger.setLevel(logging.INFO)

logtail_handler = logtail.LogtailHandler(
    source_token=telemetry_settings.TELEMETRY_SOURCE_TOKEN,
    host=telemetry_settings.TELEMETRY_HOST,
)

logtail_handler.setFormatter(
    logging.Formatter(
        "[%(levelname)s]: %(message)s",
    )
)

logger.addHandler(logtail_handler)
