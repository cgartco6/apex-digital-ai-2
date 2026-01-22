class Stripe:
    def initiate(self, amount):
        return {
            "gateway": "Stripe",
            "amount": amount,
            "status": "initiated"
        }
