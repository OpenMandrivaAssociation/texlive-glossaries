# revision 32171
# category Package
# catalog-ctan /macros/latex/contrib/glossaries
# catalog-date 2013-11-17 00:00:10 +0100
# catalog-license lppl
# catalog-version 4.01
Name:		texlive-glossaries
Epoch:		1
Version:	4.01
Release:	5
Summary:	Create glossaries and lists of acronyms
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/glossaries
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/glossaries.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/glossaries.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/glossaries.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-glossaries.bin = %{EVRD}

%description
The glossaries package supports acronyms and multiple
glossaries, and has provision for operation in several
languages (using the facilities of either babel or
polyglossia). New entries are defined to have a name and
description (and optionally an associated symbol). Support for
multiple languages is offered, and plural forms of terms may be
specified. An additional package, glossaries-accsupp, can make
use of the accsupp package mechanisms for accessibility support
for PDF files containing glossaries. The user may define new
glossary styles, and preambles and postambles can be specified.
There is provision for loading a database of terms, but only
terms used in the text will be added to the relevant glossary.
The package uses an indexing program to provide the actual
glossary; either makeindex or xindy may serve this purpose, and
a Perl script is provided to serve as interface. The package
distribution also provides the mfirstuc package, for changing
the first letter of a word to upper case. The package
supersedes the author's glossary package (which is now
obsolete), and a conversion tool is provided.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/makeglossaries
%{_texmfdistdir}/scripts/glossaries/glossaries.perl
%{_texmfdistdir}/scripts/glossaries/makeglossaries
%{_texmfdistdir}/scripts/glossaries/makeglossaries.bat
%{_texmfdistdir}/scripts/glossaries/mfirstuc.perl
%{_texmfdistdir}/tex/latex/glossaries/base/glossaries-babel.sty
%{_texmfdistdir}/tex/latex/glossaries/base/glossaries-compatible-207.sty
%{_texmfdistdir}/tex/latex/glossaries/base/glossaries-compatible-307.sty
%{_texmfdistdir}/tex/latex/glossaries/base/glossaries-polyglossia.sty
%{_texmfdistdir}/tex/latex/glossaries/base/glossaries.sty
%{_texmfdistdir}/tex/latex/glossaries/base/mfirstuc.sty
%{_texmfdistdir}/tex/latex/glossaries/dict/glossaries-dictionary-Brazilian.dict
%{_texmfdistdir}/tex/latex/glossaries/dict/glossaries-dictionary-Danish.dict
%{_texmfdistdir}/tex/latex/glossaries/dict/glossaries-dictionary-Dutch.dict
%{_texmfdistdir}/tex/latex/glossaries/dict/glossaries-dictionary-English.dict
%{_texmfdistdir}/tex/latex/glossaries/dict/glossaries-dictionary-French.dict
%{_texmfdistdir}/tex/latex/glossaries/dict/glossaries-dictionary-German.dict
%{_texmfdistdir}/tex/latex/glossaries/dict/glossaries-dictionary-Irish.dict
%{_texmfdistdir}/tex/latex/glossaries/dict/glossaries-dictionary-Italian.dict
%{_texmfdistdir}/tex/latex/glossaries/dict/glossaries-dictionary-Magyar.dict
%{_texmfdistdir}/tex/latex/glossaries/dict/glossaries-dictionary-Polish.dict
%{_texmfdistdir}/tex/latex/glossaries/dict/glossaries-dictionary-Serbian.dict
%{_texmfdistdir}/tex/latex/glossaries/dict/glossaries-dictionary-Spanish.dict
%{_texmfdistdir}/tex/latex/glossaries/expl/glossaries-accsupp.sty
%{_texmfdistdir}/tex/latex/glossaries/styles/glossary-hypernav.sty
%{_texmfdistdir}/tex/latex/glossaries/styles/glossary-inline.sty
%{_texmfdistdir}/tex/latex/glossaries/styles/glossary-list.sty
%{_texmfdistdir}/tex/latex/glossaries/styles/glossary-long.sty
%{_texmfdistdir}/tex/latex/glossaries/styles/glossary-longragged.sty
%{_texmfdistdir}/tex/latex/glossaries/styles/glossary-mcols.sty
%{_texmfdistdir}/tex/latex/glossaries/styles/glossary-super.sty
%{_texmfdistdir}/tex/latex/glossaries/styles/glossary-superragged.sty
%{_texmfdistdir}/tex/latex/glossaries/styles/glossary-tree.sty
%doc %{_texmfdistdir}/doc/latex/glossaries/CHANGES
%doc %{_texmfdistdir}/doc/latex/glossaries/INSTALL
%doc %{_texmfdistdir}/doc/latex/glossaries/README
%doc %{_texmfdistdir}/doc/latex/glossaries/glossaries-code.pdf
%doc %{_texmfdistdir}/doc/latex/glossaries/glossaries-user.html
%doc %{_texmfdistdir}/doc/latex/glossaries/glossaries-user.pdf
%doc %{_texmfdistdir}/doc/latex/glossaries/glossaries-user.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/glossariesbegin.html
%doc %{_texmfdistdir}/doc/latex/glossaries/glossariesbegin.pdf
%doc %{_texmfdistdir}/doc/latex/glossaries/glossariesbegin.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/glossary2glossaries.html
%doc %{_texmfdistdir}/doc/latex/glossaries/glossary2glossaries.pdf
%doc %{_texmfdistdir}/doc/latex/glossaries/glossary2glossaries.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/mfirstuc-manual.html
%doc %{_texmfdistdir}/doc/latex/glossaries/mfirstuc-manual.pdf
%doc %{_texmfdistdir}/doc/latex/glossaries/mfirstuc-manual.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/README-samples
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/database1.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/database2.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/minimalgls.pdf
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/minimalgls.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sample-FnDesc.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sample-crossref.pdf
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sample-crossref.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sample-custom-acronym.pdf
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sample-custom-acronym.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sample-dual.pdf
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sample-dual.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sample-entryfmt.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sample-index.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sample-inline.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sample-langdict.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sample-mfirstuc.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sample-newkeys.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sample-nomathhyper.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sample-numberlist.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sample-prefix.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sample-si.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sample.pdf
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sample.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sample4col.pdf
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sample4col.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sampleAcr.pdf
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sampleAcr.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sampleAcrDesc.pdf
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sampleAcrDesc.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sampleDB.pdf
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sampleDB.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sampleDesc.pdf
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sampleDesc.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sampleEq.pdf
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sampleEq.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sampleEqPg.pdf
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sampleEqPg.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sampleNtn.pdf
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sampleNtn.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/samplePeople.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sampleSec.pdf
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sampleSec.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sampleSort.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sampleaccsupp.pdf
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sampleaccsupp.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sampleacronyms.pdf
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sampleacronyms.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sampletree.pdf
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sampletree.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sampleutf8.pdf
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/sampleutf8.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/samplexdy-compatible207.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/samplexdy-mc.xdy
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/samplexdy-mc207.xdy
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/samplexdy.pdf
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/samplexdy.tex
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/samplexdy2.pdf
%doc %{_texmfdistdir}/doc/latex/glossaries/samples/samplexdy2.tex
#- source
%doc %{_texmfdistdir}/source/latex/glossaries/glossaries.dtx
%doc %{_texmfdistdir}/source/latex/glossaries/glossaries.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/glossaries/makeglossaries makeglossaries
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
