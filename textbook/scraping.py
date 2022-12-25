import requests, bs4

def youtube_thumbnail(copied):

    TARGET  = copied["youtube_url"]
    # TARGET  = "https://www.youtube.com/watch?v=jNQXAC9IVRw"

    result  = requests.get(TARGET)
    soup    = bs4.BeautifulSoup(result.content,"html.parser")

    og_image_elems  = soup.select('[property="og:image"]')

    for og_image_elem in og_image_elems:
        return og_image_elem.get("content")

    return ""