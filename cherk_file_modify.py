import hashlib
import os
import shelve


def get_file_hash(file_path):
    hasher = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def update_hash(
    filename_filepath_dict: dict,
    hash_file_path: str = os.path.join(os.getcwd(), "template", "hash.db"),
    update_file_name: str = "",
):
    with shelve.open(hash_file_path) as s:
        if (s.__len__() < filename_filepath_dict.__len__()) and (
            not (update_file_name)
        ):
            s.update({k: get_file_hash(v) for k, v in filename_filepath_dict.items()})
        else:
            s[update_file_name] = get_file_hash(
                filename_filepath_dict[update_file_name]
            )


def template_file_is_modify(
    file_name,
    filename_filepath_dict: dict,
    hash_file_path: str = os.path.join(os.getcwd(), "template", "hash.db"),
):
    with shelve.open(hash_file_path) as s:
        newhash = get_file_hash(filename_filepath_dict[file_name])
        oldhash = s.get(file_name)
        return newhash != oldhash
