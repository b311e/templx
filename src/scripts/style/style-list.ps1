# List Styles Script (PowerShell)
# Usage: list-styles <templatePath>

param(
    [Parameter(Mandatory=$true, Position=0)]
    [string]$TemplatePath
)

$ErrorActionPreference = "Stop"

if (-not $TemplatePath) {
    Write-Host "Usage: list-styles <templatePath>"
    Write-Host ""
    Write-Host "ARGUMENTS:"
    Write-Host "  templatePath    Path to template directory in format: builds\<agency>\<category>\<templateName>"
    Write-Host "                  templateName folder should contain in/, out/, src/, etc. folders"
    Write-Host ""
    Write-Host "DESCRIPTION:"
    Write-Host "  Extracts Word styles from templates and generates a style list."
    Write-Host "  Looks for styles.xml in in\word\ or expanded\word\ subdirectories."
    Write-Host "  Output is saved to docs\style-list-{templateName}.txt in the template directory."
    Write-Host ""
    Write-Host "EXAMPLES:"
    Write-Host "  list-styles builds\jbc\workspace\jbcNormal"
    exit 1
}

# Get the script directory to find the bash script
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$BashScript = Join-Path $ScriptDir "style\style"

# Check if Git Bash is available
$GitBash = "C:\Program Files\Git\bin\bash.exe"
if (-not (Test-Path $GitBash)) {
    Write-Host "Error: Git Bash not found at: $GitBash"
    Write-Host "This script requires Git Bash. Please install Git for Windows."
    exit 1
}

# Convert Windows path to Unix-style if needed
$UnixPath = $TemplatePath -replace '\\', '/'
& $GitBash -c "bash '$BashScript' --list '$UnixPath'"
