import subprocess
import time
from datetime import datetime, timedelta


CMDS_CMD = [
    (
        r'curl --url "https://is.muni.cz/auth/seminare/student?fakulta=1433;obdobi=10103;studium=1320724;predmet=1726876;prihlasit=909732;akce=podrob;provest=1;stopwindow=1;design=m" '
        r'-H "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7" '
        r'-H "accept-language: sk-SK,sk;q=0.9,cs;q=0.8,en-US;q=0.7,en;q=0.6" '
        r'-H "cache-control: max-age=0" '
        r'-b "__Host-issession=8702sA2T03vI33sKBEVdrs57; __Host-iscreds=zdJC3mNQcW1C9VhNp0hNZ99L; _clck=191rx2y%5E2%5Eg1u%5E0%5E2174" '
        r'-H "priority: u=0, i" '
        r'-H "referer: https://is.muni.cz/auth/seminare/student?obdobi=10103;studium=1320724;akce=podrob;predmet=1726876" '
        r'-H "sec-ch-ua: \"Chromium\";v=\"152\", \"Not?A_Brand\";v=\"24\", \"Google Chrome\";v=\"152\"" '
        r'-H "sec-ch-ua-mobile: ?0" '
        r'-H "sec-ch-ua-platform: \"Windows\"" '
        r'-H "sec-fetch-dest: document" '
        r'-H "sec-fetch-mode: navigate" '
        r'-H "sec-fetch-site: same-origin" '
        r'-H "sec-fetch-user: ?1" '
        r'-H "upgrade-insecure-requests: 1" '
        r'-H "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36"'
    ),
    (
        r'curl --url "https://is.muni.cz/auth/seminare/student?fakulta=1433;obdobi=10103;studium=1320724;predmet=1726974;prihlasit=909832;akce=podrob;provest=1;stopwindow=1;design=m" '
        r'-H "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7" '
        r'-H "accept-language: sk-SK,sk;q=0.9,cs;q=0.8,en-US;q=0.7,en;q=0.6" '
        r'-H "cache-control: max-age=0" '
        r'-b "__Host-issession=8702sA2T03vI33sKBEVdrs57; __Host-iscreds=zdJC3mNQcW1C9VhNp0hNZ99L; _clck=191rx2y%5E2%5Eg1u%5E0%5E2174" '
        r'-H "priority: u=0, i" '
        r'-H "referer: https://is.muni.cz/auth/seminare/student?fakulta=1433;obdobi=10103;studium=1320724;akce=podrob;predmet=1726974" '
        r'-H "sec-ch-ua: \"Chromium\";v=\"152\", \"Not?A_Brand\";v=\"24\", \"Google Chrome\";v=\"152\"" '
        r'-H "sec-ch-ua-mobile: ?0" '
        r'-H "sec-ch-ua-platform: \"Windows\"" '
        r'-H "sec-fetch-dest: document" '
        r'-H "sec-fetch-mode: navigate" '
        r'-H "sec-fetch-site: same-origin" '
        r'-H "sec-fetch-user: ?1" '
        r'-H "upgrade-insecure-requests: 1" '
        r'-H "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36"'
    )
]

CMDS_BASH = [
    (
        r"curl --url 'https://is.muni.cz/auth/seminare/student?fakulta=1433;obdobi=10103;studium=1320724;predmet=1726876;prihlasit=909732;akce=podrob;provest=1;stopwindow=1;design=m' "
        r"-H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' "
        r"-H 'accept-language: sk-SK,sk;q=0.9,cs;q=0.8,en-US;q=0.7,en;q=0.6' "
        r"-H 'cache-control: max-age=0' "
        r"-b '__Host-issession=8702sA2T03vI33sKBEVdrs57; __Host-iscreds=zdJC3mNQcW1C9VhNp0hNZ99L; _clck=191rx2y%5E2%5Eg1u%5E0%5E2174' "
        r"-H 'priority: u=0, i' "
        r"-H 'referer: https://is.muni.cz/auth/seminare/student?obdobi=10103;studium=1320724;akce=podrob;predmet=1726876' "
        r"""-H 'sec-ch-ua: "Chromium";v="152", "Not?A_Brand";v="24", "Google Chrome";v="152"' """
        r"-H 'sec-ch-ua-mobile: ?0' "
        r"""-H 'sec-ch-ua-platform: "Windows"' """
        r"-H 'sec-fetch-dest: document' "
        r"-H 'sec-fetch-mode: navigate' "
        r"-H 'sec-fetch-site: same-origin' "
        r"-H 'sec-fetch-user: ?1' "
        r"-H 'upgrade-insecure-requests: 1' "
        r"-H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36'"
    ),
    (
        r"curl --url 'https://is.muni.cz/auth/seminare/student?fakulta=1433;obdobi=10103;studium=1320724;predmet=1726974;prihlasit=909832;akce=podrob;provest=1;stopwindow=1;design=m' "
        r"-H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' "
        r"-H 'accept-language: sk-SK,sk;q=0.9,cs;q=0.8,en-US;q=0.7,en;q=0.6' "
        r"-H 'cache-control: max-age=0' "
        r"-b '__Host-issession=8702sA2T03vI33sKBEVdrs57; __Host-iscreds=zdJC3mNQcW1C9VhNp0hNZ99L; _clck=191rx2y%5E2%5Eg1u%5E0%5E2174' "
        r"-H 'priority: u=0, i' "
        r"-H 'referer: https://is.muni.cz/auth/seminare/student?fakulta=1433;obdobi=10103;studium=1320724;akce=podrob;predmet=1726974' "
        r"""-H 'sec-ch-ua: "Chromium";v="152", "Not?A_Brand";v="24", "Google Chrome";v="152"' """
        r"-H 'sec-ch-ua-mobile: ?0' "
        r"""-H 'sec-ch-ua-platform: "Windows"' """
        r"-H 'sec-fetch-dest: document' "
        r"-H 'sec-fetch-mode: navigate' "
        r"-H 'sec-fetch-site: same-origin' "
        r"-H 'sec-fetch-user: ?1' "
        r"-H 'upgrade-insecure-requests: 1' "
        r"-H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36'"
    )
]

USE_BASH = False

def run_commands():
    CMDS = CMDS_BASH if USE_BASH else CMDS_CMD
    for cmd in CMDS:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding='utf-8')
        print(result.stdout)

def wait_until(hour: int, minute: int = 0):
    """Sleep until the given hour:minute today (or tomorrow if already passed)."""
    now = datetime.now()
    target = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    if target <= now:
        target += timedelta(days=1)
    wait_seconds = (target - now).total_seconds()
    print(f"Waiting until {target.strftime('%Y-%m-%d %H:%M')}...")
    time.sleep(wait_seconds)

if __name__ == "__main__":
    wait_until(16, 25)
    run_commands()
