# Technical Guide

I've decided to write this entire Letter in [Common Markdown](https://commonmark.org/) for simplicity and to have simple formatting Options.
I used [mdbook](https://rust-lang.github.io/mdBook/index.html) to build the book
 and the [mdbook-pdf](https://github.com/HollowMan6/mdbook-pdf) Backend to generate pdf files.
The footnotes are provided by [mdbook-footnote](https://github.com/daviddrysdale/mdbook-footnote)

## Installation and building

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
## Issues
If you follow this guide, you will notice that the internal links inside the pdf will be broken.
There is already a [PR on the main mdbook repo](https://github.com/rust-lang/mdBook/pull/1738) on the way but until that is merged, you might want to use the PR fork for that specific PR instead of vanilla mdbook:
```sh
cargo install --git https://github.com/HollowMan6/mdBook mdbook
```
This will most likely lead to a few warnings by the various preproccessors and backends, since this fork based on mdbook 0.4.20 whilst the plugins will expect a newer version but if the PR gets merged and/or the upstream PR repo gets updated to a newer mdbook version, this won't be a problem anymore. The only thing changed since this mdbook version is a minor build issue fix for rust-nightly which isn't relevant for this book.

Since the table in the alternatives chapter is to big to be done in markdown, it was in libre office and can be found in this root folder of the repo. It has to be manually integrated into the finished pdf by having a `AlternativenTabelle.pdf` in the root of the project and then running `gerenerate.sh`.
This script requires [qpdf](https://github.com/qpdf/qpdf) to be installed on your PATH.
