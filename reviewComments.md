# Code Review for TAXAMADE Script

This document contains **detailed review comments, explanations, improvement guidelines, and concrete before/after code examples**.

## 1. Use a lint tool (e.g. Pylint VS Code plugin)

Current findings:

```python
[{
	"resource": "Taxamade/taxamade.py",
	"owner": "_generated_diagnostic_collection_name_#0",
	"code": {
		"value": "E0602:undefined-variable",
		"target": {
			"$mid": 1,
			"path": "/en/latest/user_guide/messages/error/undefined-variable.html",
			"scheme": "https",
			"authority": "pylint.readthedocs.io"
		}
	},
	"severity": 8,
	"message": "Undefined variable 'debug'",
	"source": "Pylint",
	"startLineNumber": 299,
	"startColumn": 12,
	"endLineNumber": 299,
	"endColumn": 17,
	"modelVersionId": 1,
	"origin": "extHost1"
},{
	"resource": "Taxamade/taxamade.py",
	"owner": "Pylance3",
	"code": {
		"value": "reportUndefinedVariable",
		"target": {
			"$mid": 1,
			"path": "/microsoft/pylance-release/blob/main/docs/diagnostics/reportUndefinedVariable.md",
			"scheme": "https",
			"authority": "github.com"
		}
	},
	"severity": 4,
	"message": "\"debug\" is not defined",
	"source": "Pylance",
	"startLineNumber": 299,
	"startColumn": 12,
	"endLineNumber": 299,
	"endColumn": 17,
	"modelVersionId": 1,
	"origin": "extHost1"
},{
	"resource": "Taxamade/taxamade.py",
	"owner": "_generated_diagnostic_collection_name_#0",
	"code": {
		"value": "C0301:line-too-long",
		"target": {
			"$mid": 1,
			"path": "/en/latest/user_guide/messages/convention/line-too-long.html",
			"scheme": "https",
			"authority": "pylint.readthedocs.io"
		}
	},
	"severity": 2,
	"message": "Line too long (104/100)",
	"source": "Pylint",
	"startLineNumber": 32,
	"startColumn": 1,
	"endLineNumber": 32,
	"endColumn": 1,
	"modelVersionId": 1,
	"origin": "extHost1"
},{
	"resource": "Taxamade/taxamade.py",
	"owner": "_generated_diagnostic_collection_name_#0",
	"code": {
		"value": "C0301:line-too-long",
		"target": {
			"$mid": 1,
			"path": "/en/latest/user_guide/messages/convention/line-too-long.html",
			"scheme": "https",
			"authority": "pylint.readthedocs.io"
		}
	},
	"severity": 2,
	"message": "Line too long (120/100)",
	"source": "Pylint",
	"startLineNumber": 43,
	"startColumn": 1,
	"endLineNumber": 43,
	"endColumn": 1,
	"modelVersionId": 1,
	"origin": "extHost1"
},{
	"resource": "Taxamade/taxamade.py",
	"owner": "_generated_diagnostic_collection_name_#0",
	"code": {
		"value": "C0303:trailing-whitespace",
		"target": {
			"$mid": 1,
			"path": "/en/latest/user_guide/messages/convention/trailing-whitespace.html",
			"scheme": "https",
			"authority": "pylint.readthedocs.io"
		}
	},
	"severity": 2,
	"message": "Trailing whitespace",
	"source": "Pylint",
	"startLineNumber": 110,
	"startColumn": 98,
	"endLineNumber": 110,
	"endColumn": 98,
	"modelVersionId": 1,
	"origin": "extHost1"
},{
	"resource": "Taxamade/taxamade.py",
	"owner": "_generated_diagnostic_collection_name_#0",
	"code": {
		"value": "C0116:missing-function-docstring",
		"target": {
			"$mid": 1,
			"path": "/en/latest/user_guide/messages/convention/missing-function-docstring.html",
			"scheme": "https",
			"authority": "pylint.readthedocs.io"
		}
	},
	"severity": 2,
	"message": "Missing function or method docstring",
	"source": "Pylint",
	"startLineNumber": 118,
	"startColumn": 1,
	"endLineNumber": 118,
	"endColumn": 25,
	"modelVersionId": 1,
	"origin": "extHost1"
},{
	"resource": "Taxamade/taxamade.py",
	"owner": "_generated_diagnostic_collection_name_#0",
	"code": {
		"value": "C0301:line-too-long",
		"target": {
			"$mid": 1,
			"path": "/en/latest/user_guide/messages/convention/line-too-long.html",
			"scheme": "https",
			"authority": "pylint.readthedocs.io"
		}
	},
	"severity": 2,
	"message": "Line too long (105/100)",
	"source": "Pylint",
	"startLineNumber": 130,
	"startColumn": 1,
	"endLineNumber": 130,
	"endColumn": 1,
	"modelVersionId": 1,
	"origin": "extHost1"
},{
	"resource": "Taxamade/taxamade.py",
	"owner": "_generated_diagnostic_collection_name_#0",
	"code": {
		"value": "C0103:invalid-name",
		"target": {
			"$mid": 1,
			"path": "/en/latest/user_guide/messages/convention/invalid-name.html",
			"scheme": "https",
			"authority": "pylint.readthedocs.io"
		}
	},
	"severity": 2,
	"message": "Constant name \"found\" doesn't conform to UPPER_CASE naming style",
	"source": "Pylint",
	"startLineNumber": 133,
	"startColumn": 17,
	"endLineNumber": 133,
	"endColumn": 22,
	"modelVersionId": 1,
	"origin": "extHost1"
},{
	"resource": "Taxamade/taxamade.py",
	"owner": "_generated_diagnostic_collection_name_#0",
	"code": {
		"value": "C0301:line-too-long",
		"target": {
			"$mid": 1,
			"path": "/en/latest/user_guide/messages/convention/line-too-long.html",
			"scheme": "https",
			"authority": "pylint.readthedocs.io"
		}
	},
	"severity": 2,
	"message": "Line too long (117/100)",
	"source": "Pylint",
	"startLineNumber": 149,
	"startColumn": 1,
	"endLineNumber": 149,
	"endColumn": 1,
	"modelVersionId": 1,
	"origin": "extHost1"
},{
	"resource": "Taxamade/taxamade.py",
	"owner": "_generated_diagnostic_collection_name_#0",
	"code": {
		"value": "C0301:line-too-long",
		"target": {
			"$mid": 1,
			"path": "/en/latest/user_guide/messages/convention/line-too-long.html",
			"scheme": "https",
			"authority": "pylint.readthedocs.io"
		}
	},
	"severity": 2,
	"message": "Line too long (135/100)",
	"source": "Pylint",
	"startLineNumber": 202,
	"startColumn": 1,
	"endLineNumber": 202,
	"endColumn": 1,
	"modelVersionId": 1,
	"origin": "extHost1"
},{
	"resource": "Taxamade/taxamade.py",
	"owner": "_generated_diagnostic_collection_name_#0",
	"code": {
		"value": "C0103:invalid-name",
		"target": {
			"$mid": 1,
			"path": "/en/latest/user_guide/messages/convention/invalid-name.html",
			"scheme": "https",
			"authority": "pylint.readthedocs.io"
		}
	},
	"severity": 2,
	"message": "Constant name \"found\" doesn't conform to UPPER_CASE naming style",
	"source": "Pylint",
	"startLineNumber": 205,
	"startColumn": 17,
	"endLineNumber": 205,
	"endColumn": 22,
	"modelVersionId": 1,
	"origin": "extHost1"
},{
	"resource": "Taxamade/taxamade.py",
	"owner": "_generated_diagnostic_collection_name_#0",
	"code": {
		"value": "C0303:trailing-whitespace",
		"target": {
			"$mid": 1,
			"path": "/en/latest/user_guide/messages/convention/trailing-whitespace.html",
			"scheme": "https",
			"authority": "pylint.readthedocs.io"
		}
	},
	"severity": 2,
	"message": "Trailing whitespace",
	"source": "Pylint",
	"startLineNumber": 216,
	"startColumn": 65,
	"endLineNumber": 216,
	"endColumn": 65,
	"modelVersionId": 1,
	"origin": "extHost1"
},{
	"resource": "Taxamade/taxamade.py",
	"owner": "_generated_diagnostic_collection_name_#0",
	"code": {
		"value": "C0301:line-too-long",
		"target": {
			"$mid": 1,
			"path": "/en/latest/user_guide/messages/convention/line-too-long.html",
			"scheme": "https",
			"authority": "pylint.readthedocs.io"
		}
	},
	"severity": 2,
	"message": "Line too long (106/100)",
	"source": "Pylint",
	"startLineNumber": 235,
	"startColumn": 1,
	"endLineNumber": 235,
	"endColumn": 1,
	"modelVersionId": 1,
	"origin": "extHost1"
},{
	"resource": "Taxamade/taxamade.py",
	"owner": "_generated_diagnostic_collection_name_#0",
	"code": {
		"value": "C0301:line-too-long",
		"target": {
			"$mid": 1,
			"path": "/en/latest/user_guide/messages/convention/line-too-long.html",
			"scheme": "https",
			"authority": "pylint.readthedocs.io"
		}
	},
	"severity": 2,
	"message": "Line too long (103/100)",
	"source": "Pylint",
	"startLineNumber": 257,
	"startColumn": 1,
	"endLineNumber": 257,
	"endColumn": 1,
	"modelVersionId": 1,
	"origin": "extHost1"
},{
	"resource": "Taxamade/taxamade.py",
	"owner": "_generated_diagnostic_collection_name_#0",
	"code": {
		"value": "C0303:trailing-whitespace",
		"target": {
			"$mid": 1,
			"path": "/en/latest/user_guide/messages/convention/trailing-whitespace.html",
			"scheme": "https",
			"authority": "pylint.readthedocs.io"
		}
	},
	"severity": 2,
	"message": "Trailing whitespace",
	"source": "Pylint",
	"startLineNumber": 269,
	"startColumn": 1,
	"endLineNumber": 269,
	"endColumn": 1,
	"modelVersionId": 1,
	"origin": "extHost1"
},{
	"resource": "Taxamade/taxamade.py",
	"owner": "_generated_diagnostic_collection_name_#0",
	"code": {
		"value": "C0103:invalid-name",
		"target": {
			"$mid": 1,
			"path": "/en/latest/user_guide/messages/convention/invalid-name.html",
			"scheme": "https",
			"authority": "pylint.readthedocs.io"
		}
	},
	"severity": 2,
	"message": "Constant name \"start\" doesn't conform to UPPER_CASE naming style",
	"source": "Pylint",
	"startLineNumber": 270,
	"startColumn": 5,
	"endLineNumber": 270,
	"endColumn": 10,
	"modelVersionId": 1,
	"origin": "extHost1"
},{
	"resource": "Taxamade/taxamade.py",
	"owner": "_generated_diagnostic_collection_name_#0",
	"code": {
		"value": "C0301:line-too-long",
		"target": {
			"$mid": 1,
			"path": "/en/latest/user_guide/messages/convention/line-too-long.html",
			"scheme": "https",
			"authority": "pylint.readthedocs.io"
		}
	},
	"severity": 2,
	"message": "Line too long (104/100)",
	"source": "Pylint",
	"startLineNumber": 271,
	"startColumn": 1,
	"endLineNumber": 271,
	"endColumn": 1,
	"modelVersionId": 1,
	"origin": "extHost1"
},{
	"resource": "Taxamade/taxamade.py",
	"owner": "_generated_diagnostic_collection_name_#0",
	"code": {
		"value": "C0301:line-too-long",
		"target": {
			"$mid": 1,
			"path": "/en/latest/user_guide/messages/convention/line-too-long.html",
			"scheme": "https",
			"authority": "pylint.readthedocs.io"
		}
	},
	"severity": 2,
	"message": "Line too long (104/100)",
	"source": "Pylint",
	"startLineNumber": 277,
	"startColumn": 1,
	"endLineNumber": 277,
	"endColumn": 1,
	"modelVersionId": 1,
	"origin": "extHost1"
},{
	"resource": "Taxamade/taxamade.py",
	"owner": "_generated_diagnostic_collection_name_#0",
	"code": {
		"value": "C0303:trailing-whitespace",
		"target": {
			"$mid": 1,
			"path": "/en/latest/user_guide/messages/convention/trailing-whitespace.html",
			"scheme": "https",
			"authority": "pylint.readthedocs.io"
		}
	},
	"severity": 2,
	"message": "Trailing whitespace",
	"source": "Pylint",
	"startLineNumber": 282,
	"startColumn": 1,
	"endLineNumber": 282,
	"endColumn": 1,
	"modelVersionId": 1,
	"origin": "extHost1"
},{
	"resource": "Taxamade/taxamade.py",
	"owner": "_generated_diagnostic_collection_name_#0",
	"code": {
		"value": "C0103:invalid-name",
		"target": {
			"$mid": 1,
			"path": "/en/latest/user_guide/messages/convention/invalid-name.html",
			"scheme": "https",
			"authority": "pylint.readthedocs.io"
		}
	},
	"severity": 2,
	"message": "Constant name \"start\" doesn't conform to UPPER_CASE naming style",
	"source": "Pylint",
	"startLineNumber": 283,
	"startColumn": 5,
	"endLineNumber": 283,
	"endColumn": 10,
	"modelVersionId": 1,
	"origin": "extHost1"
},{
	"resource": "Taxamade/taxamade.py",
	"owner": "_generated_diagnostic_collection_name_#0",
	"code": {
		"value": "C0301:line-too-long",
		"target": {
			"$mid": 1,
			"path": "/en/latest/user_guide/messages/convention/line-too-long.html",
			"scheme": "https",
			"authority": "pylint.readthedocs.io"
		}
	},
	"severity": 2,
	"message": "Line too long (101/100)",
	"source": "Pylint",
	"startLineNumber": 290,
	"startColumn": 1,
	"endLineNumber": 290,
	"endColumn": 1,
	"modelVersionId": 1,
	"origin": "extHost1"
}]
```

