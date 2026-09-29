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
        self.assets = []
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
        if tag in {"img", "script"} and "src" in attributes:
            self.assets.append(attributes["src"])
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
            "site.js",
            "assets/studio.svg",
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

    def test_product_positioning_and_destinations(self):
        self.assertIn("Products Built", self.html)
        for old_copy in ("Selected Work", "View Projects", "Selected Projects"):
            self.assertNotIn(old_copy, self.html)
        destinations = {href for _, href, _ in self.parser.links}
        for url in ("https://dayframehq.github.io/", "https://brahminbooking.com/",
                    "https://www.psyplay.io/", "https://github.com/gopalmani/QueryMindAI"):
            self.assertIn(url, destinations)

    def test_featured_product_order(self):
        products = re.findall(r'<article class="product">.*?<h3>([^<]+)', self.html)
        self.assertEqual(products, ["Dayframe", "PsyPlay", "KRIPA", "BrahminBooking"])
        self.assertIn('<strong>QueryMindAI</strong>', self.html)

    def test_basement_precedes_credit_and_monogram_is_uppercase(self):
        footer = self.html.split('<footer class="footer container">', 1)[1]
        self.assertLess(footer.index('class="basement-line"'), footer.index('©'))
        self.assertIn('You’ve reached the basement. I’m still wiring this part of my brain — check back soon.', footer)
        self.assertIn('>D<span>/</span>', self.html)

    def test_local_script_and_image_sources_exist(self):
        for src in self.parser.assets:
            if not urlparse(src).scheme:
                self.assertTrue((ROOT / src).is_file(), src)

    def test_clock_fallback_is_not_a_fake_time(self):
        self.assertIn('<time id="india-clock">IST</time>', self.html)
        self.assertNotIn('aria-live="polite"', self.html)

    def test_metadata_and_accessibility(self):
        self.assertIn('rel="canonical"', self.html)
        self.assertIn('property="og:title"', self.html)
        self.assertIn('class="skip-link"', self.html)
        self.assertIn("prefers-reduced-motion", self.css)
        self.assertIn(":focus-visible", self.css)

    def test_workshop_is_self_contained_valid_svg(self):
        import xml.etree.ElementTree as ET
        scene = ROOT / "assets/studio.svg"
        root = ET.parse(scene).getroot()
        self.assertTrue(root.tag.endswith("svg"))
        source = scene.read_text()
        self.assertNotIn("<script", source)
        self.assertNotIn("<image", source)
        self.assertIn("prefers-reduced-motion", source)


if __name__ == "__main__":
    unittest.main()
