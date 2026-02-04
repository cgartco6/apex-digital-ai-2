DEFAULT_MARKUP = 1.3  # 30% agency margin

def apply_agency_pricing(base_price, agency_markup=DEFAULT_MARKUP):
    return round(base_price * agency_markup, 2)
