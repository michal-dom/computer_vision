import urllib.request

csv_urls = [
    'C:/Workspace/csvs/csv_urls/xaa.csv',
    'C:/Workspace/csvs/csv_urls/xab.csv',
    'C:/Workspace/csvs/csv_urls/xac.csv',
    'C:/Workspace/csvs/csv_urls/xad.csv'
]

# import urllib.request

img_ids = []

with open("Car2.txt", "r") as myfile:
    for l in myfile.readlines():
        img_ids.append(l.strip("\n"))

i = 0
for file in csv_urls:
    with open(file, 'r', encoding="utf8") as images_file:
        for l in images_file.readlines():
            img_id = l.strip('\n').split(',')[0]
            url = l.strip('\n').split(',')[2]
            if(img_id in img_ids):
                try:
                    urllib.request.urlretrieve(url, "img/car/car" + str(i) + ".jpg")
                    with open("Carurl.txt", "a") as good_file:
                        good_file.write(url)
                except:
                    print("err")
            i += 1
    # i += 1

