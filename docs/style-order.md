# How to order styles in styles.xml

## Style Order in styles.xml

```
Built-in Styles
    Paragraph Styles
        Default
            {Normal}
            {Default Paragraph Font}
        Heading
        Body
            {No Spacing}
        Front Matter
            {Title}
            {Subtitle}
        List
            {List Paragraph}
            {List Bullet}
            {List Number}
        Callout
            {Quote}
            {Intense Quote}
            {Block Text}
        Caption
            {Caption}
        TOC
        Index
        Header
        Footer
        Optional / Other
            {Signature}
            {Date}
    Character Styles
        {Strong}
    Table Styles
    Numbering Styles

Custom Styles (Always Included)
    Paragraph Styles
        Body
            {Space Before}
            {Space After}
        Front Matter
            {Pretitle}
        List
        Optional / Other
            {Table Title}
    Character Styles
        {Underline}
        {Strikethrough}
    Table Styles
    Numbering Styles

Custom Styles (Template-Specific)
    Paragraph Styles
        Heading
        Body
        Front Matter
        List
        Callout
        Caption
        Header
        Footer
        Optional / Other
    Character Styles
    Table Styles
    Numbering Styles
```

## Always Include These Styles

Always include these built-in styles in the styles.xml to make sure they are hidden or placed last (priority 99).

Paragraph Styles:
- Title (priority 99)
- Book Title (priority 99)
- Bibliography (priority 99)
- List Paragraph (priority 99)
- Caption (priority 99)

Character Styles:
- Strong
- Emphasis
- Intense Emphasis
- Subtle Emphasis


