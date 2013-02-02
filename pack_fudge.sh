#!/bin/bash


py=`which python2`
if [ -z $py ]; then
    echo "install python2"
    exit
fi

if [ -z $2 ]; then
    echo -e "Usage:\n  $0  <dump>  <pak_file>   <empty_folder_to_extract_pak>"  
    echo            "  $0  <pack>  <folder_where_files_exist>   <new_pak_file>" 
    exit
fi

[[ $1 == "pack" ]] &&  $(which rm)  ${2}/*~

if [ -f grit/format/pack_fudge.py ]; then
    $py grit/format/pack_fudge.py $@
elif [ -f format/pack_fudge.py ]; then
    $py format/pack_fudge.py $@
else
    echo "$0  working dir needs to be adjacent to, or within the \"pack_fudge\" folder."
fi
