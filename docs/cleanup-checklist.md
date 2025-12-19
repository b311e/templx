# WordprocessingML Cleanup Checklist

## Automated Checker

### Revision Tracking (RSID) Removal
- [ ] Remove all `rsidR`, `rsidRPr`, `rsidDefault`, `rsidP`, and `rsidSect` attributes from styles
- [ ] Remove the entire `<w:rsids>` block from `word/settings.xml`:


```xml
<!-- Example -->
<w:rsids>
    <w:rsidRoot w:val="00346D74" />
    <w:rsid w:val="00015C8E" />
</w:rsids>
```

### Normal Style Standards

- [ ] Ensure Normal style has no aliases (`<w:aliases>`)
- [ ] Verify `<w:qFormat />` is present
- [ ] Confirm Normal style only contains these attributes:
```xml
<w:style w:type="paragraph" w:default="1" w:styleId="Normal">
    <w:name w:val="Normal" />
    <w:qFormat />
</w:style>
```
- [ ] Remove any unnecessary formatting from Normal (fonts, spacing, etc.)

### Proofing & Language

- [ ] Remove `<w:noProof />` to enable spelling/grammar checking:
```regex
^[ \t]*<w:noProof\s*\/>\r?\n
```
- [ ] Clean up empty `<w:rPr>` blocks after removing `noProof`

### Font Handling

- [ ] Remove `<w:iCs />` (italic for Complex Scripts/East Asian fonts):
```regex
^[ \t]*<w:iCs\s*\/>\r?\n
```
- [ ] Remove `<w:szCs />` (size for Complex Scripts)
- [ ] Replace hard-coded fonts in Headings with theme fonts:
  - Replace `<w:rFonts w:ascii="Calibri" .../>` with `<w:rFonts w:asciiTheme="majorHAnsi" .../>` 
- [ ] Remove `<w:bCs />` (bold for Complex Scripts) if not needed
- [ ] Remove `<w:lang w:bidi="ar-SA"/>` or other unwanted language settings

### Heading Styles

- [ ] Ensure all Headings use `majorHAnsi` theme fonts (not hard-coded)
- [ ] Remove linked Heading character styles:
  - Delete the character style definition (e.g., `Heading 1 Char`)
  - Remove `<w:link w:val="Heading1Char"/>` from paragraph style
- [ ] Verify Heading hierarchy is correct (basedOn relationships)


### Style Cleanup

- [ ] Remove duplicate style definitions
- [ ] Check for and remove empty `<w:pPr>` or `<w:rPr>` blocks

### Latent Styles

- [ ] Review `<w:latentStyles>` - ensure defaults are compliant with standards

### Table Styles

- [ ] Verify table styles use theme colors (not hard-coded RGB)
- [ ] Ensure default table style is set appropriately

### Theme Integration

- [ ] Replace hard-coded colors with theme colors (`w:themeColor` instead of `w:val`)
- [ ] Replace hard-coded fonts with theme fonts (`w:asciiTheme`, `w:hAnsiTheme`)
- [ ] Verify theme font references: `minorHAnsi`, `majorHAnsi`, etc.

### Namespace & Compatibility
- [ ] Verify `mc:Ignorable` includes all optional namespaces
- [ ] Check for invalid or deprecated elements

### Settings.xml Cleanup
- [ ] Remove revision tracking settings
- [ ] Check `<w:compat>` settings are appropriate for target Word version

### Final Validation
- [ ] Validate XML is well-formed (no syntax errors)


## Manual Validation

### Heading Styles

- [ ] Ensure `<w:qFormat />` is present on all Headings that must appear in Quick Styles panel.

### Style Cleanup

- [ ] Remove unused custom styles
- [ ] Remove `<w:semiHidden />` if you want styles visible
- [ ] Remove `<w:unhideWhenUsed />` if not needed

### Table Styles

- [ ] Remove unused table style definitions

### Settings.xml Cleanup

- [ ] Remove unnecessary `<w:activeWritingStyle>` entries
- [ ] Review and clean `<w:autoHyphenation>`, `<w:doNotHyphenateCaps>`, etc.

### Final Validation
- [ ] Pack the template and test opening in Word
- [ ] Verify all styles display correctly
- [ ] Check that theme colors/fonts apply properly
- [ ] Test with a new document created from the template