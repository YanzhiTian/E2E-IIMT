# build images with text.de text.en

python ../build_image/build_img.py --prefix ./de-en --font_path ../build_image/TimesNewRoman.ttf --total_corpus_path text.de --l de
python ../build_image/build_img.py --prefix ./de-en --font_path ../build_image/TimesNewRoman.ttf --total_corpus_path text.en --l en
