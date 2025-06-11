# Python 2.7 Test Coverage with `coverage.py`

This guide provides an introduction to test coverage in Python 2.7 using the `coverage.py` library. It explains what test coverage is, why it's important, and how to generate and interpret coverage reports.

## What is Test Coverage?

Test coverage is a metric that reveals which lines of your code are executed by your tests. In Python 2.7, the `coverage.py` library is the standard tool for this purpose. It helps you identify parts of your application that are not being tested, which is crucial for improving software quality and reducing the likelihood of bugs.

## Why You Need Test Coverage

Think of it as a map of your code that's colored in every time a test runs through a specific path. Untested areas remain blank. This is important for several reasons:

* **Reveals Untested Code**: It pinpoints functions, branches, and statements that your tests don't exercise.
* **Improves Test Quality**: It encourages the creation of more thorough tests that cover edge cases and different execution paths.
* **Aids Refactoring**: When you refactor or change code, you can be more confident if you know the surrounding logic is well-tested.
* **Maintains Code Health**: Over time, it helps prevent "code rot" where parts of the codebase become untested and therefore untrustworthy.

## Key Components of Coverage

When you run `coverage.py`, it works in two main phases:

1.  **Execution**: You run your test suite using `coverage run`. As your tests execute, `coverage.py` monitors which lines of your application code are run. This information is stored in a data file, typically named `.coverage`.
2.  **Reporting**: After the tests complete, you use commands like `coverage report` or `coverage html` to analyze the collected data and generate a report.

## Reading the Coverage Report

The coverage report is your main tool for understanding how well your tests cover your code. You can generate a simple text-based report directly in your terminal or a more detailed HTML report.

To see the report in your terminal, run:

```bash
coverage report -m
```

The `-m` flag is important as it will show you the "missing" line numbers for each file. Here's how to interpret the output:

| Column  | Description                                                                    |
| :------ | :----------------------------------------------------------------------------- |
| **Name** | The name of the Python module.                                                 |
| **Stmts** | The total number of executable statements in the module.                       |
| **Miss** | The number of statements that were not executed by your tests.                 |
| **Cover** | The percentage of statements that were covered (`(Stmts - Miss) / Stmts`). |
| **Missing** | The line numbers that were not executed. This is your guide for new tests.     |

### Finding Files Not in Coverage

Sometimes, a file might not appear in the report at all. This usually means your test suite never imported or touched that file. To find these completely untested files, use the `--source` option when running coverage. This tells `coverage.py` which directory of code you intend to measure.

For example, if your code is in a directory named `my_app`, you would run your tests like this:

```bash
coverage run --source=my_app my_tests.py
```

Then, when you generate the report, it will include all the files in `my_app`, even those with 0% coverage, making it clear which modules have been completely missed.

### HTML Report

For a more interactive and detailed view, generate an HTML report:

```bash
coverage html
```

This will create a directory named `htmlcov`. Open the `index.html` file inside it in your web browser. You'll see a summary, and you can click on individual file names to see a line-by-line breakdown of what was and wasn't executed.

---

## Simple Example in Python 2.7

Here’s a straightforward example of how to use `coverage.py`.

### 1. Set up your project structure:

Create a directory for your project and add the following files:

```
my_project/
├── my_app.py
└── test_my_app.py
```

### 2. Write your application code:

Place the following code inside `my_app.py`:

```python
# my_app.py

def calculate_price(base_price, tax_rate, discount=0):
    """
    Calculates the final price of an item.
    """
    if base_price < 0:
        raise ValueError("Price cannot be negative")

    tax = base_price * tax_rate
    final_price = base_price + tax

    if discount > 0:
        final_price = final_price * (1 - discount)

    return final_price
```

### 3. Write your test code:

Place the following test code inside `test_my_app.py`. Notice that we are **not** testing the discount logic.

```python
# test_my_app.py

import unittest
from my_app import calculate_price

class TestPriceCalculator(unittest.TestCase):

    def test_basic_price(self):
        self.assertEqual(calculate_price(100, 0.1), 110)

    def test_with_zero_tax(self):
        self.assertEqual(calculate_price(50, 0), 50)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_price(-10, 0.1)

if __name__ == '__main__':
    unittest.main()
```

### 4. Install `coverage.py`:

Since you're using Python 2.7, you'll need a version of `coverage.py` that is compatible. You can install it using `pip`:

```bash
pip install "coverage<5.0"
```
> **Note**: Versions of `coverage.py` 5.0 and later do not support Python 2.7.

### 5. Run your tests with coverage:

Now, from your `my_project` directory, run your tests using the `coverage run` command:

```bash
coverage run test_my_app.py
```

This will run your tests and create a `.coverage` data file.

### 6. Generate the report:

Finally, generate the report to see the results:

```bash
coverage report -m
```

You will see an output similar to this:

```
Name          Stmts   Miss  Cover   Missing
-------------------------------------------
my_app.py         7      2    71%   11-12
test_my_app.py   10      0   100%
-------------------------------------------
TOTAL            17      2    88%
```

This report clearly shows that `my_app.py` has **71% coverage** and that **lines 11-12** (the discount logic) were not executed by your tests. This gives you a clear action item: write a test that includes a discount to achieve 100% coverage.
```
