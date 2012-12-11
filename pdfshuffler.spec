Name:		pdfshuffler
Version:	0.6.0
Release:	1
Summary:	PDF file merging, rearranging, and splitting
Group:		Publishing
License:	GPLv2+
URL:		http://sourceforge.net/projects/pdfshuffler/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		pdfshuffler-0.5-fix-desktop.patch
BuildArch:	noarch

BuildRequires:	python-devel
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
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1.*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/%{name}.ui
%{_datadir}/%{name}/icons/hicolor/scalable/%{name}.svg
%{py_puresitedir}/%{name}-0.6.0-py*.egg-info
%{py_sitedir}/pdfshuffler/

#--------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0

%install
python setup.py install --root %{buildroot} --no-compile
%find_lang %{name}



%changelog
* Thu Jul 19 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.6.0-1
+ Revision: 810269
- version update 0.6.0

* Mon Jan 30 2012 Vladimir Testov <vladimir.testov@rosalab.ru> 0.5.1-3
+ Revision: 769812
- fixed: replaced %%{pyver} with %%{py_ver}

* Thu Nov 04 2010 Luc Menut <lmenut@mandriva.org> 0.5.1-2mdv2011.0
+ Revision: 593470
- fix file list (.egg-info filename)
- rebuild for python 2.7
- drop %%py_requires macro
- use %%pyver macro for .egg-info file

* Tue Oct 12 2010 Luc Menut <lmenut@mandriva.org> 0.5.1-1mdv2011.0
+ Revision: 585241
- update to 0.5.1 (bugfix release)

* Tue Jan 05 2010 Luc Menut <lmenut@mandriva.org> 0.5-1mdv2010.1
+ Revision: 486508
- update to version 0.5
  drop translations patch (merged upstream)
  rediff fix-desktop patch

* Sun Aug 30 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.4.2-1mdv2010.0
+ Revision: 422625
- change layout

  + Luc Menut <lmenut@mandriva.org>
    - import pdfshuffler

