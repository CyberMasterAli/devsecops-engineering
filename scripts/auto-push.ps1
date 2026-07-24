param(
    [Parameter(Mandatory = $false)]
    [string]$Message = "chore: update DevSecOps project"
)

$ErrorActionPreference = "Stop"

Write-Host "Starting repository update..." -ForegroundColor Cyan

$projectRoot = Split-Path -Parent $PSScriptRoot
Set-Location $projectRoot

if (-not (Test-Path ".git")) {
    Write-Error "This folder is not a Git repository."
    exit 1
}

$currentBranch = git branch --show-current

if (-not $currentBranch) {
    Write-Error "Unable to identify the current Git branch."
    exit 1
}

Write-Host "Current branch: $currentBranch" -ForegroundColor Yellow

Write-Host "`nReviewing changes:" -ForegroundColor Cyan
git status --short

$confirmation = Read-Host "`nType YES to add, commit and push these changes"

if ($confirmation -ne "YES") {
    Write-Host "Operation cancelled. No changes were pushed." -ForegroundColor Yellow
    exit 0
}

git add .

$stagedChanges = git diff --cached --name-only

if (-not $stagedChanges) {
    Write-Host "No changes are available to commit." -ForegroundColor Yellow
    exit 0
}

Write-Host "`nFiles staged for commit:" -ForegroundColor Cyan
$stagedChanges

git commit -m $Message

if ($LASTEXITCODE -ne 0) {
    Write-Error "Git commit failed."
    exit 1
}

git push origin $currentBranch

if ($LASTEXITCODE -ne 0) {
    Write-Error "Git push failed."
    exit 1
}

Write-Host "`nChanges successfully pushed to GitHub." -ForegroundColor Green