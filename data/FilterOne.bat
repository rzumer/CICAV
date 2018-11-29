echo clip = ffvideosource("in/%~n1%~x1") > "%~d1%~p1%~n1.avs"
echo import("Filter.avs") >> "%~d1%~p1%~n1.avs"
x264 --preset veryslow --crf 15 --deblock -1:-1 --output "out/%~n1.mkv" "%~d1%~p1%~n1.avs"
