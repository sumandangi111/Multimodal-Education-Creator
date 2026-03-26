import requests

def generate_image(topic):

    try:

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        url = "https://en.wikipedia.org/w/api.php"

        params = {
            "action": "query",
            "titles": topic,
            "prop": "pageimages|images",
            "format": "json",
            "pithumbsize": 500
        }

        response = requests.get(url, params=params, headers=headers)
        data = response.json()

        pages = data["query"]["pages"]

        for page_id in pages:

            page = pages[page_id]

            # First try thumbnail
            if "thumbnail" in page:
                return page["thumbnail"]["source"]

            # If no thumbnail, try images list
            if "images" in page:
                for img in page["images"]:
                    name = img["title"]

                    if name.lower().endswith((".jpg", ".jpeg", ".png")):
                        return f"https://commons.wikimedia.org/wiki/Special:FilePath/{name.replace('File:', '')}"

    except Exception as e:
        print("Wikipedia image error:", e)

    return None