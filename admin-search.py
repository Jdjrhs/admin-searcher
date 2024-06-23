import requests

def print_banner():
    banner = """
            _                                                               _                  
           ( )            _                                                ( )                 
   _ _    _| |  ___ ___  (_)  ___   ______   ___    __     _ _  _ __   ___ | |__     __   _ __ 
 /'_` ) /'_` |/' _ ` _ `\| |/' _ `\(______)/',__) /'__`\ /'_` )( '__)/'___)|  _ `\ /'__`\( '__)
( (_| |( (_| || ( ) ( ) || || ( ) |        \__, \(  ___/( (_| || |  ( (___ | | | |(  ___/| |   
`\__,_)`\__,_)(_) (_) (_)(_)(_) (_)        (____/`\____)`\__,_)(_)  `\____)(_) (_)`\____)(_)  
by ZxPLOIT and ChatGpt, 15 admin list
    """
    print(banner)

def scan_admin_paths(url):
    paths = ['/wp-login.php', 
    '/phpmyadmin',  
     '/admin',
    '/administrator',
    '/login',
    '/wp-admin',
    '/kpanel',
    '/panel',
    '/login.php',
    '/admin/login',
    '/administrator/login',
    '/siteadmin',
    '/admincp',
    '/adminarea',
    '/adminLogin']
    for path in paths:
        full_url = url + path
        try:
            response = requests.get(full_url)
            if response.status_code == 200:
                if path == '/wp-login.php':
                    print(f"Ketemu!, ternyata {path} adalah wordpress")
                elif path == '/phpmyadmin':
                    print(f"Ketemu!, ternyata {path} adalah phpmyadmin")
                elif path == '/admin':
                    print(f"Ketemu!, ternyata {path} adalah admin")
                elif path == '/administrator':
                    print(f"Ketemu!, ternyata {path} adalah administrator")
                elif path == '/login':
                    print(f"Ketemu!, ternyata {path} adalah login")
                elif path == '/wp-admin':
                    print(f"Ketemu!, ternyata {path} adalah wpadmin")
                elif path == '/kpanel':
                    print(f"Ketemu!, ternyata {path} adalah cpanel")
                elif path == '/panel':
                    print(f"Ketemu!, ternyata {path} adalah panel")
                elif path == '/login.php':
                    print(f"Ketemu!, ternyata {path} adalah login.php")
                elif path == '/admin/login':
                    print(f"Ketemu!, ternyata {path} adalah admin/login")
                elif path == '/administrator/login':
                    print(f"Ketemu!, ternyata {path} adalah administrator/login")
                elif path == '/siteadmin':
                    print(f"Ketemu!, ternyata {path} adalah siteadmin")
                elif path == '/admincp':
                    print(f"Ketemu!, ternyata {path} adalah admincp")
                elif path == '/adminarea':
                    print(f"Ketemu!, ternyata {path} adalah adminarea")
                elif path == '/adminLogin':
                    print(f"Ketemu!, ternyata {path} adalah adminLogin")
            else:
                print(f"Tidak ditemukan: {path}")
        except requests.exceptions.RequestException as e:
            print(f"Error saat mengakses {full_url}: {e}")

def main():
    print_banner()
    url = input("URL: ").strip()
    scan_admin_paths(url)

if __name__ == "__main__":
    main()
