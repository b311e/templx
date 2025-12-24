# OOXML Validation Script (PowerShell)
# Usage: validate-ooxml <file-path>
# Validates Office Open XML documents and saves a report to a "reports" folder
# in the same directory as the input file.

param(
    [Parameter(Mandatory=$true, Position=0)]
    [string]$FilePath
)

$ErrorActionPreference = "Stop"

if (-not $FilePath) {
    Write-Host "Usage: validate-ooxml <file-path>"
    Write-Host "Example: validate-ooxml builds\jbc\workspace\jbcNormal\Normal.dotm"
    Write-Host ""
    Write-Host "Supported file types:"
    Write-Host "  Word: .docx, .docm, .dotx, .dotm"
    Write-Host "  Excel: .xlsx, .xlsm, .xltx, .xltm"
    Write-Host "  PowerPoint: .pptx, .pptm, .potx, .potm"
    exit 1
}

# Get the script directory to find the project
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = Resolve-Path (Join-Path $ScriptDir "..\..\..") | Select-Object -ExpandProperty Path
$OpenXmlApp = Join-Path $ProjectRoot "src\OpenXmlApp\bin\Debug\net8.0\OpenXmlApp.exe"

# Check if file exists
if (-not (Test-Path $FilePath)) {
    Write-Host "Error: File not found: $FilePath"
    exit 1
}

# Check if OpenXmlApp is built
if (-not (Test-Path $OpenXmlApp)) {
    Write-Host "OpenXmlApp not found. Building..."
    Push-Location (Join-Path $ProjectRoot "src\OpenXmlApp")
    dotnet build --configuration Debug
    Pop-Location
}

# Run validation
& $OpenXmlApp validate $FilePath
