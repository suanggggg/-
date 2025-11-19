<#
Render PlantUML diagram to PNG and SVG using Dockerized PlantUML or local plantuml.jar.

Usage (PowerShell):
  # requires Docker
  .\render_plantuml.ps1 -Input ..\docs\er_diagram.puml -OutDir ..\docs\_images

Or install plantuml.jar and run:
  java -jar plantuml.jar -tpng er_diagram.puml
#>

param(
    [string]$Input = "..\docs\er_diagram.puml",
    [string]$OutDir = "..\docs\_images"
)

if (-not (Test-Path $OutDir)) { New-Item -ItemType Directory -Path $OutDir | Out-Null }

# Try Docker plantuml
Write-Host "Rendering PlantUML via Docker for $Input -> $OutDir"
docker run --rm -v ${PWD}:/workspace plantuml/plantuml:plantuml -tpng -o ".\$(Split-Path $OutDir -Leaf)" $Input
if ($LASTEXITCODE -ne 0) {
    Write-Host "Docker render failed. You can render locally with plantuml.jar: java -jar plantuml.jar -tpng $Input"
}