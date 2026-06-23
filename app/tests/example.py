from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import DeliveryPartner, Seller, Location
from app.services.user import password_context

SELLER = {
    "name": "RainForest",
    "email": "rainforest@xmailg.one",
    "password": "lovetrees",
    "zip_code": 11001,
}
DELIVERY_PARTNER = {
    "name": "PHL",
    "email": "phl@xmailg.one",
    "password": "tough",
    "zip_code": 11002,
    "max_handling_capacity": 2,
    "serviceable_zip_codes": [11001, 11002, 11003, 11004, 11005],
}
SHIPMENT = {
    "content": "Bananas",
    "weight": 1.25,
    "destination": 11004,
    "location": 11004,
    "client_contact_email": "py@xmailg.one",
}


async def create_test_data(session: AsyncSession):
    session.add(
        Seller(
            **SELLER,
            email_verified=True,
            password_hash=password_context.hash(SELLER["password"]),
        )
    )
    partner = DeliveryPartner(
        **{k: v for k, v in DELIVERY_PARTNER.items() if k != "serviceable_zip_codes"},
        email_verified=True,
        password_hash=password_context.hash(DELIVERY_PARTNER["password"]),
        servicable_locations=[Location(zip_code=z) for z in DELIVERY_PARTNER["serviceable_zip_codes"]],
    )
    session.add(partner)

    await session.commit()
