import sys
from pathlib import Path
import os
import shutil


def main():
    print('cmd entry:', sys.argv)

    if len(sys.argv) != 2:
        print("Argument != 2")

    path_1 = Path(sys.argv[1])

    musics = []
    videos = []
    photos = []
    documents = []
    archives = []
    others = []
    know_ext = []
    unknown_ext = []
    directory_images = f"{path_1}/images"
    directory_video = f"{path_1}/video"
    directory_music = f"{path_1}/music"
    directory_documents = f"{path_1}/documents"
    directory_archives = f"{path_1}/archives"

    def normalize(name):
        translit_dict = {
            'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'ґ': 'g', 'д': 'd', 'е': 'e', 'є': 'ie',
            'ж': 'zh', 'з': 'z', 'и': 'y', 'і': 'i', 'ї': 'i', 'й': 'i', 'к': 'k', 'л': 'l',
            'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
            'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ь': '', 'ю': 'iu',
            'я': 'ia', 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'H', 'Ґ': 'G', 'Д': 'D', 'Е': 'E',
            'Є': 'Ye', 'Ж': 'Zh', 'З': 'Z', 'И': 'Y', 'І': 'I', 'Ї': 'Yi', 'Й': 'Y', 'К': 'K',
            'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
            'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ь': '',
            'Ю': 'Yu', 'Я': 'Ya'
        }
        translit = ''
        for char in name:
            if char in translit_dict:
                translit += translit_dict[char]
            elif char.isalnum():
                translit += char
            elif char == ".":
                translit += char
            else:
                translit += '_'
        return translit

    def sorted_folder(path_1):
        for el in path_1.iterdir():
            name = el.name
            trans_name = normalize(name)
            x = f"{path_1}\\{trans_name}"
            x_path = Path(x)
            y = os.rename(el, x)
            if el.is_dir():
                if x_path.name == "images" or x_path.name == "video" or x_path.name == "documents" or x_path.name == "music" or x_path.name == "archives":
                    continue
                if not os.listdir(x):
                    os.rmdir(x)
                else:
                    sorted_folder(x_path)
            else:
                if x.endswith(".mp3") or x.endswith('.ogg') or x.endswith('.wav') or x.endswith('.amr'):
                    musics.append(trans_name)
                    if not os.path.exists(directory_music):
                        os.makedirs(directory_music)
                    shutil.move(x, directory_music)
                    if x_path.suffix in know_ext:
                        continue
                    else:
                        know_ext.append(x_path.suffix)
                elif x.endswith(".avi") or x.endswith('.mp4') or x.endswith('.mov') or x.endswith('.mkv'):
                    videos.append(trans_name)
                    if not os.path.exists(directory_video):
                        os.makedirs(directory_video)
                    shutil.move(x, directory_video)
                    if x_path.suffix in know_ext:
                        continue
                    else:
                        know_ext.append(x_path.suffix)
                elif x.endswith('.jpeg') or x.endswith('.png') or x.endswith('.jpg') or x.endswith('.svg'):
                    photos.append(trans_name)
                    if not os.path.exists(directory_images):
                        os.makedirs(directory_images)
                    shutil.move(x, directory_images)
                    if x_path.suffix in know_ext:
                        continue
                    else:
                        know_ext.append(x_path.suffix)
                elif x.endswith('.doc') or x.endswith('.docx') or x.endswith('.txt') or x.endswith('.pdf') or x.endswith('xlsx') or x.endswith('.pptx') or x.endswith('.ppt'):
                    documents.append(trans_name)
                    if not os.path.exists(directory_documents):
                        os.makedirs(directory_documents)
                    shutil.move(x, directory_documents)
                    if x_path.suffix in know_ext:
                        continue
                    else:
                        know_ext.append(x_path.suffix)
                elif x.endswith('.zip') or x.endswith('.gz') or x.endswith('.tar'):
                    archives.append(trans_name)
                    if not os.path.exists(directory_archives):
                        os.makedirs(directory_archives)
                    unpack_folder = os.path.splitext(trans_name)[0]
                    b = f"{directory_archives}/{unpack_folder}"
                    unpack = shutil.unpack_archive(x, b)
                    os.remove(x)
                    if x_path.suffix in know_ext:
                        continue
                    else:
                        know_ext.append(x_path.suffix)
                else:
                    others.append(trans_name)
                    if x_path.suffix in unknown_ext:
                        continue
                    else:
                        unknown_ext.append(x_path.suffix)

    if path_1.is_dir():
        sorted_folder(path_1)
    else:
        print("This is not a folder")

    print(f"Music = {musics}")
    print(f"Videos = {videos}")
    print(f"Photos = {photos}")
    print(f"Documents = {documents}")
    print(f"Archives = {archives}")
    print(f"Others = {others}")
    print(f"Know_ext = {know_ext}")
    print(f"Unknown = {unknown_ext}")


if __name__ == "__main__":
    main()
