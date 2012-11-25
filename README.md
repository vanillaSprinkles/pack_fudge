pack_fudge!

Requirements: python2 ... and a few others; if any errors, do the needful to fix and/or report the problem.

pack_fudge allows google chrome browswer pak files to be unpacked and repacked.

Origianl files sync'd from google-chrome-dev-25 (http://commondatastorage.googleapis.com/chromium-browser-official/chromium-25.0.1323.1.tar.bz2)
This is essentially the chrome source's grit folder with a modified py file (tools/grit/grit/format/data_pack.py) modified to pack_fudge.py

I did not code the majority of this project and so I do not claim the cretit of the code except for the small snipit within pack-fudge.py and pack_fudge.sh



Usage:

./pack_fudge.sh  dump  pak_file   empty_folder_to_extract_pak

./pack_fudge.sh  pack  folder_where_files_exist   new_pak_file

