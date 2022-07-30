# Technical Guide

I've decided to write this entire Letter in [Common Markdown](https://commonmark.org/) for simplicity and to have simple formatting Options.
I used [mdbook](https://rust-lang.github.io/mdBook/index.html) to build and the [mdbook-pdf](https://github.com/HollowMan6/mdbook-pdf) Backend to generate pdf files.

# Installation and building

If you want to build this book from Scratch these Instructions will get you Started.
These have only been tested on Arch Linux and Pop!_OS 22.04 though so I cannot garantee then to work anywhere else.

1. Install cargo and rustc, preferably through rustup for easy update managing
2. Install a chromium based webbrowser which has chroumium-headless available(chromium, google chrome, microsoft edge etc), Possibly not needed on windows 10+ since Edge is Provided with the base OS installation.
3. Install [python](https://www.python.org/) 3.10+ and add it to your PATH so you can use the python3 command and have it invoke python 3.10 or newer.
4. Install mdbook and mdbook-pdf through cargo:
```sh
cargo install mdbook
cargo install mdbook-pdf
cargo install mdbook-footnote
```
5. clone this repository using git or aquire the files in another way
```sh
git clone https://github.com/Popaulol/ipad_anschreiben
cd ipad_anschreiben
```
6. build the book using mdbook. Both the pdf and html versions can be found in the `book` directory
```
mdbook build
```
