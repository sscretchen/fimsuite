Function Capture-File-Hash($filepath) {
    $filehash = Get-FileHash -Path $filepath -Algorithm SHA512
    return $filehash
}

Function Delete-Existing-Baseline() {
    $baselineCheck = Test-Path -Path .\baseline.txt
    if ($baselineCheck){
        # Delete file
        Remove-Item -Path .\baseline.txt
    }
}

Write-Host "`n[1] Make sure your are IN THE DIRECTORY to be monitored" -ForegroundColor Green
Write-Host "[2] Create empty basline.txt file to write to" -ForegroundColor Green
read-host “Once steps above are complete, Press ENTER to continue”

Write-Host "Set task:"
Write-Host "[A] Capture Baseline"
Write-Host "[B] Monitor existing baseline"

$response = Read-Host -Prompt "[...] Please make selection"

if ($response -eq "A".ToUpper()) {
    # Delete existing Baseline
    Delete-Existing-Baseline

    # Calculate target file hash and store in .txt file
    Write-Host "`n[+] Calculating hashes. Saving to baseline.txt" -ForegroundColor Cyan

    # Collect files
    $files = Get-ChildItem -Path .\testFiles

    # Hash each file, write to baseline
    foreach ($f in $files){
        $hash = Capture-File-Hash $f.FullName
        "$($hash.Path) | $($hash.Hash)" | Out-File -FilePath .\baseline.txt -Append
    }
}

elseif ($response -eq "B".ToUpper()) {
    # Start of monitoring
    $cwd = Get-Location
    Write-Host "[+] Monitoring Path: $($cwd)" -ForegroundColor Magenta
    $hashDict = @{}

    # Load existing basleine, store hashes in an array
    $captureFpathFhash = Get-Content -Path .\baseline.txt

    foreach ($f in $captureFpathFhash) {
         $hashDict.add($f.Split("|")[0],$f.Split("|")[1])
    }

    # Begin monitoring with existing baseline (infinite loop for now, need a memory friendly alternative)
    while ($true) {
        Start-Sleep -Seconds 2

        $files = Get-ChildItem -Path .\testFiles

        # Capture hash of each file, match to baseline ofr status
        foreach ($f in $files) {
            $hash = Capture-File-Hash $f.FullName

            # Flag for file creation & changes
            if ($hashDict[$hash.Path] -eq $null) {
                Write-Host "[+] $($hash.Path) has been created!" -ForegroundColor Green
            }
            else {
                # logic break (better solution? This breaks the loop, continues monitoring)
                if ($hashDict[$hash.Path] -eq $hash.Hash) {
                    # The file has not changed
                }
                else {
                    Write-Host "[!] $($hash.Path) has changed!" -ForegroundColor Yellow
                }
            }
        }

        # internal dir to check for baseline deletions
        foreach ($key in $hashDict.Keys){
            $existingBaseline = Test-Path -Path $key
            if (-Not $existingBaseline) {
                Write-Host "[!!] $($key) has been deleted!" -ForegroundColor Red
            }
        }
    }
}
else {
    # Catch invalid input
    Write-Host "[x] Invalid input. Please choose option A or B" -ForegroundColor Red
}
