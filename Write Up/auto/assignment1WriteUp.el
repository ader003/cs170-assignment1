(TeX-add-style-hook
 "assignment1WriteUp"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "a4paper")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("babel" "english") ("inputenc" "utf8x") ("fontenc" "T1") ("geometry" "a4paper" "top=3cm" "bottom=2cm" "left=3cm" "right=3cm" "marginparwidth=1.75cm") ("todonotes" "colorinlistoftodos") ("hyperref" "colorlinks=true" "allcolors=blue")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "babel"
    "inputenc"
    "fontenc"
    "multicol"
    "geometry"
    "amsmath"
    "graphicx"
    "todonotes"
    "hyperref"))
 :latex)

