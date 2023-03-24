def get_link_img(link):
    return f'<img height="300px" width="300px" src="https://{link}">'


def get_html(links_f):
    return f"""
<!DOCTYPE HTML>
<html>
 <head>
  <meta charset="utf-8">
 </head>
 <body> 
    {links_f}
 </body>
</html>
"""


def gen_html_img(r_file):
    links_img = []
    try:
        with open(r_file, 'r', encoding='latin-1') as file:
            for line in file.readlines():
                if "https://sun" in line:
                    link = line.split("https://")[-1].strip().rstrip()
                    links_img.append(link)
            l = "".join(get_link_img(f) for f in links_img)
            r_file = r_file.split(".")[0]
            with open(f"{r_file}.html", 'w', encoding='utf-8') as out_file:
                out_file.write(get_html(l))
    except FileNotFoundError:
        print("Unable to read file")

