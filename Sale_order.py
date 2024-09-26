discount = 0.1


def create_order(price):
    sale_price = price - (price * discount)

    def apply_additional_discount():
        nonlocal sale_price
        vip_sale = 0.15
        sale_price = sale_price - (vip_sale * sale_price)
        return sale_price
    return apply_additional_discount()


print(create_order(1000))
