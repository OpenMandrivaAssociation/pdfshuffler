Name:		pdfshuffler
Version:	0.5
Release:	%mkrel 1
Summary:	PDF file merging, rearranging, and splitting
Group:		Publishing
License:	GPLv2+
URL:		http://sourceforge.net/projects/pdfshuffler/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		pdfshuffler-0.5-fix-desktop.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch

%py_requires -d
BuildRequires:	python-setuptools
BuildRequires:	gettext

Requires:	pygtk2
Requires:	python-pypdf
Requires:	python-pypoppler

%description
PDF-Shuffler is a small python-gtk application, which helps the user
to merge or split pdf documents and rotate, crop and rearrange their
pages using an interactive and intuitive graphical interface.

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1.*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/pixmaps/%{name}.svg
%{py_puresitedir}/%{name}-*.egg-info

#--------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0

%install
%__rm -rf %{buildroot}
%{__python} setup.py install --root %{buildroot} --no-compile
%find_lang %{name}

%clean
%__rm -rf %{buildroot}
