# OpenXML Create Script (PowerShell)
# Usage: create <templateType> [outputFileName]

param(
    [Parameter(Mandatory=$true, Position=0)]
    [string]$TemplateType,
    
    [Parameter(Position=1)]
    [string]$OutputFileName
)

$ErrorActionPreference = "Stop"

# Get the script directory to find the project
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = Resolve-Path (Join-Path $ScriptDir "..\..\..") | Select-Object -ExpandProperty Path
$ProjectFile = Join-Path $ProjectRoot "src\OpenXmlApp\OpenXmlApp.csproj"

# Run the dotnet command
if ($OutputFileName) {
    dotnet run --project $ProjectFile -- create $TemplateType $OutputFileName
} else {
    dotnet run --project $ProjectFile -- create $TemplateType
}
