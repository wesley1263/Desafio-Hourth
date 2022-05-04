import math

from .base import base


class DataTable:

    def __init__(self):
        self.base = base()

    def _get_products_url(self):
        products = []
        for item in base():
            products.append(item["product_url"])
        return list(set(products))

    def _get_details_by_product(self, product_url: str):
        for item in base():
            if item["product_url"] == product_url:
                return {
                    "product_url__created_at": item["product_url__created_at"],
                    "product_url__image": item["product_url__image"],
                    "store_url": item["store_url"],
                }

    def _get_sales_date_by_product(self, product_url: str):
        sales_list = []
        for item in base():
            if item["product_url"] == product_url:
                sales_list.append({
                    "consult_date": item["consult_date"],
                    "total_sales": item["c"]
                })
        return sales_list

    def get_data_table(self, current_page=1):
        formatter_data_table = []

        for url in self._get_products_url():
            formatter_data_table.append({
                "url": url,
                "details": self._get_details_by_product(url),
                "sales": self._get_sales_date_by_product(url)
            })

        return self._paginate_data_table(formatter_data_table, current_page)

    def _paginate_data_table(self, data_table, current_page=1, per_page=25):
        total_products = len(self._get_products_url())
        total_pages = math.ceil(total_products / per_page)
        return {
            "current_page": current_page,
            "total_pages": total_pages,
            "per_page": per_page,
            "total_products": total_products,
            "data_table": data_table[(current_page - 1) * per_page: current_page * per_page]
        }
