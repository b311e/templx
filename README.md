# COGA Template Manager

A comprehensive template management system for Colorado General Assembly Microsoft Office templates, including Word (.dotm) and Excel (.xltx) templates with standardized branding and themes.

## Quick Start

### Prerequisites
- [.NET 8.0 SDK](https://dotnet.microsoft.com/download/dotnet/8.0)
- Windows environment (for deployment scripts)
- Access to CGA S Drive (for production deployment)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/b311e/coga-template-manager.git
   cd coga-template-manager
   ```

2. Build the application:
   ```bash
   dotnet build
   ```

3. Set up bash aliases (optional, but recommended):
   ```bash
   source src/scripts/setup_aliases.sh
   ```

## Project Structure

```
coga-template-manager/
├── .coga/                    # COGA system metadata (hidden)
│   ├── registry/             # Agency registry and global configuration
│   └── schemas/              # Manifest validation schemas
│
├── builds/                   # Document / templates files under development
│   ├── core/                 # Custom core templates under development
│   └── <agency>/             # Agency templates and workspace files under development
│       ├── assets/
│       ├── system/           # Deployment and automation scripts
│       ├── templates/        # Document templates (Letterhead, Memo, etc.)
│       └── workspace/        # Office workspace templates (Book, Sheet, Normal, etc.)
│
├── dist/                     # Production-ready deployments
│   ├── <agency>/
│   │   ├── assets/
│   │   ├── system/
│   │   ├── templates/ 
│   │   ├── workspace/
│   └── scripts/              # Core deployment scripts (agency independent)
│
├── docs/                     # Additional project-specific documentation
│    └── template-inventory.md   # Inventory of each agency's templates and their status
│    └── taxonomy.md          # Manifest system documentation
│
├── core/                  # Core templates and components
│   ├── base/                 # Complete base templates
│   ├── data/                 # Resuable data for use in templates or files (e.g., member names)
│   └── partials/             # Reusable components
│
├── resources/                # General reference files and documentation (not project-specific)
│
├── src/
│   ├── OpenXmlApp/           # Core .NET application for template processing
│   └── scripts/              # Bash utility scripts (pack, unpack, create)
```


## Usage


### Working with Templates

Work on templates under the `build` directory.

```bash
# Unpack: Extract documents, spreadsheets, or template to workable folders.
unpack <template_file> [output folder name]

# Pack: Zips the contents into a usable office file.
pack <expanded_folder> [output file name]

# Create: Create new OpenXML documents and templates from scratch.
create <type> [output file name]

```

**Create types:**

| Type            | Ext.         | Description                 |
|-----------------|--------------|-----------------------------|
| xl-book         | xlsx         | Spreadsheet                 |
| xl-mbook        | xlsm         | Macro-enabled Spreadsheet   |
| xl-template     | xltx         | Template                    |
| xl-mtemplate    | xltm         | Macro-enabled Template      |
| word-doc        | docx         | Document                    |
| word-mdoc       | docm         | Macro-enabled Document      |
| word-template   | dotx         | Template                    |
| word-mtemplate  | dotm         | Macro-enabled Template      |

**Usage examples:**

```bash
# Create from scratch
create xl-book

# Or start from core
cp core/workspace/book/Book.xltx builds/jbc/workspace/jbcBook/src/Book.xltx

# Or start from the previous release
cp dist/jbc/workspace/jbcBook/Book.xltx builds/jbc/workspace/jbcBook/src/Book.xltx
```

Style Utilities

```bash
# Style list: Generate style list for template. Automatically saved to the docs folder.
style --list <path to template folder>

# Example:
style --list builds/jbc/workspace/jbcNormal
```

Direct commands (without adding aliases to shell):

```bash
# Unpack: Extract documents, spreadsheets, or template to workable folders.
dotnet run --project src/OpenXmlApp unpack <template_file> [output folder name]

# Pack: Zips the contents into a usable office file.
dotnet run --project src/OpenXmlApp pack <expanded_folder> [output file name]

# Create: Create new OpenXML documents and templates from scratch.
dotnet run --project src/OpenXmlApp create <type> [output file name]
```

### Adding a New Template
1. **Create builds folder structure**:
   ```bash
   # Create src, out, in, and docs folder for the JBC Letterhead template
   mkdir -p builds/jbc/templates/jbcLetterhead/{src,out,in,docs}
   ```

2. **Add template entry** in appropriate section of the `manifest-schema.json`:
   ```json
   "jbcLetterhead": {
     "name": "JBC Letterhead Template",
     "type": "word-doc-template",
     "extension": ".dotx",
     "src": "builds/jbc/templates/jbcLetterhead/src/Report.xltx",
     "out": "builds/jbc/templates/jbcLetterhead/out/Report.xltx",
     "expanded": "builds/jbc/templates/jbcLetterhead/in/",
     "docs": "builds/jbc/templates/jbcLetterhead/docs/",
     "status": "planned"
   }
   ```

4. **Update manifest**:
   ```bash
   manifest --generate jbc
   ```

### Development workflow

Work on templates within the appropriate `builds` directory.

1. Put the source file (original, packed file) in the `src` folder.

2. Unpack the file in the `src` file and store the expanded file within the `in` folder.

   ```bash
   unpack builds/jbc/workspace/jbcBook/src/Book.xltx
   ```

3. Make updates to expanded files within the `in` folder.

4. Once updates are complete and ready for testing, pack the files and store in the `out` folder.

   ```bash
   pack builds/jbc/workspace/jbcBook/in
   ```

5. Right click on the compiled file, select "Validate OOXML", then review the report. Repeat steps 1-4 as necessary.

6. Download the file in the `out` folder and test on your local device in Microsoft Word, Excel, or PowerPoint.

### Create command — behavior & troubleshooting

- Where files are written: the `create` command writes the new template file to the current working directory unless you provide a path as the name.
- Accepted template types (exact strings) are listed above in the creation types table. If you see `Unknown template type`, double-check you're using one of the types above.

- Using the helper script vs. dotnet: there is a convenience wrapper at `src/scripts/create` which forwards to the .NET app. Either:

```bash
# run via the script (recommended)
./src/scripts/create xl-template NewSpreadsheet

# or run the app directly
dotnet run --project src/OpenXmlApp/OpenXmlApp.csproj create excel-sheet-template MySheet
```

- Creating directly into a build output folder: pass a path as the name. Example:

```bash
dotnet run --project src/OpenXmlApp/OpenXmlApp.csproj create xl-template builds/jbc/workspace/jbcNormal/out/NewSpreadsheet.xltx
```

- If you don't see the created file:
   - Confirm the command printed `Created: <filename>` in its output.
   - Check the current directory (run `pwd` / `ls -la`) — the file will be there unless you gave a path.
   - Ensure you have write permissions to the directory and sufficient disk space.
   - If `dotnet run` failed to build the project, inspect the error messages from `dotnet` and run `dotnet build` to surface compile-time errors.

- Future/optional improvement: the tool could be extended to auto-place created files into the `builds/{agency}/.../out` folder based on your current path. If you'd like that behavior, I can add it.

## Template Registry & Manifests

### Manifest Structure

The system uses JSON manifests to track templates, assets, and deployment configurations:

- **Global Registry**: `.coga/registry/agencies.json` - Lists all agencies and their manifest locations
- **Agency Manifests**: `builds/<agency>/manifest.json` - Complete template inventory per agency
- **Schema & Taxonomy**: `.coga/schemas/manifest-schema.json` - Validation schema
  - **Schema documentation:** `docs/taxonomy.md`
- **Category Structure**: Templates organized by workspace, templates, system, and assets

Full  manifest documentation can be found at `src/scripts/manifest_utils/README.md`.

### Manifest Commands

**Generate / update manifest**

```bash
# Generate/update manifest for specific agency
manifest generate <agency>

# Generate/update manifest for core
manifest generate core
```

**Other manifest commands**
```bash
# List all templates across all agencies
manifest list

# Validate all manifest files
manifest validate

# Update template status
manifest update-status jbc jbcNormal active

# Get guidance for adding new templates
manifest add-template jbc jbcReport excel-book-template
```

## Deployment

### Deployment Scripts

- `dist/scripts/workspaceInstallPreProd.bat` - Deploy to PreProd environment
- `dist/scripts/workspaceDeploy.bat` - Deploy from PreProd to Production
- `dist/jbc/jbcWorkspace/JBCTemplateInstall.bat` - End-user installation script
- `style_list list <templateName>` – Generate style list for template. Saves to templateName/docs folder

## Template Inventory System

The template inventory can be found at `docs\template-inventory.md`.

### Generate Template Inventory
The inventory system provides a user-friendly overview of all templates across all agencies:

```bash
# Generate template inventory report
inventory generate

# Show help
inventory --help
```

### Inventory Output
The inventory generates `docs/template-inventory.md` with:
- **Current Status**: Template status pulled from manifests
- **Templates**: Complete listing of House, Senate, JBC, LCS, OLLS, OSA templates
- **Timestamp**: Generated date for tracking currency


**Note:** If you add, remove, or change templates or statuses in any agency manifest, rerun the inventory command to update the list.

### Getting Help
- Check the `docs/` folder for additional documentation
- Review template XML structure in `resources/defaults/`
- Contact the development team for support