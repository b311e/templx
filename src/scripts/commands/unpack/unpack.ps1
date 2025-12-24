# OpenXML Unpack Script (PowerShell)
# Usage: unpack <file path>

param(
    [Parameter(Mandatory=$true, Position=0)]
    [string]$FilePath
)

$ErrorActionPreference = "Stop"

if (-not $FilePath) {
    Write-Host "Usage: unpack <file path>"
    Write-Host "Example: unpack templates\jbc\jbcBook\source\Book.xltx"
    exit 1
}

# Get the script directory to find the project
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = Resolve-Path (Join-Path $ScriptDir "..\..\..") | Select-Object -ExpandProperty Path
$ProjectFile = Join-Path $ProjectRoot "src\OpenXmlApp\OpenXmlApp.csproj"

# Run the dotnet command
dotnet run --project $ProjectFile -- unpack $FilePath
