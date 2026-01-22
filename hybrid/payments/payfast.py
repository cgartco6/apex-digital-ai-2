class PayFast:
    def initiate(self, amount):
        return {
            "gateway": "PayFast",
            "amount": amount,
            "status": "initiated"
        }
