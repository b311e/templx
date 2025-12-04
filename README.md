# COGA Template Manager

A comprehensive template management system for Colorado General Assembly Microsoft Office templates, including Word (.dotm) and Excel (.xltx) templates with standardized branding and themes.

## Setup on Windows

1. **Install Prerequisites**
   - [.NET 8.0 SDK](https://dotnet.microsoft.com/download/dotnet/8.0)
   - [Git for Windows](https://git-scm.com/download/win) (includes Git Bash)
   - Python 3 (optional, only needed for manifest utilities)

2. **Clone Repository**
   ```bash
   git clone https://github.com/b311e/coga-template-manager.git
   cd coga-template-manager
   ```

3. **Build OpenXML Tools**
   ```bash
   dotnet build
   ```

4. **Set Up Bash Aliases** (in Git Bash)
   ```bash
   source src/scripts/setup_aliases/setup_aliases.sh
   ```
   This adds shortcuts: `pack`, `unpack`, `xpathsel`, `create-template`

5. **Start Working**
   - Templates are in `builds/<agency>/templates/`
   - Use `unpack` to extract .dotm files for editing
   - Use `pack` to rebuild templates after changes

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

## Usage

### Pack & Unpack

- Always work on templates under the `build` directory.
- Unpacked working files should go under an `in` folder.
- Packed filed should go under an `out` folder.

```bash
# Unpack: Expand spreadsheets, documents, or templates.
unpack <target-doc> <output-file-name>

# Pack: Zips the contents into a usable office file.
pack <expanded-file> <output-file-name>
```

### Create New Files

The `create` command writes the new template file to the current working directory unless you provide a path as the name.

```bash
# Create: Create a OpenXML file from scratch
create <create-type> <output-file-name>
```
**Create Types:**

| Create Type            | Ext.         | Description                 |
|-----------------|--------------|-----------------------------|
| `xl-book`         | xlsx         | Spreadsheet                 |
| `xl-mbook`        | xlsm         | Macro-enabled Spreadsheet   |
| `xl-template`     | xltx         | Spreadsheet Template                    |
| `xl-mtemplate`    | xltm         | Macro-enabled Spreadsheet Template      |
| `word-doc`        | docx         | Document                   |
| `word-mdoc`       | docm         | Macro-enabled Document      |
| `word-template`   | dotx         | Document Template                    |
| `word-mtemplate`  | dotm         | Macro-enabled Document Template      |

### Create New Snippets

Use the `create-snippet-styles` command to create new snippet files from a word doc or template.

```bash
create-snippet-styles <source-expanded-folder> <snippet-id> <style-id>,<style-id>
```

#### Snippet IDs

Snippet Ids should be unique, camel case, and follow this naming convention: 
`[scope][Template][StyleGroup][SnippetType]`.

   - `scope` = core or agency (jbc, olls, lcs, etc.)
   - `Template` = The name of the template the snippet comes from, without the agency (e.g., Normal, AuditReport, etc.).
   - `StyleGroup` = The group the style belongs to. See snippets-order-of-operations.yaml (this file will be updated and moved in the future.)
   - `SnippetType` = The type of snippet it is (styles, numbering, etc.)

#### Style IDs

Style IDs is the unique name of a style within a word doc's `styles.xml`. 
- Style IDs never include spaces or special characters. 
- Note: Although xml is case sensitive, the script is not. You do not need to match the case of a Style ID you enter in the command line with the case in the `styles.xml`.



### Style Utilities

#### List Styles

```bash
# Style list: Generate style list for an unpacked template. Automatically saved to the docs folder.
styles-list <template-name>
```

#### Import & Merge Styles

```bash
# Import styles: Import styles from one Word document to another
styles-import <target-doc> <source-doc>

# Import styles from snippet: Import styles from XML snippet to Word document or template
styles-import-snippet <target-doc> <snippet-id>
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
│   └── scripts/              # Bash utility scripts 
```

## Workflows

### Add a New Template

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
   
   ```

### Development workflow

Work on templates within the appropriate `builds` directory.

1. Put the source file (original, packed file) in the `src` folder. Do not edit the file in this folder.

2. **Unpack** the file in the `src` file, then copy it into the template build folder and rename it to `in`.

   It should look like this:
   ```
   ├── builds/
   │   └── <agency>/
   │       └── templates/
   │           └── <templateName>/
   │               ├── docs/
   │               ├── in/
   │               ├── out/
   │               └── src/
   ```

3. **Make changes:** Make updates to expanded files within the `in` folder.

4. **Pack:** Once updates are complete and ready for testing, pack the files and store in the `out` folder.

5. **Validate:** Validate the packed file using one of the methods below.

   a. Validate the file using the `validate` command (recommended). This will generate a txt file within a `reports` folder in the same directory as the target file.
   
   b. Right click on the compiled file, select "Validate OOXML", then review the report. 

6. Download the file in the `out` folder and test on your local device in Microsoft Word, Excel, or PowerPoint.


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

#### Generate / update manifest

```bash
# Generate/update manifest for specific agency
manifest-generate <agency>

# Generate/update manifest for core templates
manifest-generate core
```

#### Other manifest commands
```bash
# List all templates across all agencies
manifest-list

# Validate all manifest files
manifest-validate

# Update template status
manifest-update-status jbc jbcNormal active

# Get guidance for adding new templates
manifest-add-template jbc jbcReport excel-book-template
```

## Deployment

### Deployment Scripts

- `dist/scripts/workspaceInstallPreProd.bat` - Deploy to PreProd environment
- `dist/scripts/workspaceDeploy.bat` - Deploy from PreProd to Production
- `dist/jbc/jbcWorkspace/JBCTemplateInstall.bat` - End-user installation script
- `styles-list <templatePath>` – Generate style list for template. Saves to templatePath/docs folder

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