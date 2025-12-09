def generate_keywords(product_title):
    print("Generating keywords...")
    title = product_title.lower()

    return [
        f"{title} review",
        f"best {title}",
        f"{title} price in india",
        f"buy {title} online"
    ]
