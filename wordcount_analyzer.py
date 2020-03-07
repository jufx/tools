from tools.aggregator import Aggregator
from re import findall

PATHS = ["/home/meb/PycharmProjects/", "/home/meb/Bureau/"]
EXT = ['**/*.py', '**/*.ipynb']
RESULTS_URLS=[]



# gather files
for PATH in PATHS:
    for extension in EXT:
        A = Aggregator(path_to_files=PATH, pattern=extension)
        for result in A.matching_list:
            RESULTS_URLS.append(result)
print(len(RESULTS_URLS))

JUICY_LINES = []
RE_PATTERNS = ['from', 'import']
files_done = 0

# gather lines
for file_url in RESULTS_URLS:
    with open(file_url, mode='r') as py_script:
        for lines in py_script:
            for pattern in RE_PATTERNS:
                brute=findall(pattern=pattern,string=lines)
                if brute:
                    brute=brute[0].strip('"').replace('\n', '').replace('"', '').replace(',', '')
                    if pattern == brute[0:len(pattern)] : # and lines.replace('\n', '').replace('"', '').replace(',', '').replace('.', ' ').replace(RE_PATTERNS[0], '').replace(RE_PATTERNS[1], '').replace ('  ', ' ') not in JUICY_LINES
                        JUICY_LINES.append(lines.replace('\n', '').replace('"', '').replace(',', '').replace('.', ' ').replace(RE_PATTERNS[0], '').replace(RE_PATTERNS[1], '').replace ('  ', ' '))
        files_done += 1
        print(100 * files_done / len(RESULTS_URLS))

for line in JUICY_LINES:
    print(line.replace('\n', ''))