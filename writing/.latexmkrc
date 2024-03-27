$do_cd    = 1;
$pdf_mode = 4;
$out_dir  = "out";
$lualatex = "lualatex -file-line-error -interaction=nonstopmode -halt-on-error -shell-escape -synctex=1 %O %S";
ensure_path('TEXINPUTS', './template/')
