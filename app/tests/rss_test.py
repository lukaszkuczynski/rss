from unittest import main, TestCase
from app.rss import prepare_entry_before_writing_to_csv

class RssTest(TestCase):

    def test_csv_strips_newline(self):
        entry_before = {
            "description": "blabla\nblabla"
        }
        entry_after = prepare_entry_before_writing_to_csv(entry_before)
        self.assertNotEqual(entry_before['description'], entry_after['description'])

if __name__ == '__main__':
    main()