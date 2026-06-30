import logging

import logtail

logger = logging.getLogger("fastship")
logger.setLevel(logging.INFO)

logtail_handler = logtail.LogtailHandler(
    source_token="QjG4DPM9gr4h2YoGoMz4p2F5",
    host="s2554177.eu-fsn-3.betterstackdata.com",
)

logtail_handler.setFormatter(
    logging.Formatter(
        "[%(levelname)s]: %(message)s",
    )
)

logger.addHandler(logtail_handler)
