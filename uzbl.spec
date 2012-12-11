%define snapshot 20120514

Name:		uzbl
Summary:	Web browser following the UNIX philosophy
Version:	0.0
Release:	%mkrel 0.%{snapshot}.1
Source0:	%{name}-%{snapshot}.tar.xz
Requires:	xclip
BuildRequires:	gtk+3-devel webkitgtk3-devel
Provides:	webclient
License:	GPLv3
Group:		Networking/WWW
URL:		http://www.uzbl.org/

%description
Uzbl follows the UNIX philosophy - "Write programs that do one thing
and do it well. Write programs to work together. Write programs to handle
text streams, because that is a universal interface."

 * very minimal graphical interface. You only see what you need
 * what is not browsing, is not in uzbl. Things like URL changing,
   loading/saving of bookmarks, saving history, downloads, ... are
   handled through external scripts that you write
 * controllable through various means such as FIFO and socket files,
   stdin, keyboard and more
 * advanced, customizable keyboard interface with support for modes,
   modkeys, multichars, variables (keywords) etc. (e. g. you can tweak
   the interface to be vim-like, emacs-like or any-other-program-like)
 * focus on plain text storage for your data and configs in simple,
   parseable formats
 * Uzbl keeps it simple, and puts you in charge.

%prep
%setup -q -n %name-%snapshot

%build
%make 

%install
%{__rm} -Rf %{buildroot}
%make DESTDIR=%buildroot PREFIX=%_prefix install
install -d %{buildroot}%{_docdir}
mv %{buildroot}%{_datadir}/%{name}/docs %{buildroot}%{_docdir}/%{name}

%clean
%{__rm} -Rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}-*
%{_datadir}/%{name}
%doc %{_docdir}/%{name}/*


%changelog
* Mon Jul 02 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.0-0.20120514.1mdv2012.0
+ Revision: 807785
- update to 20120514 snapshot

* Mon Dec 12 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.0-0.1.20111128.1
+ Revision: 740436
- Use GTK+3
- Update to 20111128

* Mon Jun 20 2011 Funda Wang <fwang@mandriva.org> 0.0-0.1.20100805.2
+ Revision: 686156
- rebuild for new webkit

* Sun Aug 08 2010 Rémy Clouard <shikamaru@mandriva.org> 0.0-0.1.20100805.1mdv2011.0
+ Revision: 567760
- new snapshot
- use xz instead of bzip2

* Sun Apr 25 2010 Rémy Clouard <shikamaru@mandriva.org> 0.0-0.1.20100408.2mdv2010.1
+ Revision: 538532
- add xclip to match default config and clean spec

* Thu Apr 08 2010 Rémy Clouard <shikamaru@mandriva.org> 0.0-0.1.20100408.1mdv2010.1
+ Revision: 533129
- bump release

* Mon Nov 30 2009 Rémy Clouard <shikamaru@mandriva.org> 0.0-0.1.20091130.1mdv2010.1
+ Revision: 472126
- bump release

* Sun Jun 07 2009 Nicolas Vigier <nvigier@mandriva.com> 0.0-0.1.20090606.2mdv2010.0
+ Revision: 383722
- install doc and example config files in /usr/share/uzbl

* Sat Jun 06 2009 Nicolas Vigier <nvigier@mandriva.com> 0.0-0.1.20090606.1mdv2010.0
+ Revision: 383376
- import uzbl