---

## 2. Expect Missing Input Files IB.csv, Obchody.csv

All input files might be missing. Consider to jump over or end up gracefully.

## 3. Avoid Global Variables
Functions rely on global variables like `oo`, `kurz_USD`, `kurz_EUR`. Pass these as parameters.

### Before
```python
def parse_column(col):
    data = oo.dropna(...)
```

### After
```python
def parse_column(df, col):
    data = df.dropna(subset=["Symbol"])
```

---

## 4. Create a Helper Function for Numeric Cleaning
Repeated `.str.replace()` patterns should be consolidated.

### After
```python
def clean_numeric(series):
    return (series.astype(str)
                 .str.replace(',', '.', regex=False)
                 .str.replace(r"[   ]", '', regex=True)
                 .astype(float)
                 .fillna(0))
```

---

## 5. Improve Date Parsing
Use more resilient date parsing.

```python
data["Datum obchodu"] = pd.to_datetime(data["Datum obchodu"], dayfirst=True, errors="coerce")
```

---

## 6. Reduce Repetition (Sell/Buy/Dividend)
Create reusable pipelines.

```python
def process_fio(df):
    sell = parse_column(df, "Prodej")
    buy  = parse_column(df, "Nákup")
    div  = parse_column(df, "")
    return sell, buy, div
```

---

## 7. Excel Export Refactoring
Create abstraction.

```python
def write_table(writer, sheet, df, row, title=None, fmt=None):
    ws = writer.sheets[sheet]
    if title:
        ws.write(row, 0, title)
        row += 1
    df.to_excel(writer, sheet_name=sheet, index=False, startrow=row)
    if fmt:
        format_sheet_columns(ws, df, df.columns, fmt)
    return row + len(df) + 2
```

---

## 8. Simplify Currency Conversion
Use mapping:

```python
RATES = {"USD": kurz_USD, "EUR": kurz_EUR}
```

---

## 9. Add Type Hints & Docstrings
Improves readability.

---

## 10. Replace print() with logging
Use:
```python
logger.info("Parse errors: %s", error)
```

---

## 11. Improve CSV Preprocessing
Use `dropwhile` for header skipping.

---

## 12. Split Script Into Modules
Suggested structure:
```
parser_fio.py
parser_ibkr.py
excel_writer.py
utils.py
main.py
```

---

## 13. Improve Naming
Use descriptive names:
- `raw_data`
- `row_offset`

---

## 14. Defensive Programming
Add column validation.

```python
required = {"Symbol", "Měna"}
missing = required - set(df.columns)
```

---
