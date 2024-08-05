class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, target):
        if (
            self.text == target.text
            and self.text_type == target.text_type
            and self.url == target.url
        ):
            return True

    def __repr__(self) -> str:
        TEXT = self.text
        TEXT_TYPE = self.text_type
        URL = self.url

        return f"TextNode({TEXT}, {TEXT_TYPE}, {URL})"


def main():
    test = TextNode("This is a text node", "bold", "https://www.boot.dev")
    test.__repr__()


main()
