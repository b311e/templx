# OpenXML Pack Script (PowerShell)
# Usage: pack <source directory> [output file]
# If output file is not provided, it will be auto-generated in the out folder

param(
    [Parameter(Mandatory=$true, Position=0)]
    [string]$SourceDir,
    
    [Parameter(Position=1)]
    [string]$OutputFile
)

$ErrorActionPreference = "Stop"

if (-not $SourceDir) {
    Write-Host "Usage: pack <source directory> [output file]"
    Write-Host "Example: pack builds\jbc\workspace\jbcNormal\in"
    Write-Host "Example: pack builds\jbc\templates\jbcMemo\in"
    Write-Host "Example: pack builds\jbc\workspace\jbcSheet\in builds\jbc\workspace\jbcSheet\out\CustomSheet.xltx"
    exit 1
}

# Get the script directory to find the project
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = Resolve-Path (Join-Path $ScriptDir "..\..\..") | Select-Object -ExpandProperty Path
$ProjectFile = Join-Path $ProjectRoot "src\OpenXmlApp\OpenXmlApp.csproj"

# Run the dotnet command
if ($OutputFile) {
    dotnet run --project $ProjectFile -- pack $SourceDir $OutputFile
} else {
    dotnet run --project $ProjectFile -- pack $SourceDir
}
