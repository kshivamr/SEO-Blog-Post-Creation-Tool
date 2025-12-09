import os
from dotenv import load_dotenv
from scraper import scrape_amazon
from keywords import generate_keywords
from blog_generator import generate_blog
from publisher_blogger import publish_post

load_dotenv()

BLOG_ID = os.getenv("BLOG_ID")


def run():
    products = scrape_amazon()
    product = products[0]

    print(f"\nProcessing: {product['title']}\n")

    keywords = generate_keywords(product["title"])
    blog = generate_blog(product, keywords)

    print("Generated Blog:\n", blog)

    print("\nPosting to Blogger...")
    link = publish_post(BLOG_ID, product["title"], blog)

    print("\n✅ Blog Posted Successfully!")
    print("URL:", link)


if __name__ == "__main__":
    run()
import os
from dotenv import load_dotenv
from scraper import scrape_amazon
from keywords import generate_keywords
from blog_generator import generate_blog
from publisher_blogger import publish_post

load_dotenv()

BLOG_ID = os.getenv("BLOG_ID")


def run():
    products = scrape_amazon()
    product = products[0]

    print(f"\nProcessing: {product['title']}\n")

    keywords = generate_keywords(product["title"])
    blog = generate_blog(product, keywords)

    print("Generated Blog:\n", blog)

    print("\nPosting to Blogger...")
    link = publish_post(BLOG_ID, product["title"], blog)

    print("\n✅ Blog Posted Successfully!")
    print("URL:", link)


if __name__ == "__main__":
    run()
