import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("No vaccine found")
        if (
                datetime.date.today()
                > visitor.get("vaccine").get("expiration_date")
        ):
            raise OutdatedVaccineError("Vaccine is expired")
        missing_masks = 0
        if visitor.get("wearing_a_mask") is False:
            missing_masks += 1
            raise NotWearingMaskError("Masks are missing")
        return f"Welcome to {self.name}"
