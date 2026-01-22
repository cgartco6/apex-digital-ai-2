from fastapi import APIRouter
from hybrid.payments.payfast import PayFast
from hybrid.governance.audit import Audit

router = APIRouter()

@router.post("/pay")
def pay(amount: float):
    payment = PayFast().initiate(amount)
    Audit().log(f"Payment initiated: {amount}")
    return payment
