import importlib.util
from pathlib import Path
import unittest


SCRIPT = Path(__file__).parents[1] / "scripts" / "search_databases.py"
SPEC = importlib.util.spec_from_file_location("search_databases", SCRIPT)
search_databases = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(search_databases)


class MetadataFingerprintTests(unittest.TestCase):
    def test_preserves_string_and_list_author_behavior(self):
        base = {"title": "A Study", "year": 2024}

        self.assertEqual(
            search_databases.metadata_fingerprint({**base, "authors": "Smith, Jones"}),
            "a study|2024|smith",
        )
        self.assertEqual(
            search_databases.metadata_fingerprint({**base, "authors": ["Smith", "Jones"]}),
            "a study|2024|smith",
        )

    def test_uses_stable_name_for_dictionary_author(self):
        result = {
            "title": "A Study",
            "year": 2024,
            "authors": [{"name": "Smith, Jane", "family": "Smith"}],
        }

        self.assertEqual(
            search_databases.metadata_fingerprint(result),
            "a study|2024|smith jane",
        )

    def test_uses_family_when_dictionary_has_no_name(self):
        result = {
            "title": "A Study",
            "year": 2024,
            "authors": [{"family": "Smith", "given": "Jane"}],
        }

        self.assertEqual(
            search_databases.metadata_fingerprint(result),
            "a study|2024|smith",
        )


class DeduplicateResultsTests(unittest.TestCase):
    def test_keeps_records_with_different_non_empty_dois(self):
        records = [
            {"title": "Same metadata", "year": 2024, "authors": ["Smith"], "doi": "10.1000/one"},
            {"title": "Same metadata", "year": 2024, "authors": ["Smith"], "doi": "10.1000/two"},
        ]

        self.assertEqual(len(search_databases.deduplicate_results(records)), 2)

    def test_prefers_doi_record_regardless_of_input_order(self):
        without_doi = {"title": "Same work", "year": 2024, "authors": ["Smith"], "source": "a"}
        with_doi = {**without_doi, "doi": "https://doi.org/10.1000/work", "source": "b"}

        for records in ([without_doi, with_doi], [with_doi, without_doi]):
            unique = search_databases.deduplicate_results(records)
            self.assertEqual(len(unique), 1)
            self.assertEqual(unique[0]["doi"], "https://doi.org/10.1000/work")

    def test_removes_duplicate_records_with_same_normalized_doi(self):
        records = [
            {"title": "First", "doi": "DOI: 10.1000/WORK."},
            {"title": "Second", "doi": "https://doi.org/10.1000/work"},
        ]

        self.assertEqual(search_databases.deduplicate_results(records), records[:1])


if __name__ == "__main__":
    unittest.main()
