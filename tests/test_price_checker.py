import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from check_price import extract_price_from_html, update_document


class PriceCheckerTests(unittest.TestCase):
    def html(self, condition='Excellent', sim='Physical SIM + eSIM', colour='Blue', price='338.00'):
        return f'''<html><head><script>Excellent £125.00</script></head><body>
          <h1>iPhone 15 Blue • 128 GB • Physical SIM + eSIM</h1>
          <section>Select condition: Fair £290.00 Good £330.00 Excellent £359.00</section>
          <aside>Other offers: iPhone 16 £299.00</aside>
          <section>iPhone 15 <ul><li>{condition}</li><li>128 GB</li>
          <li>{sim}</li><li>{colour}</li></ul><b>£{price}</b> before trade-in</section>
          <footer>£599 new</footer></body></html>'''

    def test_exact_variant(self):
        self.assertEqual(extract_price_from_html(self.html()), 338.00)

    def test_ignore_condition_picker_price(self):
        self.assertEqual(extract_price_from_html(self.html(price='339.50')), 339.50)

    def test_reject_esim_only(self):
        with self.assertRaises(ValueError):
            extract_price_from_html(self.html(sim='eSIM'))

    def test_reject_wrong_colour(self):
        with self.assertRaises(ValueError):
            extract_price_from_html(self.html(colour='Black'))

    def test_reject_wrong_condition(self):
        with self.assertRaises(ValueError):
            extract_price_from_html(self.html(condition='Good'))

    def test_reject_scripts_with_fake_price(self):
        with self.assertRaises(ValueError):
            extract_price_from_html('<html><script>iPhone 15 Excellent 128 GB Physical SIM + eSIM Blue £199.00</script><body>Other device £399</body></html>')

    def test_history_when_price_changes_and_no_repeats_for_hourly_check(self):
        existing={'history':[{'at':'2026-10-24T18:00:00Z','price':338.0,'source':'automatic'}]}
        changed=update_document(existing,339.0,'2026-10-24T19:00:00Z')
        self.assertEqual(len(changed['history']),2)
        unchanged=update_document(changed,339.0,'2026-10-24T20:00:00Z')
        self.assertEqual(len(unchanged['history']),2)


if __name__ == '__main__':unittest.main()
