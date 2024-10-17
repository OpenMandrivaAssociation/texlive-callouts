Name:		texlive-callouts
Version:	44899
Release:	2
Summary:	Put simple annotations and notes inside a picture
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/callouts
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/callouts.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/callouts.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines the annotation environment in which
callouts, notes, arrows, and the like can be placed to describe
certain parts of a picture.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/callouts
%doc %{_texmfdistdir}/doc/latex/callouts

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
