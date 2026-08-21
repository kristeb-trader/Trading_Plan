# ============================================================
#  SETUP - Estructura de carpetas del proyecto Chaumer
#  Uso: abrir PowerShell y ejecutar:  .\00_SETUP_Estructura.ps1
# ============================================================

$Raiz = "E:\Proyectos\Chaumer"

$Carpetas = @(
    "00_Guias",
    "01_Plan",
    "01_Plan\subfases",
    "02_Assets",
    "02_Assets\validos",
    "02_Assets\invalidos",
    "02_Assets\frontera",
    "02_Assets\test_ciego",
    "02_Assets\diagramas",
    "03_Materia_Prima",
    "04_Web",
    "05_Backtesting",
    "05_Backtesting\datos",
    "05_Backtesting\sql",
    "06_Dashboard",
    "99_Archivo"
)

Write-Host "Creando estructura en $Raiz ..." -ForegroundColor Cyan

foreach ($c in $Carpetas) {
    $ruta = Join-Path $Raiz $c
    if (-not (Test-Path $ruta)) {
        New-Item -ItemType Directory -Path $ruta -Force | Out-Null
        Write-Host "  [+] $c"
    } else {
        Write-Host "  [=] $c (ya existe)" -ForegroundColor DarkGray
    }
}

# Archivos base del plan (solo si no existen)
$Base = @{
    "01_Plan\TRADING_PLAN_CHAUMER.md" = "# TRADING PLAN - Estrategia Chaumer (NQ / NinjaTrader 8)`r`n`r`nVersion: 0.1 (en construccion)`r`nUltima actualizacion: $(Get-Date -Format 'yyyy-MM-dd')`r`n"
    "01_Plan\reglas.json"             = "[]`r`n"
    "01_Plan\PENDIENTES.md"           = "# PENDIENTES`r`n`r`nReglas sin cerrar y decisiones aplazadas.`r`n"
    "01_Plan\GLOSARIO.md"             = "# GLOSARIO OPERATIVO`r`n`r`nCada termino con su definicion medible.`r`n"
}

foreach ($f in $Base.Keys) {
    $ruta = Join-Path $Raiz $f
    if (-not (Test-Path $ruta)) {
        Set-Content -Path $ruta -Value $Base[$f] -Encoding UTF8
        Write-Host "  [+] $f" -ForegroundColor Green
    }
}

# Control de versiones del proyecto (opcional pero recomendado)
Set-Location $Raiz
if (-not (Test-Path (Join-Path $Raiz ".git"))) {
    git init | Out-Null
    Set-Content -Path (Join-Path $Raiz ".gitignore") -Value "04_Web/`r`n99_Archivo/`r`n*.tmp`r`n" -Encoding UTF8
    git add . | Out-Null
    git commit -m "Estructura inicial del proyecto Chaumer" | Out-Null
    Write-Host "`nRepositorio git inicializado (04_Web excluido: sera su propio repo)." -ForegroundColor Yellow
}

Write-Host "`nListo. Deja las tres guias en: $Raiz\00_Guias" -ForegroundColor Cyan
