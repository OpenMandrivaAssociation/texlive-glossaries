Name:		texlive-glossaries
Epoch:		1
Version:	4.41
Release:	1
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
%{_texmfdistdir}/scripts/glossaries
%{_texmfdistdir}/tex/latex/glossaries
%doc %{_texmfdistdir}/doc/latex/glossaries
%doc %{_texmfdistdir}/doc/man/man1/*
#- source
%doc %{_texmfdistdir}/source/latex/glossaries

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
