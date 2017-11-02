(TeX-add-style-hook
 "assignment1WriteUp"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "a4paper")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("babel" "english") ("inputenc" "utf8x") ("fontenc" "T1") ("geometry" "a4paper" "top=3cm" "bottom=2cm" "left=3cm" "right=3cm" "marginparwidth=1.75cm") ("todonotes" "colorinlistoftodos") ("hyperref" "colorlinks=true" "allcolors=blue")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "babel"
    "inputenc"
    "fontenc"
    "geometry"
    "amsmath"
    "graphicx"
    "todonotes"
    "hyperref")
   (LaTeX-add-labels
    "fig:frog"
    "tab:widgets")
   (LaTeX-add-bibliographies
    "sample"))
 :latex)

