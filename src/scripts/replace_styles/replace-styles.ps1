# OpenXML Replace Styles Script (PowerShell)
# Usage: replace-styles <target-doc> <source-doc>
#   target-doc: Document that will receive new styles (will be modified)
#   source-doc: Document with styles to copy from (read-only)

param(
    [Parameter(Position=0)]
    [string]$TargetDoc,
    
    [Parameter(Position=1)]
    [string]$SourceDoc
)

$ErrorActionPreference = "Stop"

if (-not $TargetDoc -or -not $SourceDoc) {
    Write-Host "Usage: replace-styles <target-doc> <source-doc>"
    Write-Host "  target-doc: Document that will receive new styles (will be modified)"
    Write-Host "  source-doc: Document with styles to copy from (read-only)"
    Write-Host ""
    Write-Host "Example:"
    Write-Host "  replace-styles document.docx template.dotx"
    exit 1
}

# Get the script directory to find the project
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = Resolve-Path (Join-Path $ScriptDir "..\..\..") | Select-Object -ExpandProperty Path
$ProjectFile = Join-Path $ProjectRoot "src\OpenXmlApp\OpenXmlApp.csproj"

# Run the dotnet command
dotnet run --project $ProjectFile -- replace-styles $TargetDoc $SourceDoc
