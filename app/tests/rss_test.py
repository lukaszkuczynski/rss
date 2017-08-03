from unittest import main, TestCase
from app.rss import prepare_entry_before_writing_to_csv

class RssTest(TestCase):

    def test_csv_strips_newline(self):
        description = "blabla\nblabla"
        entry = {
            "description": description
        }
        prepare_entry_before_writing_to_csv(entry)
        description_after = entry['description']
        self.assertNotEqual(description, description_after)
        self.assertEqual(description_after, "blablablabla")

if __name__ == '__main__':
    main()