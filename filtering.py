def nomi_filter():
    print("""
█▀▄ █▀█ █▀▄▀█ ▄▀█ █ █▄░█   █▀▀ █ █░░ ▀█▀ █▀▀ █▀█ █ █▄░█ █▀▀
█▄▀ █▄█ █░▀░█ █▀█ █ █░▀█   █▀░ █ █▄▄ ░█░ ██▄ █▀▄ █ █░▀█ █▄█
          - eclibse security labs
          - visit : https://eclibsesec.tech""")
    extensions_input = input("$ extension allowed (pisahkan dengan koma, contoh: go.id,ac.id,sch.id): ")
    allowed_domains = set()
    for ext in extensions_input.split(','):
        ext = ext.strip()
        if not ext.startswith('.'):
            ext = '.' + ext
        allowed_domains.add(ext)
    input_file = input("$ give me your list: ")
    output_file = input("$ save to: ")
    domains = set()
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip().lower()
                for ext in allowed_domains:
                    if line.endswith(ext):
                        domains.add(line)
                        break
    except UnicodeDecodeError:
        print(f"Error decoding the file '{input_file}'. Please check the file encoding.")
    with open(output_file, 'w', encoding='utf-8') as f:
        for domain in domains:
            f.write(domain + '\n')
    print(f"done! check at '{output_file}'")

# Memanggil fungsi
nomi_filter()
