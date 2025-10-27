Answers to reflection questions provided in the lab

1.Which issues were the easiest to fix, and which were the hardest? Why?
-Easiest: Style-related issues such as missing blank lines, unused imports, and converting strings to f-strings were quick to fix since they only required minor formatting or syntax changes.
-Hardest: The harder ones were logic and structure-related issues, such as replacing the bare except block with specific exception types and removing the global statement. These required understanding the program’s logic and adjusting the code without breaking functionality.

2.Did the static analysis tools report any false positives? If so, describe one example.
No major false positives were found. However, Pylint’s warning about catching a general exception (W0718) was not entirely incorrect but was overly strict — in some cases, a general Exception is acceptable for controlled error logging. Still, narrowing it down improved code clarity.

3.How would you integrate static analysis tools into your actual software development workflow? Consider continuous integration (CI) or local development practices.
-Integrate Pylint, Flake8, and Bandit into a Continuous Integration (CI) pipeline (e.g., GitHub Actions) so every commit or pull request automatically runs code checks.
-Configure pre-commit hooks locally so developers catch issues before pushing code.
-Use these tools during development to maintain consistent style, detect security risks early, and enforce team-wide coding standards.


4.What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
-The code is now more secure (no eval() or bare except blocks).
-It’s cleaner and more readable — functions follow PEP 8, use proper naming, and include docstrings.
-Maintainability improved with safe file handling (with open) and structured logging.
-Overall, the codebase is more robust, easier to understand, and less prone to silent errors or security risks.


