# Replace Styles From Snippet Script (PowerShell)
# Usage: replace-styles-from-snippet <target-doc> <snippet-file> [snippet-id]

param(
    [Parameter(Mandatory=$true, Position=0)]
    [string]$TargetDoc,
    
    [Parameter(Mandatory=$true, Position=1)]
    [string]$SnippetFile,
    
    [Parameter(Position=2)]
    [string]$SnippetId
)

$ErrorActionPreference = "Stop"

if (-not $TargetDoc -or -not $SnippetFile) {
    Write-Host "Usage: replace-styles-from-snippet <target-doc> <snippet-file> [snippet-id]"
    Write-Host "  target-doc: Document that will have styles replaced (will be modified)"
    Write-Host "  snippet-file: XML file containing style snippets"
    Write-Host "  snippet-id: ID of the snippet to use (e.g., 'listStylesDefault')"
    Write-Host ""
    Write-Host "Example:"
    Write-Host "  replace-styles-from-snippet target.docx core\partials\styles\list-styles.xml listStylesDefault"
    exit 1
}

# Get the script directory to find the project
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = Resolve-Path (Join-Path $ScriptDir "..\..\..") | Select-Object -ExpandProperty Path
$ProjectFile = Join-Path $ProjectRoot "src\OpenXmlApp\OpenXmlApp.csproj"

# Run the dotnet command
if ($SnippetId) {
    dotnet run --project $ProjectFile -- replace-styles-from-snippet $TargetDoc $SnippetFile $SnippetId
} else {
    dotnet run --project $ProjectFile -- replace-styles-from-snippet $TargetDoc $SnippetFile
}
