from requests import get

def web_crawler():
        response = get("https://www.gintarine.lt/maistas-ir-papildai-sportininkams")
        html_content = response.text
        from lxml.html import fromstring
        tree = fromstring(html_content)

        # Fetch all product items
        products = tree.xpath("//div[contains(@class, 'product-item')]")

        for product in products:
            product_name = product.xpath(".//input[@name='productName']/@value")[0]
            product_price = product.xpath(".//input[@name='productPrice']/@value")[0]
            product_brand = product.xpath(".//input[@name='productBrand']/@value")[0]

            print(f"Product Name: {product_name}")
            print(f"Product Price: {product_price}")
            print(f"Product Brand: {product_brand}")