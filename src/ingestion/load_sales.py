from datetime import date

from pydantic import BaseModel, Field # BaseModel para definir modelos de datos y Field para agregar restricciones a los campos


class Sale(BaseModel):
    sale_id: int
    store_id: str
    product_id: str
    quantity: int = Field(gt=0) #mayor a 0
    unit_price: float = Field(gt=0) #mayor a 0
    sale_date: date #debe contener una fecha

if __name__ == "__main__":
    sale = Sale(
        sale_id=1,
        store_id="S001",
        product_id="P001",
        quantity=5,
        unit_price=4.50,
        sale_date="2026-01-01",
    )

    print(sale)