import json
import os.path


def main():
    fileList = []
    path = "movies"
    # Extract each filename in the folder
    for filenames in os.walk(path):
        fileList.append(filenames)

    data_list = []
    # Using the filename transform the data
    for i in range(len(filenames[2])):
        try:
            data = json.load(open('movies/' + filenames[2][i], encoding='utf-8'))
            data_final = dict((k, data[k]) for k in ('original_title', 'budget', 'genres', 'popularity', "release_date",
                                                     "revenue", "runtime", "vote_average", "vote_count", "spoken_languages"))
            # Data transformation on genre and spoken language list
            genres = []
            for i in range(len(data_final["genres"])):
                genres.append(data_final["genres"][i]['name'])
            data_final["genres"] = ", ".join(genres)

            spoken_languages = []
            for i in range(len(data_final["spoken_languages"])):
                genres.append(data_final["spoken_languages"][i]['name'])
            data_final["spoken_languages"] = ", ".join(spoken_languages)

            # Add the final data list into the main list
            data_list.append(data_final)
        except Exception:
            pass
    
    # Output the file as the main json using the json.dump() method
    out_file = open("movies.json", "w")
    json.dump(data_list, out_file, indent=2)
    out_file.close()


if __name__ == '__main__':
    main()