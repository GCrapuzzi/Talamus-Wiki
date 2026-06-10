import unittest
from pathlib import Path

from talamus.redact import find_secrets, is_secret_file, redact


class SecretFileTests(unittest.TestCase):
    def test_secret_like_files_detected(self) -> None:
        for name in (".env", ".env.production", "id_rsa", "server.pem", "credentials.json"):
            self.assertTrue(is_secret_file(Path(name)), name)

    def test_normal_files_pass(self) -> None:
        for name in ("README.md", "main.py", "environment.md", "keynote.md"):
            self.assertFalse(is_secret_file(Path(name)), name)


class FindSecretsTests(unittest.TestCase):
    def test_detects_aws_key_with_line_number(self) -> None:
        text = "riga uno\nAWS_KEY = AKIAIOSFODNN7EXAMPLE\n"
        findings = find_secrets(text)
        self.assertTrue(any(f["kind"] == "aws-access-key" and f["line"] == 2 for f in findings))

    def test_detects_private_key_block_and_generic_assignment(self) -> None:
        text = '-----BEGIN RSA PRIVATE KEY-----\napi_key = "sk_live_abcdef1234567890"\n'
        kinds = {f["kind"] for f in find_secrets(text)}
        self.assertIn("private-key-block", kinds)
        self.assertIn("generic-assignment", kinds)

    def test_findings_never_include_the_value(self) -> None:
        text = "password = supersegreta12345678"
        for finding in find_secrets(text):
            self.assertNotIn("supersegreta", str(finding))

    def test_clean_text_has_no_findings(self) -> None:
        self.assertEqual(find_secrets("una nota normale sulla chiave di volta del ponte"), [])


class RedactTests(unittest.TestCase):
    def test_redacts_and_counts(self) -> None:
        text = "token: AKIAIOSFODNN7EXAMPLE e Bearer abcdefghijklmnopqrstuvwxyz123456"
        redacted, count = redact(text)
        self.assertGreaterEqual(count, 2)
        self.assertNotIn("AKIAIOSFODNN7EXAMPLE", redacted)
        self.assertIn("[REDACTED:", redacted)

    def test_clean_text_untouched(self) -> None:
        text = "il grafo è un indice, non la verità"
        redacted, count = redact(text)
        self.assertEqual(count, 0)
        self.assertEqual(redacted, text)


if __name__ == "__main__":
    unittest.main()
