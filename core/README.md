# Core Templates

The core directory contains the base templates and reusable components used to create agency-specific templates.

## Directory Structure

```
core/
├── base/                   # Complete base templates
│   ├── workspace/
│   │   ├── book/
│   │   │   └── Book.xltx
│   │   ├── colors/
│   │   │   └── Colors.xml
│   │   ├── fonts/
│   │   │   └── Fonts.xml
│   │   ├── normal/
│   │   │   └── Normal.dotm
│   │   ├── officeUI/
│   │   │   ├── excel.OfficeUI
│   │   │   └── word.OfficeUI
│   │   ├── sheet/
│   │   │   └── Sheet.xltx
│   │   └── theme/
│   │        └── Theme.thmx
│   └── templates/
├── partials/              # Reusable components
│   ├── styles/            # Standard style definitions
│   ├── numbering/         # Standard numbering definitions
│   └── snippets/          # Other useful XML elements
```

## Usage

### Creating New Agency Templates

1. **Start with Base Template**
   ```bash
   cp core/base/excel/Book-Base.xltx templates/[agency]/book/template.xltx
   ```

2. **Customize for Agency**
   ```bash
   unpack templates/[agency]/book/template.xltx
   # Edit template/ folder with agency-specific changes
   pack template/ templates/[agency]/book/template.xltx
   ```

### Core Principles

- **Base templates** are complete, working templates ready for customization
- **Partials** are reusable components that can be mixed and matched
- - Core templates use neutral styling that's easy to customize
- All templates maintain proper OpenXML structure and Office compatibility

---

*These are the core building blocks for all agency templates. Handle with care and test thoroughly.*