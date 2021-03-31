import os
import glob
import re
import json

def main():
  FOLDER_NAME = "FinalProject"
  FOLDERS = glob.glob("%s//*//" % FOLDER_NAME)
  RENAME_DICT = {}

  try:
    for folder in FOLDERS:
      print(folder)
      FDR_NAME = re.search(r"\\(.+?)\\", folder).group(1)
      mob_files = glob.glob("%s*.mob" % folder)

      mob_dict = {}
      for i in range(len(mob_files)):
        try:
          with open(mob_files[i], "r") as mob_json:
            mob_dict = json.load(mob_json)
            new_name = re.sub("\\\\", "_", os.path.splitext(mob_files[i])[0])
            mob_dict["name"] = new_name
            mob_dict["flowchart"]["name"] = new_name
          with open(mob_files[i], "w") as mob_json:
            json.dump(mob_dict, mob_json)
        except UnicodeDecodeError as err:
          print(mob_files[i])
          continue

  except Exception as e:
    raise e

if __name__ == "__main__":
  main()