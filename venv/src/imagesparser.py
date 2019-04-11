
csv_images = [
    'C:/Workspace/csvs/csv_imgs/xaa.csv',
    'C:/Workspace/csvs/csv_imgs/xab.csv',
    'C:/Workspace/csvs/csv_imgs/xac.csv',
    'C:/Workspace/csvs/csv_imgs/xad.csv',
    'C:/Workspace/csvs/csv_imgs/xae.csv',
    'C:/Workspace/csvs/csv_imgs/xaf.csv',
    'C:/Workspace/csvs/csv_imgs/xag.csv',
    'C:/Workspace/csvs/csv_imgs/xah.csv',
    'C:/Workspace/csvs/csv_imgs/xai.csv',
    'C:/Workspace/csvs/csv_imgs/xaj.csv',
    'C:/Workspace/csvs/csv_imgs/xak.csv',
    'C:/Workspace/csvs/csv_imgs/xal.csv',
    'C:/Workspace/csvs/csv_imgs/xam.csv',
    'C:/Workspace/csvs/csv_imgs/xan.csv',
    'C:/Workspace/csvs/csv_imgs/xao.csv',
    'C:/Workspace/csvs/csv_imgs/xap.csv',
    'C:/Workspace/csvs/csv_imgs/xaq.csv',
    'C:/Workspace/csvs/csv_imgs/xar.csv',
    'C:/Workspace/csvs/csv_imgs/xas.csv',
    'C:/Workspace/csvs/csv_imgs/xat.csv',
    'C:/Workspace/csvs/csv_imgs/xau.csv',
    'C:/Workspace/csvs/csv_imgs/xav.csv',
    'C:/Workspace/csvs/csv_imgs/xaw.csv',
    'C:/Workspace/csvs/csv_imgs/xax.csv',
    'C:/Workspace/csvs/csv_imgs/xay.csv',
    'C:/Workspace/csvs/csv_imgs/xaz.csv',
    'C:/Workspace/csvs/csv_imgs/xba.csv',
    'C:/Workspace/csvs/csv_imgs/xbb.csv',
    'C:/Workspace/csvs/csv_imgs/xbc.csv',
    'C:/Workspace/csvs/csv_imgs/xbd.csv'
]

choose_class = "Car"

classes = {}
classes_w_images = {}
with open('C:/Workspace/csvs/class-descriptions-boxable.csv', 'r') as class_file:
    for l in class_file.readlines():
        class_id = l.strip('\n').split(',')[0]
        class_name = l.strip('\n').split(',')[1]
        classes_w_images[class_name] = []
        classes[class_id] = class_name


for file_path in csv_images:
    with open(file_path, 'r') as csv_image:
        for l in csv_image.readlines():
            img_id = l.strip('\n').split(',')[0]
            class_id = l.strip('\n').split(',')[2]
            classes_w_images[classes[class_id]].append(img_id)
    with open(choose_class + ".txt", "a") as file:
        for img_id in classes_w_images[choose_class]:
            file.write(img_id + "\n")

with open(choose_class + ".txt", "r") as file:
    set_id = set(file.readlines())
    with open("Car2.txt", "a") as good_file:
        for img_id in set_id:
            good_file.write(img_id)

