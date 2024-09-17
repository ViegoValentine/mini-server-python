@echo off
setlocal enabledelayedexpansion

REM Uzyskanie aktualnej daty i godziny
for /f "delims=" %%a in ('wmic OS Get localdatetime ^| find "."') do set datetime=%%a

set "year=%datetime:~0,4%"
set "month=%datetime:~4,2%"
set "day=%datetime:~6,2%"

for /f "tokens=1-2 delims=: " %%a in ('time /t') do set "godzina=%%a%%b"

REM Utworzenie nazwy raportu z daty i godziny
set "nazwa_backup=backup-raport-%year%-%month%-%day%-!godzina!"
set "nazwa_raport=raport-%year%-%month%-%day%-!godzina!"

:menu
cls
echo MENU:
echo 1. Start - Uruchomienie pierwszego i drugiego programu
echo 2. Informacje - Wyswietlenie informacji o skrypcie
echo 3. Backup - Stworzenie i wyswietlenie backupu z raportu
echo 4. Zakoncz - Zakoncz prace skryptu

set /p wybor="Wybierz opcje: "

if "%wybor%"=="1" goto start
if "%wybor%"=="2" goto informacje
if "%wybor%"=="3" goto backup
if "%wybor%"=="4" goto koniec

:start
echo Uruchamianie pierwszego programu...
python funkcja.py

echo.
echo Uruchamianie drugiego programu...
python uRaport.py %nazwa_raport%

pause
goto menu

:informacje
echo Informacje o skrypcie:
echo - Skrypt ma za zadanie obliczyc wartosci funkcji kwadratowej, zadanej w pliku txt,
echo utworzenie pliku wyjsciowego z wynikami, a nastepnie 
echo stowrzenie raportu w pliku html.
echo - Możliwosc stworzenia bakupu wygenerowanego wczesniej raportu.
pause
goto menu

:backup
echo Tworzenie i wyswietlanie backupu z raportu w formacie HTML...
python uRaport.py %nazwa_backup%
start %nazwa_backup%.html
pause
goto menu

:koniec
echo Zakonczono prace skryptu.
exit /b
