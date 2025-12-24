# OOXML Validator

Command-line tool to validate Office Open XML documents (Word, Excel, PowerPoint) using the OpenXML SDK validator.

## Features

- Validates `.docx`, `.docm`, `.dotx`, `.dotm` (Word documents)
- Validates `.xlsx`, `.xlsm`, `.xltx`, `.xltm` (Excel documents)
- Validates `.pptx`, `.pptm`, `.potx`, `.potm` (PowerPoint documents)
- Automatically creates a `reports/` folder next to the validated file
- Generates timestamped validation reports with detailed error information
- Reports include file metadata, error descriptions, XPath locations, and part URIs

## Usage

### PowerShell (Windows)
```powershell
.\src\scripts\validate\validate.ps1 <file-path>
```

### Bash (Linux/Mac/Git Bash)
```bash
source src/scripts/setup_aliases/setup_aliases.sh
validate <file-path>
```

### Direct C# App Usage
```powershell
.\src\OpenXmlApp\bin\Debug\net8.0\OpenXmlApp.exe validate <file-path>
```

## Examples

```powershell
# Validate a Word template
.\src\scripts\validate\validate.ps1 "core\templates\normal\src\Normal.dotm"

# Validate an Excel template
.\src\scripts\validate\validate.ps1 "resources\defaults\defaultXLSTART\Sheet\Sheet.xltx"

# Using alias (after sourcing setup_aliases.sh in bash)
validate builds/jbc/templates/jbcMemo/out/jbcMemo.dotm
```

## Report Output

Reports are saved to a `reports/` folder in the same directory as the input file:

```
your-file-location/
├── YourFile.dotm
└── reports/
    └── YourFile-validation-20251126-163258.txt
```

### Report Format

```
OOXML Validation Report
======================
File: YourFile.dotm
Full Path: C:\full\path\to\YourFile.dotm
Timestamp: 2025-11-26 16:32:58
File Size: 3,119,755 bytes

Document Type: Word

Found 2 validation error(s):

Error 1:
  Description: The 'firstRow' attribute is not declared.
  Error Type: Schema
  Part: /word/glossary/document.xml
  Path: /w:glossaryDocument[1]/w:docParts[1]/...

======================
Validation PASSED/FAILED
Total Errors: 2
```

## Installation

The validator is automatically built when you build the OpenXmlApp project:

```powershell
cd src\OpenXmlApp
dotnet build --configuration Debug
```

## Implementation Details

- Built using DocumentFormat.OpenXml SDK v3.3.0
- Uses OpenXmlValidator for schema and structural validation
- Supports Office 2007+ file formats (ECMA-376 standard)
- Validates against strict Open XML schemas
