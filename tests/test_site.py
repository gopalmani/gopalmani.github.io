import re
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.meta = []
        self.title = ""
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if "id" in attributes:
            self.ids.append(attributes["id"])
        if tag in {"a", "link"} and "href" in attributes:
            self.links.append((tag, attributes["href"], attributes))
        if tag == "meta":
            self.meta.append(attributes)
        if tag == "title":
            self._in_title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data


class WebsiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = (ROOT / "index.html").read_text(encoding="utf-8")
        cls.css = (ROOT / "style.css").read_text(encoding="utf-8")
        cls.parser = SiteParser()
        cls.parser.feed(cls.html)

    def test_required_files_exist_and_are_not_empty(self):
        required = [
            "index.html",
            "style.css",
            "favicon.svg",
            "favicon.ico",
            "apple-touch-icon.png",
        ]
        for relative_path in required:
            path = ROOT / relative_path
            with self.subTest(path=relative_path):
                self.assertTrue(path.is_file())
                self.assertGreater(path.stat().st_size, 0)

    def test_page_has_title_and_description(self):
        self.assertTrue(self.parser.title.strip())
        descriptions = [
            meta.get("content", "").strip()
            for meta in self.parser.meta
            if meta.get("name") == "description"
        ]
        self.assertTrue(any(descriptions))

    def test_ids_are_unique(self):
        self.assertEqual(len(self.parser.ids), len(set(self.parser.ids)))

    def test_internal_anchors_have_targets(self):
        targets = set(self.parser.ids)
        for tag, href, _ in self.parser.links:
            if tag == "a" and href.startswith("#") and len(href) > 1:
                with self.subTest(href=href):
                    self.assertIn(href[1:], targets)

    def test_local_linked_files_exist(self):
        for _, href, _ in self.parser.links:
            parsed = urlparse(href)
            if not parsed.scheme and not parsed.netloc and parsed.path:
                with self.subTest(href=href):
                    self.assertTrue((ROOT / parsed.path).is_file())

    def test_new_tab_links_are_safe(self):
        for tag, href, attrs in self.parser.links:
            if tag == "a" and attrs.get("target") == "_blank":
                rel = set(attrs.get("rel", "").split())
                with self.subTest(href=href):
                    self.assertIn("noopener", rel)
                    self.assertIn("noreferrer", rel)

    def test_css_braces_are_balanced(self):
        css_without_comments = re.sub(r"/\*.*?\*/", "", self.css, flags=re.S)
        self.assertEqual(css_without_comments.count("{"), css_without_comments.count("}"))


if __name__ == "__main__":
    unittest.main()
