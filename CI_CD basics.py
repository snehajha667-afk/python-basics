"""
CI/CD Basics

CI = Continuous Integration
CD = Continuous Delivery / Continuous Deployment

This file demonstrates the idea behind CI/CD.

Workflow:

1. Write code
2. Write tests
3. Run tests locally
4. Commit changes
5. Push code to GitHub
6. GitHub Actions automatically:
   - Installs Python
   - Installs dependencies
   - Runs tests
7. If all tests pass:
   - Continuous Delivery: Application is ready for deployment.
   - Continuous Deployment: Application is deployed automatically.

Example Project:
"""

def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


def run_tests() -> None:
    """Simple test cases."""

    assert add(10, 5) == 15
    assert subtract(20, 5) == 15

    print("✅ All tests passed!")


if __name__ == "__main__":
    print("Running CI/CD example...\n")

    run_tests()

    print("\nCI Pipeline Successful!")
    print("Code is ready for deployment.")
